from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Email not provided")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault("is_active", True)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        if kwargs.get("is_active") is not True:
            raise ValueError("Superuser should be active")
        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser should be staff")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser should have is_superuser=True")
        return self.create_user(email, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):  # type:ignore
    email = models.EmailField(max_length=255, unique=True)  # type:ignore
    first_name = models.CharField(max_length=255)  # type:ignore
    last_name = models.CharField(max_length=255)  # type:ignore
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # type:ignore
    date_joined = models.DateTimeField(auto_now_add=True)  # type:ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()
