from django.db import models

class UserDetail(models.Model):
    user_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=25, verbose_name='Full Name')
    address = models.TextField()
    landmark = models.CharField(max_length=30)
    state = models.CharField(max_length=15)
    district = models.CharField(max_length=15)  
    added_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname  
