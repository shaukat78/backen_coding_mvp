from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Add related_name to resolve the clash
    groups = models.ManyToManyField(
        Permission,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',
        related_query_name='user',
    )

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        # Rename the model in the database to avoid conflicts
        db_table = 'custom_user'


class Tweet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=120)

    def __str__(self):

        return f"{self.user.email}: {self.body}"