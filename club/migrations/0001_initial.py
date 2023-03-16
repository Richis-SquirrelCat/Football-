# Generated by Django 4.1.3 on 2023-03-14 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cost', models.CharField(max_length=255)),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('emblem', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='FormView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('footnote', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
                ('foto', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('banner', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('foto', models.ImageField(upload_to='')),
                ('name_surname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('who', models.CharField(max_length=255)),
                ('game', models.IntegerField()),
                ('start', models.IntegerField()),
                ('sub_off', models.CharField(max_length=255)),
                ('time_in_played', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Statistica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('club1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='club.club')),
                ('club2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='club.club')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.news')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.CharField(max_length=255)),
                ('time', models.TimeField()),
                ('club1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='t1', to='club.club')),
                ('club2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='t2', to='club.club')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(upload_to='')),
                ('date', models.DateField()),
                ('account', models.CharField(max_length=255)),
                ('club1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teammates1', to='club.club')),
                ('club2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teammates2', to='club.club')),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.schedule')),
            ],
        ),
    ]
