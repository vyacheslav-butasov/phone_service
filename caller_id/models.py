from django.db import models


class Phone_number(models.Model):
    code = models.SmallIntegerField()
    start_number = models.IntegerField()
    end_number = models.IntegerField()
    company = models.CharField(max_length=200)
    region = models.CharField(max_length=200)

    def __str__(self):
        return str(self.code)
