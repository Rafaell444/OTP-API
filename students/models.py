from django.db import models


# Create your models here.
class Otp(models.Model):
    profiles = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    Input_Uri = models.CharField("Input URI", max_length=255)

    def __str__(self):
        return self.Input_Uri
