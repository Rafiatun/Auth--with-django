from django.contrib.auth import get_user_model
from django.contrib.auth.backends import  ModelBackend, UserModel
from django.contrib.auth.models import User


class CaseInsensitive(ModelBackend):

    def Authenticate(self, request , username=None, password=None , **kwagrs ):
        UserModel=get_user_model()
        if username is None:
            username=kwagrs.get(UserModel.USERNAME_FIELD)

        try:
           case_insensitivie_email_field= '{}__iexact'.format(UserModel.USERNAME_FIELD)
           user=UserModel._default_manager.get(**{case_insensitivie_email_field: username})

        except UserModel.DoesNotExist:
            UserModel().set_password(password)

        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user