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

FOOD = (
    ('A', 'American'),
    ('B', 'Breakfast'),

)
# Create your models here.


class Eater(models.Model):
    name = models.CharField(max_length=25)
    sex = models.CharField(
        max_length=18,
        choices=SEX,
        default=SEX[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interestedIn = models.CharField(
        max_length=18,
        choices=ORIENTATION,
        default=ORIENTATION[0]
    )
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(99)])


class FoodInterests(models.Model):
    topFavCuisine = models.CharField(max_length=35, null=True, blank=True)
    secFavCuisine = models.CharField(max_length=35, null=True, blank=True)
    thirdFavCuisine = models.CharField(max_length=35, null=True, blank=True)
    taste = models.CharField(
        max_length=6,
        choices=TASTE,
        default=TASTE[2]
    )
