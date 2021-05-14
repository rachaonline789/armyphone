from django.db import models

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return str(self.name)


# class tb_army_phone(models.Model):
#     army_name = models.CharField(max_length=300)
#     army_rank = models.TextField()
#     army_phone = models.ImageField(upload_to='photo',default='')
#     army_nickname = models.DateTimeField(auto_now=True,blank=False)

class tb_army_phone(models.Model):
    army_name = models.CharField(max_length=100)
    army_rank = models.CharField(max_length=100)
    army_phone = models.CharField(max_length=50)
    army_province = models.CharField(max_length=50)
    army_nickname = models.CharField(max_length=100)
    