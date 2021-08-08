from django.db import models

# Create your models here.
class Hotels(models.Model):
    image = models.ImageField(upload_to='picturs')
    name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=13)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Menu(models.Model):
    image = models.ImageField(upload_to='menu_items')
    item_name = models.CharField(max_length=50)
    price = models.IntegerField()
    hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name
    
    # qs = Menu.objects.filter(hotel__id=1)

class CustomerRegisteration(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + self.last_name


