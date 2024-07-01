from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.contrib.auth import get_user_model
from .models import ActivityLog

User = get_user_model()


@receiver(post_save, sender=User)
def log_user_activity(sender, instance, created, **kwargs):
    action = 'Користувач створений!!!' if created else 'Оновлено дані користувача!!!'
    ActivityLog.objects.create(user=instance, action=action)

@receiver(post_save, sender=User)
@receiver(pre_save, sender=User)
def handle_user_email(sender, instance, created=False,  **kwargs):
    if created:
        user_log = ActivityLog.objects.filter(user=None).last()
        user_log.user = instance
        user_log.save()
    else:
        default_email = f'{instance.username}.nonreal@gmail.com'
        action = f'Встановлено Email за замовчуванням {default_email} для користувача {instance.username}' if not instance.email else False
        instance.email = instance.email or default_email
        if action:
            ActivityLog.objects.create(action=action)


