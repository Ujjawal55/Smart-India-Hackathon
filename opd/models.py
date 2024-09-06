from django.db import models
from django.contrib.auth.models import User
import uuid


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="doctor")
    username = models.CharField("Username", max_length=200)
    name = models.CharField("Full Name", max_length=200)
    email = models.EmailField("Email", max_length=190)
    profile_image = models.ImageField(
        "Image",
        upload_to="profile/",
        default="profile/default-profile.png",
    )
    speciality = models.CharField("Speciality", max_length=200, blank=True)
    phone_number = models.CharField("Phone Number", max_length=10, blank=True)
    street_address = models.CharField("Street Address", max_length=255, blank=True)
    city = models.CharField("City", max_length=255, blank=True)
    experience = models.IntegerField("Year of Experience", default=0)
    about = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        self.name = self.name.upper()
        self.speciality = self.speciality.capitalize()

        super().save(*args, **kwargs)


class Product(models.Model):
    owner = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=255)
    category = models.CharField("Category", max_length=255)
    stock = models.IntegerField("Stock", default=0)
    price = models.IntegerField("Price", default=0)

    def __str__(self):
        return str(self.name.capitalize())

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        self.category = self.category.capitalize()
        super().save(*args, **kwargs)
