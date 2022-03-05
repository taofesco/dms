from django.dispatch import receiver
from django.urls import reverse
from django.db.models.signals import post_save
from django.core.mail import send_mail, EmailMessage 
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from urllib.parse import urlparse

import secrets
from django_rest_passwordreset.signals import reset_password_token_created
from account.models import MyUser, EmailConfirmatiom


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, referer, reset_password_token, *args, **kwargs):
    uri = urlparse(referer)
    context = {
        'scheme': uri.scheme,
        'netloc': uri.netloc,
        'url': reverse('password_reset:reset-password-request'),
        'token': reset_password_token.key
    }

    html_message = render_to_string(
        'account/reset_password.html', context=context)
    plain_message = strip_tags(html_message)
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Workstomer Password Assistance"),
        # message:
        plain_message,
        # from:
        "Workstomer <password-reset-noreply@workstomer.com>",
        # to:
        [reset_password_token.user.email],
        html_message=html_message
    )




    
