from django.db import models

class StudentDetails(models.Model):
	fullname=models.CharField(max_length=100,default="")
	contactnumber=models.CharField(max_length=15,default="")
	address=models.CharField(max_length=100,default="")
	gender=models.CharField(max_length=20,default="")
	dateofbirth=models.CharField(max_length=20,default="")
	qualification=models.CharField(max_length=10,default="")
	username=models.CharField(max_length=10,default="")
	password=models.CharField(max_length=10,default="")

class tolldetails(models.Model):
	tollnumber=models.CharField(max_length=10,default="")
	startpoint=models.CharField(max_length=10,default="")
	endpoint=models.CharField(max_length=10,default="")
	tickettype=models.CharField(max_length=10,default="")
	cost=models.CharField(max_length=10,default="")
	vehicletype=models.CharField(max_length=100,default="")
	vehiclenumber=models.CharField(max_length=15,default="")
	payment=models.CharField(max_length=10,default="")
	
class PaymentDetails(models.Model):
	vehicletype=models.CharField(max_length=100,default="")
	vehiclenumber=models.CharField(max_length=15,default="")
	payment=models.CharField(max_length=10,default="")



	
		



# Create your models here.
