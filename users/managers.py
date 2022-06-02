from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, reg_no, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        if not reg_no:
            raise ValueError(_('The Reg number must be set'))
        email = self.normalize_email(email)
        user = self.model(reg_no=reg_no, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, reg_no, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """

        user = self.create_user(
            reg_no,
            email,
            password=password,
            **extra_fields,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
