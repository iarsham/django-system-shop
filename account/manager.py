from django.contrib.auth.models import BaseUserManager


class CustomManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('email field must be set !')
        user = self.model(email=email, password=None, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # manage errors
        if extra_fields.get('is_active') is not True:
            raise ValueError('Super User is_active Must Be True !')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super User is_staff Must Be True !')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super User is_superuser Must Be True !')

        return self._create_user(email, password, **extra_fields)
