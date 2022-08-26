from distutils.command.upload import upload
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class Login(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)


class Seller(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='seller')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class User(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Products(models.Model):
    product_name = models.CharField(max_length=200)
    product_type = models.CharField(max_length=200)
    stock = models.IntegerField()
    product_seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.ImageField(upload_to='static/images/', blank=True)

    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ''
    #     return url

    def __str__(self):
        return self.product_name

class Order(models.Model):
	customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		# for i in orderitems:
		# 	if i.product.digital == False:
		# 		shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
	order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

# class VaccinationSchedule(models.Model):
#     hospital = models.ForeignKey(Hospital, on_delete=models.DO_NOTHING)
#     date = models.DateField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()


# class Complaint(models.Model):
#     user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
#     subject = models.CharField(max_length=200)
#     complaint = models.TextField()
#     date = models.DateField()
#     reply = models.TextField(null=True, blank=True)


# class Appointment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment')
#     schedule = models.ForeignKey(VaccinationSchedule, on_delete=models.CASCADE)
#     status = models.IntegerField(default=0)
#     vaccine_name = models.ForeignKey(Vaccine, on_delete=models.DO_NOTHING, null=True, blank=True)
#     vaccinated = models.BooleanField(default=False)


# class ReportCard(models.Model):
#     patient = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     vaccine = models.ForeignKey(Vaccine, on_delete=models.DO_NOTHING)


