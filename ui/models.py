from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100, default='#', blank=True)
    image = models.ImageField(default='default.jpg', upload_to='project_images')
    technology = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title} - {self.technology}'


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.subject}'


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.percentage}%'


class Service(models.Model):
    icon = models.CharField(max_length=100, default='fa fa-', blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.icon}'
