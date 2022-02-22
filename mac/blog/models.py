from django.db import models


# Refer Model Field Reference Django for more info about RHS of below.

#  Do changes in MAIN PROJECT --> SETTINGS.PY --> INSTALLED_APPS[] --> Replace 'shop' with 'blog.apps.BlogConfig' which is a class name( BlogConfig ) from apps.py file

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    by_name = models.CharField(max_length=500, default="")
    head0 = models.CharField(max_length=500, default="")
    chead0 = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=500, default="")
    chead1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=500, default="")
    chead2 = models.CharField(max_length=5000, default="")
    pub_date = models.DateField(null=True)
    thumbnail = models.ImageField(upload_to="blog/images", default="")

    def __str__(self):

        return self.title
