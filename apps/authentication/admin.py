from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()


class UserAccountAdmin(admin.ModelAdmin):
  list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
  list_filter = ('is_staff', 'is_active')
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('email',)


admin.site.register(User, UserAccountAdmin)
