from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

class AccountAdmin(UserAdmin):
	display_list	= ['email','username','date_join','last_login','is_admin,','is_superuser'],
	readonly_list	= ['id','date_join','last_login']
	search_fields	= ['email','username']

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Account, AccountAdmin)
