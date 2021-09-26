# Generated by Django 3.2.7 on 2021-09-15 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Ism')),
                ('last_name', models.CharField(max_length=50, verbose_name='Familiya')),
                ('middle_name', models.CharField(max_length=50, verbose_name='Otasini ismi')),
                ('subject', models.CharField(max_length=50, verbose_name='Fan')),
                ('title', models.CharField(max_length=100, verbose_name='Sarlavha')),
                ('context', models.TextField(verbose_name='Kontekst')),
                ('photo', models.ImageField(upload_to='media/', verbose_name='Surat')),
            ],
        ),
        migrations.CreateModel(
            name='CourseRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Ism')),
                ('last_name', models.CharField(max_length=50, verbose_name='Familiya')),
                ('middle_name', models.CharField(max_length=50, verbose_name='Otasini ismi')),
                ('phone', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Telefon raqam')),
                ('email', models.EmailField(max_length=254, verbose_name="Elektron po'chka")),
            ],
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/', verbose_name='Surat')),
                ('person_name', models.CharField(max_length=50, verbose_name='Trener')),
                ('title', models.CharField(max_length=100, verbose_name='Savloha')),
                ('date_time', models.DateTimeField(verbose_name='Sana')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Ism')),
                ('last_name', models.CharField(max_length=50, verbose_name='Familiya')),
                ('middle_name', models.CharField(max_length=50, verbose_name='Otasini ismi')),
                ('phone', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Telefon raqam')),
                ('email', models.EmailField(max_length=254, verbose_name="Elektron po'chta")),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Kurs nomi')),
                ('image', models.ImageField(upload_to='', verbose_name='Rasm')),
                ('title', models.CharField(max_length=100, verbose_name='Savlaha')),
                ('context', models.TextField(verbose_name='Text')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='About_teacher', to='api.aboutteacher')),
            ],
        ),
    ]