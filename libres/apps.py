from django.apps import AppConfig

class LibresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'libres'
    
    def ready(self):
        from . import squash
