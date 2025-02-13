from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import timedelta


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    membership_type = models.CharField(max_length=10, choices=[('Silver', 'Silver'), ('Gold', 'Gold'), ('Diamond', 'Diamond')], blank=True, null=True)
    membership_start_date = models.DateField(null=True, blank=True)
    membership_expiry_date = models.DateField(null=True, blank=True)

    def set_membership(self, membership_type):
        self.membership_type = membership_type
        self.membership_start_date = timezone.now().date()
        if membership_type == 'Silver':
            self.membership_expiry_date = timezone.now().date() + timedelta(days=30)
        elif membership_type == 'Gold':
            self.membership_expiry_date = timezone.now().date() + timedelta(days=90)
        elif membership_type == 'Diamond':
            self.membership_expiry_date = timezone.now().date() + timedelta(days=180)
        self.save()