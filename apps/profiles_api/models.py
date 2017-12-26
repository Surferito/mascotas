from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserProfileManager(BaseUserManager):
    ''' Helps django work with out custom user model '''

    def create_user(self, email, password=None):
        ''' creates a new user profile object '''

        if not email:  # if email== none or false
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)  # pone el email en minusculas entero
        user = self.model(email=email,)  # crea un objeto usuario

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        ''' creates a new superuser '''

        user = self.create_user(email, password)  # crea un objeto usuario

        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    ''' Represents a user profile inside our system '''

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # esta variable permite al usuario logearse con su email
    USERNAME_FIELD = 'email'


    def get_full_name(self):
        ''' Use to get a users full name '''

        return self.name

    def get_short_name(self):
        ''' Use to get a users short name '''

        return self.name

    def __str__(self):
        ''' Django uses this to convert the object to a string '''

        return self.email

class ProfileFeedItem(models.Model):
    """ Profile status update """
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text