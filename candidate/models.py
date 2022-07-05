from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_countries.fields import CountryField


# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, phone, role, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            phone=phone,
            role=role,
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, phone, role, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """

        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            phone=phone,
            role=role,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,

    )
    date_of_birth = models.DateField()
    options = (("employer", "employer"),
               ("candidate", "candidate"))
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=12, choices=options, default="candidate")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'phone', 'role']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class company_Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='employer', null=True)
    Company_logo = models.ImageField(upload_to="images")
    Company_name = models.CharField(max_length=100)
    Services = models.CharField(max_length=200)
    Company_start_date = models.DateField(null=True)
    Websites = models.CharField(max_length=100)


#
class jobs(models.Model):
    Company_name = models.ForeignKey(company_Profile, on_delete=models.CASCADE, null=True)
    Job_details = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Experience = models.PositiveIntegerField(default=1)
    Salary = models.PositiveIntegerField(default=15000)
    Skills = models.CharField(max_length=200, null=True)


class Candidateprofile(models.Model):
    category = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('Other', 'other'),
    )
    photo = models.FileField(null=True)
    name = models.CharField(max_length=200)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=200, null=True, choices=category, default="male")
    mobile = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    resume = models.FileField(null=True, upload_to='resumes')


# class application(models.Model):
#     user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='candiate')
#     job = models.CharField(max_length=200)
#     submitted_date = models.DateField(null=True)
#     options = (
#         ('Accepted', 'Accepted'),
#         ('Rejected', 'Rejected')
#     )
#     status = models.CharField(max_length=120, choices=options)

class Application(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone_number = models.PositiveIntegerField()
    location = models.CharField(max_length=255, null=True)
    grad_year = models.IntegerField(blank=True)
    postion_for_which_you_applying = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes', null=True)


# class my_application(models.Model):
#     user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
#     job = models.ForeignKey(jobs, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True)
#     address = models.CharField(max_length=250)
#     option = {
#         ("order_placed", "order_placed"),
#         ("Dispatched", "Dispatched"),
#         ("cancel", "cancel"),
#         ("Intransit", "Intransit"),
#         ("delivered", "delivered"),
#
#     }
#     status = models.CharField(max_length=120, choices=option, default="order_placed")
#     excepted_delivery_date = models.DateField(null=True)
