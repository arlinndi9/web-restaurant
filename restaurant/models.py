from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30,default='')
    lastname = models.CharField(max_length=30,default='')
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=255,default='')
    message = models.TextField()

    def __str__(self):
     return self.name


class table(models.Model):
    name = models.CharField(max_length=30)
    date = models.CharField(max_length=230)
    email = models.EmailField(max_length = 254)
    time = models.CharField(max_length=12,default='')
    phone = models.CharField(max_length=30,default='')
    people = models.IntegerField(default='')
    message= models.TextField(max_length=300,null=True,blank=True)


    def __str__(self):
     return self.name

class menu(models.Model):
    photo = models.ImageField(upload_to='images/')
    name=models.CharField(max_length=100)
    content=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    CATEGORY_CHOICES = (
        ('appetizers', 'Appetizers'),
        ('entrees', 'Entrees'),
        ('desserts', 'Desserts'),
    )
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES,default='')

    def __str__(self):
        return self.name
