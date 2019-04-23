import csv
from .models import ReferenceEquipment


with open('RefEquip.csv') as re:
    dreader = csv.DictReader(re, delimiter=';')
    for row in dreader:
        ReferenceEquipment.objects.create(description=row['description'],serial_number=row['serial_number'],protocol=row['protocol'],callibration_data=row['callibration_data'],validity=row['validity'])