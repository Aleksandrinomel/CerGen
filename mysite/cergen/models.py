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
        return '<ReferenceEquipment {}>'.format(self.description)


class Principle(models.Model):
    class Meta:
        db_table = "Principle"

    category = models.CharField(max_length=150)
    principle = models.CharField(max_length=150)

    def __str__(self):
        return '<Principle {} {} >'.format(self.category, self.principle)


class Accessory(models.Model):
    class Meta:
        db_table = "Accessory"

    type = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    serial_number = models.CharField(max_length=150)

    def __str__(self):
        return '<Accessory {} {} {}>'.format(self.type, self.description, self.serial_number)


class MeasuringRangeUnits(models.Model):
    class Meta:
        db_table = "MeasuringRangeUnits"

    units = models.CharField(max_length=20)

    def __str__(self):
        return '<MeasuringRangeUnits {}>'.format(self.units)


class OutputSignalUnits(models.Model):
    class Meta:
        db_table = "OutputSignalUnits"

    units = models.CharField(max_length=20)

    def __str__(self):
        return '<OutputSignalUnits {}>'.format(self.units)


class CalibrationRangeUnits(models.Model):
    class Meta:
        db_table = "CalibrationRangeUnits"

    units = models.CharField(max_length=20)

    def __str__(self):
        return '<CalibrationRangeUnits {}>'.format(self.units)


