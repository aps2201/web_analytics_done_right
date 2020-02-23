from django.db import models

import uuid

# Create your models here.
class general(models.Model):
    cv_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length = 50)
    middle_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    about = models.TextField()
    experience = models.ForeignKey('curvit.experience',null=True,on_delete=models.CASCADE)
    education = models.ForeignKey('curvit.education',null=True,on_delete=models.CASCADE)
    certification = models.ForeignKey('curvit.certification',null=True,on_delete=models.CASCADE)
    volunteering = models.ForeignKey('curvit.volunteering',null=True,on_delete=models.CASCADE)
    

class experience(models.Model):
    exp_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.CharField(max_length = 50)
    position = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    start_date = models.DateField()
    end_date = models.DateField()
    class Meta:
        verbose_name_plural = "Experience"
        ordering = ['-start_date']

class education(models.Model):
    edu_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.CharField(max_length = 50)
    degree = models.CharField(max_length = 50)
    field = models.CharField(max_length = 50)
    start_date = models.DateField()
    end_date = models.DateField()
    class Meta:
        verbose_name_plural = "Education"
        ordering = ['-start_date']

class certification(models.Model):
    cer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    certificate = models.CharField(max_length = 50)
    organization = models.CharField(max_length = 50)
    start_date = models.DateField()
    end_date = models.DateField()
    credential_id =  models.CharField(max_length = 50)
    credential_url = models.URLField()
    class Meta:
        verbose_name_plural = "Certification"
        ordering = ['-start_date']

class volunteering(models.Model):
    vol_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.CharField(max_length = 50)
    role = models.CharField(max_length = 50)
    cause = models.CharField(max_length = 50)
    start_date = models.DateField()
    end_date = models.DateField()
    class Meta:
        verbose_name_plural = "Volunteering"
        ordering = ['-start_date']
