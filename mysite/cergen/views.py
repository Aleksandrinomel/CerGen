from django.shortcuts import render
from django.http import JsonResponse
from .models import DescriptionAndNumber, ReferenceEquipment
import csv
import codecs
from .points import points
from datetime import datetime


def index(request):
    context = {}
    print(request.POST)

    # Парсер csv с приборами
    if request.method == 'POST' and 'equip' in request.FILES:
        global equipments
        equipments = []
        serial_numbers = []
        f = request.FILES['equip']
        dreader = csv.DictReader(codecs.iterdecode(f, 'utf-8'), delimiter=';')
        for row in dreader:
            equipments.append(row)
            serial_numbers.append(row['Serial Number'])

    # Обработка данных из формы для построения шаблона сертификата
    if request.method == 'POST' and 'note' in request.POST:
        context.update(dict(request.POST.items()))

        # Таблица точек тестирования
        test_points = []
        for i in range(1, int(request.POST['testPointsNumber']) + 1):
            test_point = []
            test_point.extend([request.POST['testPoint' + str(i)], request.POST['pointValue' + str(i)],
                               request.POST['referenceValue' + str(i)], request.POST['displayValue' + str(i)],
                               request.POST['deviation' + str(i)], request.POST['mdoRnd' + str(i)]])
            test_points.append(test_point)

        context.setdefault('testPoints', test_points)

        # Таблица инструментов
        tools = []
        for i in range(1, 5):
            tool = []
            if request.POST['devName' + str(i)] != '':
                tool.extend([request.POST['devName' + str(i)], request.POST['devDescription' + str(i)],
                             request.POST['protocolNumber' + str(i)], request.POST['calibrationDate' + str(i)],
                             request.POST['validity' + str(i)]])
                tools.append(tool)
        print(tools)
        context.setdefault('tools', tools)

        # Таблица аксессуаров
        accessories = []
        for i in range(1, 4):
            accessory = []
            if request.POST['typeAccessory' + str(i)] != '':
                accessory.extend([request.POST['typeAccessory' + str(i)], request.POST['descAccessory' + str(i)],
                                  request.POST['accessorySerialNumber' + str(i)]])
                accessories.append(accessory)
        print(accessories)
        context.setdefault('accessories', accessories)

        return render(request, 'cergen/template.html', context)

    procedure_descriptions = DescriptionAndNumber.objects.values_list('description', flat=True)
    procedure_numbers = DescriptionAndNumber.objects.values_list('number', flat=True)
    dev_names = ReferenceEquipment.objects.values_list('description', flat=True)

    print_calibration_date = datetime.now().strftime('%d.%m.%Y')

    context = {
        'print_calibration_date': print_calibration_date,
        'dev_names': dev_names,
        'serial_numbers': serial_numbers,
        'procedure_descriptions': procedure_descriptions,
        'procedure_numbers': procedure_numbers
    }
    return render(request, 'cergen/index.html', context)


def get_serial_number(request):
    if request.method == 'GET':
        json_data = []
        for row in equipments:
            if row['Serial Number'] == request.GET['serial_number']:
                json_data = row
    return JsonResponse(json_data, safe=False)


def get_test_points(request):
    if request.method == 'GET':
        start = float(request.GET['measuringRangeFrom'])
        end = float(request.GET['measuringRangeTo'])
        mdop = bool(int(request.GET['maximumToleranceProcent']))
        mdo = float(request.GET['maximumTolerance'])
        npoints = int(request.GET['testPointsNumber'])
        rnd = int(request.GET['decimals'])

        p = points(start, end, mdop, mdo, npoints, rnd)
        print(p)
    return JsonResponse(p, safe=False)


def get_description_procedure(request):
    if request.method == 'GET':
        procedure = DescriptionAndNumber.objects.get(description=request.GET['description_procedure'])
        number = procedure.number
    return JsonResponse(number, safe=False)


def get_dev_name(request):
    if request.method == 'GET':
        dev_stuff = ReferenceEquipment.objects.filter(description=request.GET['dev_name']).values()[0]
        print(dev_stuff)
    return JsonResponse(dev_stuff, safe=False)


def template(request):

    return render(request, 'cergen/template.html')
