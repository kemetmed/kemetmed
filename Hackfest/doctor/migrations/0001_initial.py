# Generated by Django 3.2.8 on 2022-01-15 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('healthcare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicineId', models.AutoField(primary_key=True, serialize=False)),
                ('medicineName', models.CharField(max_length=25)),
                ('singleUnitQuantity', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prescriptionId', models.AutoField(primary_key=True, serialize=False)),
                ('prescriptionPatient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='healthcare.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PrescribedMedicine',
            fields=[
                ('prescribedMedicineId', models.AutoField(primary_key=True, serialize=False)),
                ('prescribedMedicineDuration', models.CharField(max_length=11)),
                ('prescribedMedicineQuantity', models.CharField(max_length=11)),
                ('prescribedMedicineTakenQuantity', models.CharField(max_length=11)),
                ('prescribedMedicineInstructions', models.TextField(max_length=50)),
                ('prescribedMedicineDiagnosis', models.TextField(max_length=50)),
                ('prescribedMedicineMedicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.medicine')),
                ('prescribedMedicinePrescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.prescription')),
            ],
        ),
    ]
