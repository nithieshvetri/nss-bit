import os
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.core.validators import FileExtensionValidator
import datetime

year_choices=[(r,r) for r in range(2015, 2065)]

def file_path1(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/Home",filename)

def file_path2(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/Services",filename)

def file_path3(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/POs",filename)

def file_path4(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/PMY",filename)

def file_path5(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/DL",filename)

def file_path6(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/NLM",filename)

def file_path7(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/SBM",filename)

def file_path8(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/UBA",filename)

def file_path9(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/Awards",filename)

def file_path10(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/VolunteerTalent",filename)

def file_path11(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/Sapling",filename)

def file_path12(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/BDC",filename)

def file_path13(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/Seminars",filename)

def file_path14(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("pdfs/Reports",filename)

def file_path15(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("pdfs/ActivityCalendar",filename)

def file_path16(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("pdfs/Assets",filename)

def file_path17(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/structure",filename)

def file_path18(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("images/Others",filename)

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError("Users must have an email address")
        email = email.lower()
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

class Home(models.Model):
    """Model for creating image slider in homepage"""
    class Meta:
        verbose_name_plural = "Home"
        ordering = ['S_No']

    S_No = models.IntegerField(unique=True, default=None,null=True,blank=True, verbose_name="S.No.")
    event = models.CharField(max_length=255, default=None, null=True,blank=True, verbose_name="Event Name")
    image = models.ImageField(null=True, upload_to=file_path1,
                                verbose_name="Home Slider")

    def __str__(self):
        return self.event

class Services(models.Model):
    """Model for creating slider of services in homepage"""
    class Meta:
        verbose_name_plural = "Services"
        ordering = ['S_No']

    S_No = models.IntegerField(unique=True, default=None, blank=True, null=True, verbose_name="S.No.")
    event = models.CharField(max_length=255, default=None, blank=True, null=True, verbose_name="Event Name")
    image = models.ImageField(null=True, upload_to=file_path2, 
                                verbose_name= "Services Slider")

    def __str__(self):
        return self.event

class UpcomingEvent(models.Model):
    """Model for updating upcoming events"""

    class Meta:
        verbose_name_plural = "Upcoming Events"

    event = models.CharField(max_length=255, default=None, verbose_name="Event Name")
    date = models.CharField(max_length=255, default=None, verbose_name="Event Data & Time")

    def __str__(self):
        return self.event

class Structure(models.Model):
    """Model for creating slider of services in homepage"""
    class Meta:
        verbose_name_plural = "NSS Structure (Upload only two images)"

    image = models.ImageField(null=True, upload_to=file_path17, 
                                verbose_name= "Structure Image(For update , replace this image only)")

    def __str__(self):
        return "Image Structure"

class POs(models.Model):
    """Model for updating Programme Officers"""

    class Meta:
        verbose_name_plural = "Programme Officers"
        ordering = ['S_No']
    
    S_No = models.IntegerField(unique=True, default=None, null=True, verbose_name="S.No.")
    name = models.CharField(max_length=255, default=None, verbose_name="Name")
    position = models.CharField(max_length=255, default=None, verbose_name="Position")
    photo = models.ImageField(null=True, upload_to=file_path3, 
                                validators=[FileExtensionValidator(allowed_extensions=['jpeg','jpg'])],
                                verbose_name="Photo")

    def __str__(self):
        return self.name

class AC(models.Model):
    """Model for updating Advisory Committee Members"""
    class Meta:
        verbose_name_plural = "Advisory Committee"
        ordering = ['S_No']

    S_No = models.IntegerField(unique=True, default=None, null=True, verbose_name="S.No.")
    name = models.CharField(max_length=255, default=None, verbose_name="Name")
    position = models.CharField(max_length=255, default=None, verbose_name="Position")

    def __str__(self):
        return self.name

class PMY(models.Model):
    """Model for updating pradhan mantri yojana"""
    class Meta:
        verbose_name_plural = "Pradhan Mantri Yojana (PMY)"

    title = models.CharField(max_length=255, default=None, verbose_name="Scheme Title ")
    Objective = models.TextField(max_length=500, null=True, default=None, verbose_name="Objective")
    link = models.CharField(max_length=500, default=None,null=True, verbose_name="Read More Link") 
    image = models.ImageField(null=True, upload_to=file_path4, 
                                verbose_name= "Scheme Image")

    def __str__(self):
        return self.title


# class DL(models.Model):
#     """Model for updating Digital Literacy"""
#     class Meta:
#         verbose_name_plural = "Digital Literacy"

#     title = models.CharField(max_length=255, default=None, verbose_name="Scheme Title ")
#     image1 = models.ImageField(null=True,blank=True, upload_to=file_path5,
#                                 verbose_name= "Image 1")
#     date1 = models.CharField(max_length=255, default=None, verbose_name="Date")
#     image2 = models.ImageField(null=True, blank=True,upload_to=file_path5,
#                                 verbose_name= "Image 2")
#     date2 = models.CharField(max_length=255, default=None, verbose_name="Date")
#     image3 = models.ImageField(null=True, blank=True, upload_to=file_path5,
#                                 verbose_name= "Image 3")
#     date3 = models.CharField(max_length=255, default=None, verbose_name="Date")
#     image4 = models.ImageField(null=True, blank=True, upload_to=file_path5,
#                                 verbose_name= "Image 4")
#     date4 = models.CharField(max_length=255, default=None, verbose_name="Date")
#     video = models.URLField(max_length=500, blank=True, default=None,null=True, verbose_name="Video URL") 
#     place = models.CharField(max_length=255, default=None, verbose_name="Place")

#     def __str__(self):
#         return self.title


class NLM(models.Model):
    """Model for updating National Literacy Mission"""
    class Meta:
        verbose_name_plural = "National Literacy Mission"
        ordering = ['-pk']

    event = models.CharField(max_length=255, default=None, verbose_name="Event Title")
    date = models.CharField(max_length=255, default=None, verbose_name="Date & Year ")
    place = models.CharField(max_length=255, default=None, verbose_name="Place")
    image1 = models.ImageField(null=True,blank=True, upload_to=file_path6,
                                verbose_name= "Image 1")
    image2 = models.ImageField(null=True, blank=True,upload_to=file_path6,
                                verbose_name= "Image 2")
    image3 = models.ImageField(null=True,blank=True, upload_to=file_path6,
                                verbose_name= "Image 3")
    image4 = models.ImageField(null=True, blank=True,upload_to=file_path6,
                                verbose_name= "Image 4")
    video = models.URLField(max_length=500, default=None,null=True,blank=True, verbose_name="Video URL") 
    

    def __str__(self):
        return self.date

# class SBM(models.Model):
#     """Model for updating Swachh Bharath Mission"""
#     class Meta:
#         verbose_name_plural = "Swachh Bharath Mission"

#     date = models.CharField(max_length=255, default=None, verbose_name=" Year ")
#     image1 = models.ImageField(null=True, blank=True, upload_to=file_path7,
#                                 verbose_name= "Image 1")
#     image2 = models.ImageField(null=True, blank=True, upload_to=file_path7,
#                                 verbose_name= "Image 2")
#     image3 = models.ImageField(null=True, blank=True, upload_to=file_path7,
#                                 verbose_name= "Image 3")
#     image4 = models.ImageField(null=True, blank=True, upload_to=file_path7,
#                                 verbose_name= "Image 4")
#     place = models.CharField(max_length=255, default=None, verbose_name="Place")
#     video = models.URLField(max_length=500, default=None,null=True, verbose_name="Video URL")

#     def __str__(self):
#         return self.date

class UBA(models.Model):
    """Model for updating Unnat Bharat Abhiyan(UBA)"""
    class Meta:
        verbose_name_plural = "Unnat Bharat Abhiyan(UBA)"
        ordering = ['-pk']

    event = models.CharField(max_length=255, default=None, verbose_name="Event Name ")
    date = models.CharField(max_length=255, default=None, verbose_name=" Year ")
    place = models.CharField(max_length=255, default=None, verbose_name="Place")
    description = models.TextField(max_length=500, null=True, default=None, verbose_name="Description")
    image1 = models.ImageField(null=True, blank=True,upload_to=file_path8,
                                verbose_name= "Image 1")
    image2 = models.ImageField(null=True, blank=True, upload_to=file_path8,
                                verbose_name= "Image 2")
    image3 = models.ImageField(null=True, blank=True,upload_to=file_path8,
                                verbose_name= "Image 3")
    image4 = models.ImageField(null=True, blank=True,upload_to=file_path8,
                                verbose_name= "Image 4")
    video = models.URLField(max_length=500, blank=True,default=None,null=True, verbose_name="Youtube URL")

 
    def __str__(self):
        return self.event

class Awards(models.Model):
    """Model for updating Awards & Achievements"""
    class Meta:
        verbose_name_plural = "Awards & Achievements"
        ordering = ['-pk']

    date = models.CharField(max_length=255, default=None, verbose_name=" Year ")
    description = models.TextField(max_length=500, null=True, default=None, verbose_name="Description")
    image = models.ImageField(null=True, blank=True, upload_to=file_path9,
                                verbose_name= "Image")
    def __str__(self):
        return self.description

choice = (
        ('Report', 'Report'),
        ('Magazine', 'Magazine'),
    )

class Reports(models.Model):
    """Model for updating Reports and Magazines"""
    class Meta:
        verbose_name_plural = "Reports & Magazines"
        ordering = ['pk']

    type = models.CharField(max_length=255, choices = choice, default=None, verbose_name=" type ")
    year = models.CharField(max_length=255, default=None, verbose_name=" Year ")
    file = models.FileField(null=True,upload_to=file_path14,
                    validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                    verbose_name="PDF File")
    
    def __str__(self):
        return self.year

class ActivityCalendar(models.Model):
    """Model for uploading Activity Calendar"""
    class Meta:
        verbose_name_plural = "Activity Calendar"
        ordering = ['-pk']

    year = models.CharField(max_length=255, default=None, verbose_name=" Year ")
    pdf1 = models.FileField(null=True,upload_to=file_path15,
                    validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                    verbose_name="PDF File")
    
    def __str__(self):
        return self.year

class Assets(models.Model):
    """Model for uploading Assets document"""
    class Meta:
        verbose_name_plural = "Assets Created (Upload only one document)"

    file = models.FileField(null=True,upload_to=file_path16,
                    validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                    verbose_name="PDF File")
    
    def __str__(self):
        return "Assets(Edit this only)"

class VT(models.Model):
    """Model for uploading Volunteer's Talent"""
    class Meta:
        verbose_name_plural = "Volunteers Talent"
        ordering = ['-pk']

    name = models.CharField(max_length=255, default=None, verbose_name="Name ")
    skill = models.CharField(max_length=255, default=None, verbose_name="Skill ")
    file = models.FileField(null=True, upload_to=file_path10,
                    validators=[FileExtensionValidator(allowed_extensions=['mp4', 'jpg'])],
                    verbose_name="Video or Image")
    image1 = models.ImageField(null=True, blank=True, upload_to=file_path10,
                                verbose_name= "Image 1")
    image2 = models.ImageField(null=True, blank=True, upload_to=file_path10,
                                verbose_name= "Image 2")
 
    def __str__(self):
        return self.name

class Sapling(models.Model):
    """Model for updating Sapling Plantation events"""
    class Meta:
        verbose_name_plural = "Sapling Plantation"

    event = models.CharField(max_length=255, default=None, verbose_name="Event Name ")
    count = models.CharField(max_length=255, default=None, verbose_name=" Sapling Count ")
    About = models.TextField(max_length=500, null=True, default=None, verbose_name="Event Description")
    year = models.CharField(max_length=255, default=None, verbose_name=" Year ")
    image1 = models.ImageField(null=True, upload_to=file_path11,
                                verbose_name= "Image 1")

 
    def __str__(self):
        return self.event


class BDC(models.Model):
    """Model for uploading Blood Donation Camps"""
    class Meta:
        verbose_name_plural = "Blood Donation Camp (BDC)"
        ordering = ['-pk']

    date = models.CharField(max_length=255, default=None, verbose_name="Event Date ")
    donated_to = models.CharField(max_length=255, default=None, verbose_name=" Donated to ")
    count = models.IntegerField(verbose_name="Units")
    photo = models.ImageField(null=True, upload_to=file_path12,
                                verbose_name= "Image")

 
    def __str__(self):
        return self.date

class Camp(models.Model):
    """Model for uploading camps"""
    class Meta:
        verbose_name_plural = "Camp Organised"
        ordering = ['-pk']

    date = models.CharField(max_length=255, default=None, verbose_name="Event Date ")
    description = models.TextField(max_length=500, null=True, default=None, verbose_name="Description")
    video = models.URLField(max_length=500, default=None,null=True, verbose_name="Video URL")
 
    def __str__(self):
        return self.date

class Seminar(models.Model):
    """Model for uploading seminars and conferences"""
    class Meta:
        verbose_name_plural = "Seminars & Conferences"
        ordering = ['-pk']

    date = models.CharField(max_length=255, default=None, verbose_name="Event Date ")
    description = models.TextField(max_length=500, null=True, default=None, verbose_name="Description")
    photo = models.ImageField(null=True, blank=True, upload_to=file_path13,
                                verbose_name= "Image")

 
    def __str__(self):
        return self.date

class Others(models.Model):
    """Model for updating other events(yearwise)"""
    class Meta:
        verbose_name_plural = "Events Organised (Others)"
        ordering = ['-pk']

    year = models.IntegerField(choices=year_choices, default=datetime.date.today().year, verbose_name="Year: (Note: Year you select here must be the starting year of this academic. E.g., For 2021-2022, you should select here 2021 only not 2022.")
    event = models.CharField(max_length=255, default=None, verbose_name="Event Name ")
    date = models.CharField(max_length=255, default=None, verbose_name=" Date & Time ")
    description = models.TextField(max_length=500, null=True, default=None, verbose_name="Description")
    image1 = models.ImageField(null=True, blank=True,upload_to=file_path18,
                                verbose_name= "Image 1")
    image2 = models.ImageField(null=True,blank=True, upload_to=file_path18,
                                verbose_name= "Image 2")
    image3 = models.ImageField(null=True,blank=True, upload_to=file_path18,
                                verbose_name= "Image 3")
    image4 = models.ImageField(null=True, blank=True,upload_to=file_path18,
                                verbose_name= "Image 4")
    video = models.URLField(max_length=500, blank=True,default=None,null=True, verbose_name="Youtube URL")

 
    def __str__(self):
        return self.event


class HomeUpdate(models.Model):
    """Models for stop displaying corona update and awards count"""
    class Meta:
        verbose_name_plural = "Home awards & corona warning update"

    year = models.IntegerField(choices=year_choices, default=2026, verbose_name="Select the year you wish to stop displaying corona alert in homepage:")
    awards = models.IntegerField( default= 42, verbose_name="Awards")
    
    def __str__(self):
        return "Edit this field only"
