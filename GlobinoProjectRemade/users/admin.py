from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# from users.forms im

# Register your models here.
User = get_user_model()

@admin.register(User)
class UserAdmin(UserAdmin):

    model = User

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'identifier',
                    'dep_1',
                    'dep_2',
                    'dep_3',
                    'dep_4',
                    'dep_5',
                    'update_permission',
                    'send_message',

                )

            }

        )
    )