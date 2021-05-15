from django.db import migrations
from django.contrib.auth import get_user_model

USER_LIST = (
    'basic@mail.com', 'premium@mail.com', 'enterprise@mail.com', 'admin@mail.com',
)


def create_basic_users(apps, schema_editor):

    User = get_user_model()
    Plan = apps.get_model('core', 'Plan')
    Plan.objects.all().delete()

    plans = {
        plan.split("@")[0][0].upper(): plan.split("@")[0].capitalize()
        for plan in USER_LIST
    }

    for plan, name in plans.items():
        Plan.objects.create(id=plan, name=name)
    for user in USER_LIST:
        password = user.split("@")[0]
        plan_id = user[0].upper()
        plan= Plan.objects.get(id=plan_id)
        if 'admin' not in user:
            User.objects.create_user(
                user,
                plan_id,
                password
            )
        else:
            User.objects.create_superuser(user, plan_id, password)


def delete_basic_users(apps, schema_editor):
    User = get_user_model()
    Plan = apps.get_model('core', 'Plan')
    User.objects.filter(name__in=USER_LIST).delete()
    Plan.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210515_1445'),
    ]

    operations = [
        migrations.RunPython(create_basic_users, reverse_code=delete_basic_users)
    ]
