from django.db import models

# Create your models here.
# create a tblgallery
class tblgallery(models.Model):
    title=models.CharField(max_length=20,null=True)
    image=models.ImageField(upload_to="static/picture/",null=True)
    description=models.TextField(default="")
    price=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    old_price=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    rating=models.IntegerField(default=0)
    category=models.CharField(max_length=20,default="")
    def __str__(self):
        return self.title

# tbl Reservation ke liye
class tblreservation(models.Model):
    Full_Name=models.CharField(max_length=50)
    Phone=models.CharField(max_length=15 )
    email=models.EmailField()
    guests=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    special_requests=models.TextField(blank=True)
    status=models.CharField(max_length=20,default="Pending")

#tbl contact ke liye
class tblContact(models.Model):
    Full_Name=models.CharField(max_length=50)
    Phone=models.CharField(max_length=15 )
    email=models.EmailField()
    Message=models.TextField(blank=True)

#tbl reviews ke liye
class tblreview(models.Model):
    Full_Name=models.CharField(max_length=50)
    Feedback=models.TextField(blank=True)
    Image=models.ImageField(upload_to="static/picture/",null=True)

# tbl login form
class tbllogin(models.Model):
    Email=models.EmailField(max_length=100,null=True)
    password=models.CharField(max_length=15,null=True)

#tbl register form
class tblregister(models.Model):
    Full_Name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=15)
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=15,null=True )
    Image=models.ImageField(upload_to="static/picture/",null=True)
    Address=models.TextField(blank=True)