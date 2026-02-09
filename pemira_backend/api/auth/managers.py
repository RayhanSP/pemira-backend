from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(
            self,
            email,
            password,
    ):
        user = self.model(email=self.normalize_email(email.lower()) or None)
        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password
        )

        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user