from django.apps import AppConfig


class HoobyAppConfig(AppConfig):
    name = 'hooby_app'

    def ready(self):
        import hooby_app.signals