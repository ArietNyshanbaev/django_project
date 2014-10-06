from django.db import models

class SignUp(models.Model):
    first_name = models.CharField(max_length = 60, blank = True, null = True)
    last_name = models.CharField(max_length = 60, blank = True, null = True)
    email = models.EmailField(null =False , blank = False)
    first_time = models.DateTimeField(auto_now_add = True, auto_now = False)
    last_time = models.DateTimeField(auto_now_add = False, auto_now = True)
    
    def __unicode__(self):
        return (self.email)
    

