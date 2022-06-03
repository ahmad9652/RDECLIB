from django.db import models
from django.template import Library
from executing import Source

# Create your models here.
class AddBook(models.Model):
    Date = models.DateField(auto_now_add=True)
    Accession_Number = models.AutoField(primary_key=True)
    Author = models.CharField(max_length=400)
    Title = models.CharField(max_length=500)
    Volume = models.IntegerField(blank=True,null=True)
    Place = models.CharField(max_length=500)
    Publisher = models.CharField(max_length=400)
    Year_Of_Publication = models.IntegerField(blank=True,null=True)
    Source = models.CharField(max_length=400,blank=True,null=True)
    Pages = models.IntegerField(blank=True,null=True)
    Book_Number = models.IntegerField()
    Bill_Number = models.IntegerField(blank=True,null=True)
    Bill_Date = models.DateField(blank=True,null=True)
    Withdrawn_Date = models.DateField(blank=True,null=True)
    Remark = models.CharField(max_length=1000,blank=True,null=True)
    class_No = models.IntegerField(blank=True,null=True)
    Category=models.CharField(max_length=100,default=" ")

# class AddStudent(models.Model):
#     First_Name = models.CharField(max_length=100)
#     Last_Name = models.CharField(max_length=100)
#     Fathers_Name = models.CharField(max_length=100)
#     Address = models.CharField(max_length=500)
#     Roll_Number = models.BigIntegerField()
#     Year = models.IntegerField(default=0)
#     Branch=models.CharField(max_length=50)
#     Phone_Number=models.BigIntegerField()
#     Joining_Date=models.DateField()
#     Expiring_Date=models.DateField()
#     Library_ID = models.BigIntegerField()
#     Issued_Book_No=models.BigIntegerField()



