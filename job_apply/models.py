from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    """
    """
    first_name = models.CharField(max_length=300, verbose_name="First Name")
    last_name = models.CharField(max_length=300, verbose_name="Last Name")
    email = models.CharField(max_length=300, verbose_name="Email")
    address = models.CharField(max_length=300, blank=True, verbose_name="Address")
    phone_number = PhoneNumberField(blank=False, unique=True)
    avatar_url = models.CharField(max_length=300, verbose_name="Avatar URL")
    cv_path = models.CharField(max_length=300, verbose_name="Cv_Path")
    message = models.TextField(max_length=300, verbose_name="Message")
    def __str__(self):
        return str(self.first_name)
    
class Experience(models.Model):
    """
    """
    user = models.ForeignKey(User, related_name='Experience_User', on_delete=models.CASCADE)
    work_experience_position = models.CharField(max_length=300, verbose_name="Work Experience Position")
    work_experience_employer = models.CharField(max_length=300, verbose_name="Work Experience Employer")
    work_experience_location = models.CharField(max_length=300, verbose_name="Work Experience Location")
    work_experience_starts = models.DateField(verbose_name="End Data")
    work_experience_ends =models.DateField(verbose_name="End Data")
    description = models.TextField(blank=True, verbose_name="Description")


class Training(models.Model):
    """
    """
    user = models.ForeignKey(User, related_name='Training_User', on_delete=models.CASCADE)
    training_institution = models.CharField(max_length=300, verbose_name="Training Institution")
    training_degree = models.CharField(max_length=300, verbose_name="Training Degree")
    training_major = models.CharField(max_length=300, verbose_name="Training Major")
    training_starts = models.DateField(verbose_name="Start Date")
    training_ends = models.DateField(verbose_name="End Data")
    description = models.TextField(blank=True, verbose_name="Description")

    def __str__(self):
        return str(self.user)

class Vacancy(models.Model):
    """
    """
    title = models.CharField(max_length=300, verbose_name="Title")
    link = models.CharField(max_length=300, verbose_name="Link")
    def __str__(self):
        return str(self.title)

class Application(models.Model):
    """
    """
    user = models.ForeignKey(User, related_name='Applyed_application', on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, related_name='Applyed_vacancy', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)
