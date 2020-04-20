from django.db import models

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=264)

    def __str__(self):
        return self.name

class Column(models.Model):
    name = models.CharField(max_length=264)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="get_patient_related_columns")

    def __str__(self):
        return f"Column: {self.name} Patient: {self.patient.name} "

class Cell(models.Model):
    value = models.CharField(max_length=4000)
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name="get_columns_related_cells")

    def __str__(self):
        return f"Cell of Column: {self.column.name} of Patient: {self.column.patient.name}"