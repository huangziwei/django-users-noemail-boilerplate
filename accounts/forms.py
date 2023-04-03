from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)

    def save(self, commit=True):
        name = self.cleaned_data.get("name", None)
        return super().save(commit=commit)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username",)
