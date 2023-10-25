
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    
    
    def __str__(self):
        return self.email

    # def get_absolute_url(self):
    #     return "/users/%i/" % (self.pk)





















# from django.db import models

# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# #manager for our custom model 
# class UsersManager(BaseUserManager):
#     """
#         This is a manager for Account class 
#     """
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError("Users must have an Emaill address")
#         if not username :
#             raise ValueError("Users must have an Username")
#         user  = self.model(
#                 email=self.normalize_email(email),
#                 username=username,
#             )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#                 email=self.normalize_email(email),
#                 password=password,
#                 username=username,
#             )
#         user.is_admin = True
#         user.is_staff=True
#         user.is_superuser=True
#         user.save(using=self._db)
#         return user
    
    
    
#     class Users(AbstractBaseUser):
    
    
#         email = models.EmailField(verbose_name='email', max_length=60, unique=True)
#         username = models.CharField(max_length=30,unique=True)
#         date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#         last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
#         is_admin = models.BooleanField(default=False)
#         is_active = models.BooleanField(default=True)
#         is_staff  = models.BooleanField(default=False)
#         is_superuser = models.BooleanField(default=False)

#         USERNAME_FIELD = 'email'
#         REQUIRED_FIELDS = ['username']

#         # objects = MyAccountManager()
#         objects = UserManager()

#         def __str__(self):
#             return self.email

#         def has_perm(self, perm, obj=None):
#             return self.is_admin
#         def has_module_perms(self, app_label ):
#             return True