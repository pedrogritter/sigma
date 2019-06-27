from django.apps import AppConfig


class UserProfilesConfig(AppConfig):
    name = 'userprofiles'

    def ready(self):
        import userprofiles.signals
