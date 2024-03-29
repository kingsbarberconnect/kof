from django.db import models
from cloudinary.models import CloudinaryField


class FormData(models.Model):
    first_name = models.CharField(max_length=256, blank=True, null=True)
    last_name = models.CharField(max_length=256, blank=True, null=True)
    age = models.CharField(max_length=256, blank=True, null=True)
    email = models.EmailField(max_length=256, blank=True, null=True)
    phone_number = models.CharField(max_length=256, blank=True, null=True)
    state = models.CharField(max_length=256, blank=True, null=True)
    lga = models.CharField(max_length=256, blank=True, null=True)
    category = models.CharField(max_length=256, blank=True, null=True)
    shop_name = models.CharField(max_length=256, blank=True, null=True)

    dateadded = models.DateTimeField(auto_now_add=True)
    datemodified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} - {self.last_name}"


def user_upload_directory(instance, filename):
    return f'assests/{filename}'
