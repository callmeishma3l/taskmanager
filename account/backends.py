from django.conf import settings
from django.contrib.auth import get_user_model

class MyBackend(object):
    my_user_model = get_user_model()

    def get_user(self, email):
        try:
            return self.my_user_model.objects.get(email=email)
        except self.my_user_model.DoesNotExist:
            return None

    def authenticate(self, email=None, password=None):
        user = self.get_user(email)

        if user:
            if user.check_password(password):
                return user
            else:
                return None