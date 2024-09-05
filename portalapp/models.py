from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class Department(models.Model):
    code = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=200)

class collage(models.Model):
    code = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=200)

class alumniUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='portalapp_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='portalapp_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    phone_no = models.CharField(max_length=20,null=True,blank=True)
    roll_no = models.CharField(max_length=15,null=True,blank=True)
    ROLE_CHOICES = [
        ("Alumni","Alumni"),("Student","Student"),("Faculty","Faculty")
    ]
    role = models.CharField(max_length=10,choices=ROLE_CHOICES, default="Student")
    degree = models.CharField(max_length=10,null=True,blank=True)
    department = models.ForeignKey(Department,null=True,blank=True,on_delete=models.CASCADE)
    year_of_admission = models.IntegerField(null=True,blank=True)
    stream = models.CharField(max_length=100,null=True,blank=True)
    collage = models.ForeignKey(collage,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.username
    


class alumniInfo(models.Model):
    alumni = models.ForeignKey(alumniUser, on_delete=models.CASCADE)
    company = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.alumni.username}"
    

class events(models.Model):
    alumni = models.ForeignKey(alumniUser, on_delete=models.CASCADE)
    EVENT_CHOICES = [
        ("Workshop","Workshop"),("Webinar","Webinar"),("Hackthon","Hackthon"),("livesessions","Livesessions"),
    ]
    event = models.CharField(max_length=16,choices=EVENT_CHOICES, default="Workshop")
    title = models.CharField(max_length=100)
    date = models.DateTimeField(null=True, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=300, blank=True)
    location = models.CharField(max_length=112,blank=True, null=True)

    def __str__(self):
        return self.title
class job_list(models.Model):
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    user = models.ForeignKey(alumniUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=10,default=1)
    desc = models.CharField(max_length=300, blank=True)

class queries(models.Model):
    alumni = models.ForeignKey(alumniUser, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    query = models.TextField()

class successtory(models.Model):
    alumni = models.ForeignKey(alumniUser, on_delete=models.CASCADE)
    story = models.TextField()

class tech_points(models.Model):
    alumni = models.ForeignKey(alumniUser, on_delete=models.CASCADE)
    tech_point = models.CharField(max_length=200)

class innnovations(models.Model):
    alumni = models.ForeignKey(alumniUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    theme = models.CharField(max_length=50)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)