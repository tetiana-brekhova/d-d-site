import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):

    class Meta:
        permissions = [
            ("view_customuser", "Can view CustomUser"),
        ]

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser):

    user_name = models.CharField(max_length=20, default=None, null=True)
    email = models.CharField(max_length=100, unique=True, default=None)
    password = models.CharField(default=None, max_length=255)
    is_active = models.BooleanField(default=True)
    id = models.AutoField(primary_key=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return f"'id': {self.id}, 'user_name': '{self.user_name}', 'email': '{self.email}'"

    def __repr__(self):
        return f"{CustomUser.__name__}(id={self.id})"

    @staticmethod
    def get_by_id(user_id):
        custom_user = CustomUser.objects.filter(id=user_id).first()
        return custom_user if custom_user else None

    @staticmethod
    def get_by_email(email):
        custom_user = CustomUser.objects.filter(email=email).first()
        return custom_user if custom_user else None

    @staticmethod
    def delete_by_id(user_id):
        user_to_delete = CustomUser.objects.filter(id=user_id).first()
        if user_to_delete:
            CustomUser.objects.filter(id=user_id).delete()
            return True
        return False

    @staticmethod
    def create(email, password, user_name=None):
        if len(user_name) >= 0 and len(email) <= 100 and len(email.split('@')) == 2 and len(CustomUser.objects.filter(email=email)) == 0:
            custom_user = CustomUser(email=email, password=password, user_name=user_name)
            custom_user.save()
            return custom_user
        return None

    def to_dict(self):
        return {'id': self.id,
                'user_name': f'{self.user_name}',
                'email': f'{self.email}',
                'is_active': self.is_active}


    @staticmethod
    def get_all():
        return CustomUser.objects.all()


    def has_module_perms(self, app_label):
        if self.is_active and self.role == 1:
            return True

    def has_perm(self, perm):
        if self.is_active and self.role == 1:
            return True
