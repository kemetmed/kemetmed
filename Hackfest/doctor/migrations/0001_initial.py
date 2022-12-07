# Generated by Django 3.2.8 on 2022-01-16 12:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('healthcare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosisName', models.CharField(max_length=200)),
                ('diagnosisBodySite', models.CharField(max_length=100)),
                ('dateOfOnset', models.DateField()),
                ('severity', models.CharField(max_length=50)),
                ('dateOfAbatement', models.DateField()),
                ('diagnosisCertainity', models.CharField(max_length=100)),
                ('diagnosisDescription', models.TextField()),
                ('createdDate', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='LaboratoryTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testName', models.CharField(max_length=200)),
                ('testSpecimen', models.CharField(max_length=100)),
                ('testBodySite', models.CharField(max_length=200)),
                ('testUse', models.CharField(max_length=100)),
                ('testDescription', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceName', models.CharField(max_length=200)),
                ('deviceBodySite', models.CharField(max_length=200)),
                ('deviceUse', models.CharField(max_length=100)),
                ('deviceDscription', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('form', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('strength', models.CharField(max_length=100)),
                ('concentration', models.CharField(max_length=100)),
                ('unitOfPreparation', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('expiryDate', models.DateField()),
                ('amount', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicineDirection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doseUnit', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('doseTiming', models.CharField(max_length=100)),
                ('additionalInstruction', models.TextField()),
                ('reason', models.TextField()),
                ('medicineId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosisId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.diagnosis')),
                ('laboratoryTestId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.laboratorytest')),
                ('medicalDevice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.medicaldevice')),
                ('patientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.patient')),
            ],
        ),
        migrations.CreateModel(
            name='MedicineDirPrescriptionMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicineDirectionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.medicinedirection')),
                ('prescriptionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.prescription')),
            ],
        ),
    ]
