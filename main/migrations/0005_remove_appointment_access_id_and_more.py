# Generated by Django 4.2 on 2023-04-28 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_patient_assigned_doctor_alter_patient_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='access_id',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_time',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='health_notes',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='phone_no',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='specialization',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='assigned_doctor',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='card_no',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='email',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='matric',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='password',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='phone_no',
        ),
    ]
