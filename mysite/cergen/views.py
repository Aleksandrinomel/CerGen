from django.shortcuts import render
from django.http import JsonResponse
from .models import DescriptionAndNumber
import csv
import codecs
from .points import points


def index(request):
    serial_numbers = []
    global list_of_rows
    list_of_rows = []
    if request.method == 'POST' and 'equip' in request.POST:
        try:
            print(request.POST)

            f = request.FILES['equip']
            dreader = csv.DictReader(codecs.iterdecode(f, 'utf-8'), delimiter=';')
            for row in dreader:
                list_of_rows.append(row)
                serial_numbers.append(row['Serial Number'])
        except:
            pass
    if request.method == 'POST' and 'note' in request.POST:
        start = float(request.POST['measuringRangeFrom'])
        end = float(request.POST['measuringRangeTo'])
        mdop = bool(int(request.POST['maximumToleranceProcent']))
        mdo = float(request.POST['maximumTolerance'])
        npoints = int(request.POST['testPointsNumber'])
        rnd = int(request.POST['decimals'])
        print(type(start), type(end), mdo, mdop, npoints, rnd)
        #for row in request.POST.items():
        context = dict(request.POST.items())
        return render(request, 'cergen/template.html', context)



    procedure_descriptions = DescriptionAndNumber.objects.values_list('description', flat=True)
    procedure_numbers = DescriptionAndNumber.objects.values_list('number', flat=True)

    context = {
        'serial_numbers': serial_numbers,
        'procedure_descriptions': procedure_descriptions,
        'procedure_numbers': procedure_numbers
    }
    return render(request, 'cergen/index.html', context)


def get_serial_number(request):
    if request.method == 'GET':
        json_data = []
        for row in list_of_rows:
            if row['Serial Number'] == request.GET['serial_number']:
                json_data = row
    return JsonResponse(json_data, safe=False)


def get_test_points(request):
    if request.method == 'GET':
        json_data = []
        start = float(request.GET['measuringRangeFrom'])
        end = float(request.GET['measuringRangeTo'])
        mdop = bool(int(request.GET['maximumToleranceProcent']))
        mdo = float(request.GET['maximumTolerance'])
        npoints = int(request.GET['testPointsNumber'])
        rnd = int(request.GET['decimals'])
        print(type(start), type(end), mdo, mdop, npoints, rnd)

        p = points(start, end, mdop, mdo, npoints, rnd)
        print(p)
    return JsonResponse(p, safe=False)


def template(request):

    return render(request, 'cergen/template.html')
