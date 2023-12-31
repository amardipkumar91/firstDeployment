from django.db import models

# Create your models here.
GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)
#Company Model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=(('IT','IT'),
                                                    ('Non IT','Non IT')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name+" "+self.address

#Employee Model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    gender = models.CharField(max_length=1,choices=GENDER)
    position = models.CharField(max_length=50,choices=(('Manager','manager'),
                                                     ('Software developer','software developer'),
                                                     ('Project Leader','project leader')))
    add_company = models.ForeignKey(Company,on_delete=models.CASCADE)