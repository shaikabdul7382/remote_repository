from django.db import models
class ContactData(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    salary = models.IntegerField()
    location = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
