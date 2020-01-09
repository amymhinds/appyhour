from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

SEX = (
    ('P', 'Prefer not to say'),
    ('F', 'Female'),
    ('M', 'Male'),
    ('NB', 'Non-Binary')
)

ORIENTATION = (
    ('1', 'Anything that eats'),
    ('2', 'Men'),
    ('3', 'Women'),
    ('4', 'Men and Women'),
    ('5', 'Non-Binary')
)

TASTE = (
    ('1', 'Sweet'),
    ('2', 'Savory'),
    ('3', 'Both')
)

# Create your models here.


class Eater(models.Model):
    name = models.CharField(max_length=25)
    sex = models.CharField(
        max_length=17,
        choices=SEX,
        default=SEX[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interested_in = models.CharField(
        max_length=18,
        choices=ORIENTATION,
        default=ORIENTATION[0][0]
    )
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(99)])
    location = models.TextField(null=True, blank=True)
    top_fav_cuisine = models.CharField(max_length=35, null=True, blank=True)
    sec_fav_cuisine = models.CharField(max_length=35, null=True, blank=True)
    third_fav_cuisine = models.CharField(max_length=35, null=True, blank=True)
    least_fav_cuisine = models.CharField(max_length=35, null=True, blank=True)


class Reviews(models.Model):
    title = models.CharField(max_length=25, null=True, blank=True)
    about_my_date = models.TextField(blank=True, null=True)
    stars = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
