from django.apps import AppConfig


class SignConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sign'

    def ready(self):
        from .signals import create_or_save_profile


# Настройка приложения
class ProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile'

    def ready(self):
        pass  # Инициализация сигналов или другой логики, если необходимо

