from decouple import config
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest

from app.modules.auth.models.client_user import ClientUser
from app.tasks.email import send_email_job


# class ClientUserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput, label="Password")
#     password_confirmation = forms.CharField(
#         widget=forms.PasswordInput, label="Confirm Password"
#     )

#     class Meta:
#         model = ClientUser
#         fields = [
#             "name",
#             "email",
#             "password",
#             "phone_number",
#         ]

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.instance and self.instance.pk:
#             self.fields["password_confirmation"].required = False
#             self.fields["password"].required = False
#             self.fields["password_confirmation"].widget = forms.HiddenInput()
#             self.fields["password"].widget = forms.HiddenInput()

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password_confirmation = cleaned_data.get("password_confirmation")
#         if self.instance.pk is None:
#             if password and password_confirmation and password != password_confirmation:
#                 raise forms.ValidationError("Passwords do not match.")
#         return cleaned_data


class ClientUserAdmin(UserAdmin):
    list_per_page = 30

    def save_form(self, request, form, change):
        # Access raw password in save_form
        raw_password = form.cleaned_data.get("password1")

        # Create or modify the instance returned by save_form
        obj = super().save_form(request, form, change)

        # Attach raw_password as a custom attribute to the user object
        if raw_password:
            obj.raw_password = raw_password

        return obj

    def save_model(
        self, request: HttpRequest, obj: ClientUser, form: forms.ModelForm, change: bool
    ) -> None:

        # Access the raw_password in save_model, if it was set in save_form
        raw_password = getattr(obj, "raw_password", None)

        # Save the user
        super().save_model(request, obj, form, change)

        # If it's a new user, send an email with the raw password
        if not change and raw_password:
            send_email_job.delay(
                "[Adventure] Password",
                f"Thank you for using our application. Your password to login is: {raw_password}",
                config("FROM_MAIL"),
                [obj.username],
            )
