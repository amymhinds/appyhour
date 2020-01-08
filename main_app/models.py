from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls import reverse

SEX = (
    ('P','Prefer not to say'),
    ('F', 'Female'),
    ('M', 'Male'),
    ('NB','Non-Binary')  
)

INTERESTS = (
    ('1','Anything that eats'),
    ('2','Men'),
    ('3','Women'),
    ('4','Men and Women'),
    ('5','Non-Binary')
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
        choices=INTERESTS,
        default=INTERESTS[0]
    )

    
