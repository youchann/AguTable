from django.contrib import admin


from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _

from table.models import table,user,teacher,classes



admin.site.register(table)
admin.site.register(user)
admin.site.register(teacher)
admin.site.register(classes)
