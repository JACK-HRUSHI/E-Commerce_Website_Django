from django.db import models

# Refer Model Field Reference Django for more info about RHS of below.

#  Do changes in MAIN PROJECT --> SETTINGS.PY --> INSTALLED_APPS[] --> Replace 'shop' with 'shop.apps.ShopConfig'

class Product(models.Model):
    product_id = models.AutoField # It Automatically Increments Count
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="") # Need to write default as we adding this in existing DB
    subcategory = models.CharField(max_length=50, default="") # Need to write default as we adding this in existing DB
    price = models.IntegerField(default=0) # Need to write default as we adding this in existing DB
    desc = models.CharField(max_length=300)
    pub_date = models.DateField(null=True)
    image = models.ImageField(upload_to="shop/images", default="") # Need to write default as we adding this in existing DB

    def __str__(self):

        return self.product_name
        return self.price

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):

        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    add = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True) # By using this it will assigned current time in timestamp variable

    def __str__(self):

        return self.update_desc[0:7] + "..."