from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    phone = models.CharField(max_length=255,unique=True)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']

class NextOfKin(Person):
    pass

class Patient(Person):
    first_visit = models.DateField(auto_now=True)
    next_of_kin = models.OneToOneField(NextOfKin,
                                         on_delete=models.CASCADE, 
                                         null=True,
                                         blank=True)