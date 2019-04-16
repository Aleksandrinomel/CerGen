from django.shortcuts import render
from django.http import JsonResponse
import csv
import codecs
import json
import sys

global dreader
def index(request):
    serial_numbers = []
    global list_of_rows
    list_of_rows = []
    if request.method == 'POST':
        f = request.FILES['equip']
        print(f)
        dreader = csv.DictReader(codecs.iterdecode(f, 'utf-8'), delimiter=';')
        for row in dreader:
            list_of_rows.append(row)
            serial_numbers.append(row['Serial Number'])
    context = {
        'serial_numbers': serial_numbers
    }
    print(list_of_rows)
    return render(request, 'cergen/index.html', context)


def get_serial_number(request):
    if request.method == 'GET':
        json_data = []
        for row in list_of_rows:
            if row['Serial Number'] == request.GET['serial_number']:
                json_data = row
    return JsonResponse(json_data, safe=False)


