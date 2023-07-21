# Generated by Django 4.2.3 on 2023-07-18 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('ciclo', models.CharField(max_length=20)),
                ('paralelo', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('facultad', models.CharField(choices=[('agropecuaria', 'Agropecuaria y de Recursos Naturales Renovables'), ('educación', 'Educación, el Arte y la Comunicación'), ('energía', 'Energía, las Industrias y los Recursos Naturales no Renovables'), ('jurídica', 'Jurídica, Social y Administrativa'), ('salud', 'Salud Humana'), ('distancia', 'Unidad de Educación a Distancia y en Línea')], max_length=30)),
                ('inicio_periodo', models.DateField()),
                ('final_periodo', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(choices=[('decano', 'Decano'), ('docente', 'Docente'), ('estudiante', 'Estudiante'), ('director', 'Director')], max_length=20)),
                ('cedula', models.CharField(max_length=20)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroActividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tutoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField()),
                ('tema', models.CharField(max_length=60)),
                ('modalidad', models.CharField(choices=[('presencial', 'Presencial'), ('virtual', 'Virtual')], max_length=20)),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_tutorias.asignatura')),
                ('docente', models.ForeignKey(limit_choices_to={'cargo': 'docente'}, on_delete=django.db.models.deletion.CASCADE, to='sistema_tutorias.persona')),
            ],
        ),
        migrations.AddField(
            model_name='asignatura',
            name='carrera',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sistema_tutorias.carrera'),
        ),
    ]
