from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16, blank=True)
    address = models.CharField(max_length=255, blank=True)



# Абстрактный базовый класс
class BaseProfile(models.Model):
    phone = models.CharField(max_length=16, blank=True)
    address = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True  # Указываем, что класс является абстрактным


# Наследуемый класс пользовательского профиля
class UserProfile(BaseProfile):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"{self.user}'s profile"




