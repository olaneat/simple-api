
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, user, password=None):
        if not email:
            raise ValueError('email is necessary')
        user = self.model(email=self.normalize_email('email'))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, emai, password):
        if password is None:
            raise TypeError('password is necessary')
        
        user = self.create_user(email, password)
        user_is_superuser =True
        user.is_staff = True
        user.save()

        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = [] 

    def __str__(self):
        return self.email
    
    
    objects = UserManager()

    
    

