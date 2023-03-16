from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=255)
    emblem = models.FileField()


class Schedule(models.Model):
    schedule = models.CharField(max_length=255)  # расписание
    club1 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='t1')
    club2 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='t2')
    time = models.TimeField()


class Main(models.Model):
    text = models.CharField(max_length=255)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)


class Media(models.Model):  # +
    media = models.FileField()
    date = models.DateField()
    club1 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='teammates1')
    club2 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='teammates2')
    account = models.CharField(max_length=255)  # счёт


class News(models.Model):  # +
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    foto = models.ImageField()
    date = models.DateField()
    banner = models.BooleanField()



class FormView(models.Model):
    foto = models.ImageField()


class Brand(models.Model):
    name = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    foto = models.ImageField()


class Statistica(models.Model):
    date = models.DateTimeField()
    club1 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='team1')
    club2 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='team2')


class Participant(models.Model):
    foto = models.ImageField()
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    who = models.CharField(max_length=255)
    game = models.IntegerField()
    start = models.IntegerField()
    sub_off = models.CharField(max_length=255)
    time_in_played = models.IntegerField()


class Opinion(models.Model):
    text = models.CharField(max_length=255)
    foto = models.ImageField()
    name_surname = models.CharField(max_length=255)


class SocialMedia(models.Model):
    web = models.URLField()


class Info(models.Model):
    logo = models.ImageField()
    footnote = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()

