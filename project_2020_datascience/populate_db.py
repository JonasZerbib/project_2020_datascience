from collections import defaultdict
import csv
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'project_2020_datascience.settings')
django.setup()

from firstApp.models import Patient,  Column, Cell


WANTED_COLUMNS = ['V_CALL',	'D_CALL', 'J_CALL', 'SEQUENCE_VDJ',
                  'SEQUENCE_IMGT', 'V_SEQ_LENGTH', 'JUNCTION_LENGTH']


patient_object, created = Patient.objects.get_or_create(name="P1")

with open('P1_I1_S1_genotyped_db-pass.tab', newline='') as f:
    patient_reader = csv.DictReader(f, delimiter='\t')
    for row in patient_reader:
        #print(loading_bar(length, patient_reader.line_num ))
        for column_name in WANTED_COLUMNS:
            column_object, created = Column.objects.get_or_create(
                name=column_name, patient=patient_object)
            Cell.objects.create(value=row[column_name], column=column_object)


# for chaque dossier:
#     creer un nouveau patient

#     colunm (name , patient)

#     cell (valeur, column, patient)

