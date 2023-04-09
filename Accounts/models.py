from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address')
        elif not username:
            raise ValueError('Users must have a valid username')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if not kwargs.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not kwargs.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **kwargs)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, blank=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=10, blank=True)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    def name(self):
        return self.username


    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True
        return False

    def has_module_perms(self, app_label):
        if self.is_active and self.is_superuser:
            return True
        return False

    def __str__(self):
        return f"username: {self.username}\nmail: {self.email}\nphone: {self.phone_number}\n"

# Create your models here.


