from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# Product Categories
class Collection(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name


# Users
class User(models.Model):
  customer = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)  
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  phone = models.CharField(max_length=10)
  email = models.EmailField(max_length=100)
  password = models.CharField(max_length=100)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'


# Inventory
class Product(models.Model):
  name = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=50, default=0, decimal_places=6)
  category = models.ForeignKey(Collection, on_delete=models.CASCADE, default=1)
  description = models.CharField(max_length=250, default='', blank=True, null=True)
  image = models.ImageField(upload_to='uploads/product/')

  is_sale = models.BooleanField(default=False)
  sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

  def __str__(self):
    return self.name
  
  @property
  def imageURL(self):
    try :
      url = self.image.url
    except:
      url = ''
    return url


# Customer Orders
class Order(models.Model):
  items = models.ForeignKey(Product, on_delete=models.CASCADE)
  customer = models.ForeignKey(User, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)
  date = models.DateTimeField(auto_now_add=True)
  status = models.BooleanField(default=False)

  def __str__(self):
    return str(self.id) 
  
  @property
  def get_total(self):
    total = self.product.price * self.quantity
    return total
  
  @property
  def get_cart_total(self):
    order_items = self.orderitem_set.all()
    total = sum([item.get_total for item in order_items])
    return total
  
  @property
  def get_cart_items(self):
    order_items = self.orderitem_set.all()
    total = sum([item.quantity for item in order_items])
    return total  
  

class ShippingAddress(models.Model):
  customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
  address = models.CharField(max_length=200, null=False)
  city = models.CharField(max_length=200, null=False)
  state = models.CharField(max_length=200, null=False)
  zipcode = models.CharField(max_length=200, null=False)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.address
  