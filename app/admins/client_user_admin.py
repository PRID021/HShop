from decouple import config
from django import forms
from django.contrib import admin
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest

from app.modules.auth.models.client_user import ClientUser
from app.tasks.email import send_email_job


class ClientUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password"
    )

    class Meta:
        model = ClientUser
        fields = [
            "name",
            "email",
            "password",
            "phone_number",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["password_confirmation"].required = False
            self.fields["password"].required = False
            self.fields["password_confirmation"].widget = forms.HiddenInput()
            self.fields["password"].widget = forms.HiddenInput()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")
        if self.instance.pk is None:
            if password and password_confirmation and password != password_confirmation:
                raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class ClientUserAdmin(admin.ModelAdmin):
    list_per_page = 30
    form = ClientUserForm
    list_display = ("id", "name", "email", "phone_number", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")

    def save_model(
        self, request: HttpRequest, obj: ClientUser, form: forms.ModelForm, change: bool
    ) -> None:
        raw_password = obj.password
        if change:
            current_user = ClientUser.objects.get(pk=obj.pk)
            self.password = current_user.password
        else:
            obj.password = make_password(obj.password)

        super().save_model(request, obj, form, change)

        if not change:
            send_email_job.delay(
                "[Adventure] Password",
                f"Thank you for using our application. Your password to login is: {raw_password}",
                config("FROM_MAIL"),
                [obj.email],
            )

    def has_delete_permission(self, request, obj=None):
        return True
