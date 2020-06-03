from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    r2 = models.ManyToManyField("home.Test", blank=True, related_name="customtext_r2",)
    r3 = models.ManyToManyField("users.User", blank=True, related_name="customtext_r3",)
    r4 = models.ManyToManyField(
        "home.HomePage", blank=True, related_name="customtext_r4",
    )
    r5 = models.BigIntegerField(null=True, blank=True,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Test(models.Model):
    "Generated Model"
    hjgjh = models.BigIntegerField()


class R2(models.Model):
    "Generated Model"
    r2 = models.BigIntegerField()


class R1(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()


class R4(models.Model):
    "Generated Model"
    r4 = models.BigIntegerField()


class R3(models.Model):
    "Generated Model"
    r3 = models.BigIntegerField()
