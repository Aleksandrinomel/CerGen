from django.db import models


class DescriptionAndNumber(models.Model):
    class Meta:
        db_table = "DescriptionAndNumber"

    description = models.CharField(max_length=150)
    number = models.CharField(max_length=150)

    def __str__(self):
        return '<DescriptionAndNumber {} {} >'.format(self.description, self.number)


class ReferenceEquipment(models.Model):
    class Meta:
        db_table = "ReferenceEquipment"

    description = models.CharField(max_length=150)
    serial_number = models.CharField(max_length=150)
    protocol = models.CharField(max_length=150)
    callibration_data = models.CharField(max_length=150)
    validity = models.CharField(max_length=150)

    def __str__(self):
        return '<DescriptionAndNumber {}>'.format(self.description)
