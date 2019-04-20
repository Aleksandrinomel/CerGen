from django.shortcuts import render
from django.http import JsonResponse
from .models import DescriptionAndNumber
import csv
import codecs
import json
import random
from .points import points

def index(request):

    if request.method == 'GET' :
        print(request.GET['signal'])
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

        def points(start, end, mdop, mdo, npoints, rnd):
            list_of_points_ref = [start, end]
            s_n = start - end
            list_of_points_dev = []
            list_of_points_delta = []
            point = start
            all_points = {}

            for i in range(npoints - 2):
                point += ((end - start) / (npoints - 1))
                list_of_points_ref.append(round(point, rnd))
                list_of_points_ref.sort()

            if mdop:
                mdo /= 100
                for j in list_of_points_ref:
                    rand = random.uniform(-s_n * mdo, s_n * mdo)
                    list_of_points_dev.append(round(j + rand, rnd))
                for i in range(len(list_of_points_ref)):
                    list_of_points_delta.append(round(abs(abs(list_of_points_ref[i])-abs(list_of_points_dev[i])) * 100 / s_n, rnd))
            else:
                for j in list_of_points_ref:
                    rand = random.uniform(-mdo, mdo)
                    list_of_points_dev.append(round(j + rand, rnd))
                for i in range(len(list_of_points_ref)):
                    list_of_points_delta.append(round(abs(abs(list_of_points_ref[i]) - abs(list_of_points_dev[i])), rnd))

            for n in range(npoints):
                all_points[n + 1] = [list_of_points_ref[n], list_of_points_dev[n], list_of_points_delta[n]]

            return all_points

        d = points(start, end, mdop, mdo, npoints, rnd)
        print(d)

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


