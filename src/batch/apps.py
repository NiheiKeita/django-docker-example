from django.apps import AppConfig


class BatchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'batch'

    def ready(self):
        from .management.commands.example_batch import start
        start()
