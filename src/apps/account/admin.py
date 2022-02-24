from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import (
    UserChangeForm, UserCreationForm, AdminPasswordChangeForm)
from django.contrib.admin import site
# Register your models here.

# class UserProfileInline(admin.StackedInline):
#     model = UserProfile
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     inlines = [UserProfileInline,]


@admin.register(User)
class CUserAdmin(UserAdmin):
    add_form_template = 'admin/auth/user/add_form.html'
    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('username', 'password',"email")}),
        (_("Personal Details"),{'fields':["display_name","picture_url"]}),
         # (_('Personal info'), {
         #     'fields': ('first_name','last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        #(_("Priviledge Access"),{"fields":("role",)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    search_fields = ["username"]
    change_password_form = AdminPasswordChangeForm
    list_display = ("username","is_staff",)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = search_term
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(username=search_term_as_int)
        return queryset, use_distinct
