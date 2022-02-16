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

    # We add this function in class, since in DB product name is display as ( product_object n )
    # So by doing this it will replace name ( product_object n --> product_name give in DB )



# To save changes done in models use command --> python manage.py makemigrations
# Changes are get stored in migration  folder of app --> shop

# To apply changes use command --> python manage.py migrate