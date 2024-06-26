from django.db.models.signals import post_save,post_delete,pre_save,pre_delete
from django.dispatch import receiver,Signal
from .models import Blog
from django_authentications import settings
from django.core.mail import send_mail
from django.contrib import messages


@receiver(post_save,sender=Blog)
def created_blog(sender,instance,created,**kwargs):
    if created:
        subject=f'New blog created: {instance.title}'
        message=f'Hi ,\n A new blog has been published on our website. \n Check it out'
        sender_email=settings.EMAIL_HOST_USER
        # send_mail(subject, message, sender_email, [instance.author.email], fail_silently=False)
        # print('Email sent successfully')









