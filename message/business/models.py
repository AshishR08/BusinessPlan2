from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from uuid import uuid4
from django.conf import settings
from django_resized import ResizedImageField

import os

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    phoneNumber = models.CharField(null=True,blank=True,max_length=100)
    phoneId = models.CharField(null=True, blank=True, max_length=200)

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, unique=True, max_length=100)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]


        self.last_updated = timezone.localtime(timezone.now())
        super(Profile, self).save(*args, **kwargs)



class BusinessPlan(models.Model):
    profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    company_description = models.TextField(null=True, blank=True)
    market_analysis = models.TextField(null=True, blank=True)
    swot_analysis = models.TextField(null=True, blank=True)
    product_detail = models.TextField(null=True, blank=True)
    marketing_strategy = models.TextField(null=True, blank=True)
    

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, unique=True, max_length=100)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]


        self.last_updated = timezone.localtime(timezone.now())
        super(BusinessPlan, self).save(*args, **kwargs)




class ChatSession(models.Model):
    
    OPTIONS = [
        ('(Pty Ltd)','(Pty Ltd)'),
        ('Not Profit','Not Profit'),
        ('Partnership','Partnership'),
    ]

    business_name = models.TextField(null=True, blank=True)
    business_type = models.CharField(choices = OPTIONS, null=True, blank=True, max_length=100)
    country = models.TextField(null=True, blank=True)
    product_service = models.TextField(null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    years = models.IntegerField(null=True, blank=True)
    progress = models.TextField(null=True, blank=True)

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


    uniqueId = models.CharField(null=True, blank=True, unique=True, max_length=100)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]


        self.last_updated = timezone.localtime(timezone.now())
        super(ChatSession, self).save(*args, **kwargs)