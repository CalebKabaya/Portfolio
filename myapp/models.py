
from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Home(models.Model):
    aboutme=models.TextField(max_length=600, blank=True)
    title=models.CharField(max_length=60, blank=True)
    email=models.CharField(max_length=60, blank=True)
    location=models.CharField(max_length=60, blank=True)
    image=CloudinaryField('image',blank=True)



    def __str__(self):
        return f'{self.title}'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()
class About(models.Model):
    aboutme=models.TextField(max_length=600, blank=True)
    image=CloudinaryField('image',blank=True)



    def __str__(self):
        return f'{self.aboutme}'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()

class Skills(models.Model):
    skill1=models.CharField(max_length=300, blank=True)
    percentage=models.CharField(max_length=100, blank=True)

  

    def __str__(self):
        return f'{self.skill1}'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()

class AllSkills(models.Model):
    skill1=models.CharField(max_length=300, blank=True)
    percentage=models.CharField(max_length=100, blank=True)

  

    def __str__(self):
        return f'{self.skill1}'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()        

class Experience(models.Model):
    time=(
        ('months', 'months'),
        ('year', 'year'),
    )
    title=models.CharField(max_length=300, blank=True)
    duration=models.CharField(max_length=100, blank=True)
    how_many_months_or_years=models.IntegerField(blank=True,null=True)
    month_or_year=models.CharField(choices=time, blank=True,max_length=100)
    description=models.TextField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.title}'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()

class Education(models.Model):
    title=models.CharField(max_length=300, blank=True)
    duration=models.CharField(max_length=100, blank=True)
    total_years=models.CharField(max_length=50, blank=True)
    description=models.TextField(max_length=300, blank=True)
    year_month=models.CharField(max_length=50, blank=True)


    def __str__(self):
        return f'{self.title}'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()

class Services(models.Model):
    service_title=models.CharField(max_length=300, blank=True)
    service_description=models.TextField(max_length=300, blank=True)
    logo=CloudinaryField('image',blank=True)


    def __str__(self):
        return f'{self.service_title}'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()


class Projects(models.Model):
    image=CloudinaryField('image', blank=True)
    title=models.CharField(max_length=50, blank=True)
    description=models.TextField(max_length=500, blank=True)
    user_story=models.TextField(max_length=500, blank=True)


    technologies=models.CharField(max_length=40, blank=True)
    link=models.URLField(blank=True)


    def __str__(self):
        return f'{self.title}'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()  
         
class Testimonials(models.Model):
    image=CloudinaryField('image')
    testimonial=models.TextField(max_length=500, blank=True)
    name=models.CharField(max_length=50, blank=True)
    job_title=models.CharField(max_length=40, blank=True)


    def __str__(self):
        return f'{self.name}'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()  

class MyCV(models.Model):

    cv=models.FileField(upload_to='documents',blank=True)
    certificate=models.FileField(upload_to='documents',blank=True)


    def __str__(self):
        return f'{self.cv}'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def all_posts(cls):
        return cls.objects.all()  

class Address(models.Model):
    address=models.CharField(max_length=50, blank=True)
    phone=models.CharField(max_length=50, blank=True)
    email=models.CharField(max_length=50, blank=True)
  




    def __str__(self):
        return f'{self.address}'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def all_posts(cls):
        return cls.objects.all() 

class Achiev(models.Model):
    clients=models.IntegerField( blank=True)
    projects=models.IntegerField( blank=True)
    review=models.IntegerField( blank=True)
    years=models.IntegerField( blank=True)

  

    def __str__(self):
        return f'{self.clients}'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def all_posts(cls):
        return cls.objects.all() 