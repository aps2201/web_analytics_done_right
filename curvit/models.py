from django.db import models
from django.contrib.auth import get_user_model

import uuid

# Create your models here.

class general(models.Model):
    cv_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length = 50)
    middle_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    about = models.TextField()
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "CV Main"
    def __str__(self):
        return "{0},{1}".format(self.last_name,self.first_name)

class experience(models.Model):
    exp_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.CharField(max_length = 50)
    position = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True)
    cv = models.ForeignKey('curvit.general',on_delete=models.CASCADE,related_name='exp_cv')
    class Meta:
        verbose_name_plural = "Experience"
        ordering = ['-start_date']
    def __str__(self):
        return "{0}|{1}".format(self.company,self.start_date)

class education(models.Model):
    edu_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.CharField(max_length = 50)
    degree = models.CharField(max_length = 50)
    field = models.CharField(max_length = 50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True)
    cv = models.ForeignKey('curvit.general',on_delete=models.CASCADE,related_name='edu_cv')
    class Meta:
        verbose_name_plural = "Education"
        ordering = ['-start_date']
    def __str__(self):
        return "{0} | {1}".format(self.school,self.start_date)

class certification(models.Model):
    cer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    certificate = models.CharField(max_length = 50)
    organization = models.CharField(max_length = 50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True)
    credential_id =  models.CharField(max_length = 50)
    credential_url = models.URLField()
    cv = models.ForeignKey('curvit.general',on_delete=models.CASCADE,related_name='cer_cv')
    class Meta:
        verbose_name_plural = "Certification"
        ordering = ['-start_date']
    def __str__(self):
        return "{0} | {1}".format(self.certificate,self.start_date)


class volunteering(models.Model):
    vol_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.CharField(max_length = 50)
    role = models.CharField(max_length = 50)
    cause = models.CharField(max_length = 50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True)
    cv = models.ForeignKey('curvit.general',on_delete=models.CASCADE,related_name='vol_cv')
    class Meta:
        verbose_name_plural = "Volunteering"
        ordering = ['-start_date']
    def __str__(self):
        return "{0} {1} | {2}".format(self.organization,self.role,self.start_date)
