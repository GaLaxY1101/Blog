from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class MyAccountManager(BaseUserManager):
	def create_user(self,email,password = None,username = None):
		if not email:
			raise ValueError('User must have an email')
		if not username:
			raise ValueError('User must have an username')
		user = self.model(
			email = self.normalize_email(email),
			username = username,
		)
		user.set_password(password)
		user.save(using = self._db)
		return user


	def create_superuser(self,email,password, username):
		if not email:
			raise ValueError('User must have an email')
		if not username:
			raise ValueError('User must have an username')
		user = self.create_user(
			email = self.normalize_email(email),
			username = username,
			password = password,
		)
		user.is_admin 		= True
		user.is_staff 		= True
		user.is_superuser 	= True	

		user.set_password(password)
		user.save(using = self._db)
		return user
		
class Account(AbstractBaseUser):
	email				= models.EmailField(max_length=60, unique = True)
	username 			= models.CharField(max_length=50, unique = True)
	first_name 			= models.CharField(max_length=50, default = None, null=True, blank = True)
	last_name 			= models.CharField(max_length=50, default = None, null=True, blank = True)


	date_join			= models.DateTimeField(auto_now_add = True)
	last_login 			= models.DateTimeField(auto_now = True)
	
	is_active			= models.BooleanField(default = True)
	is_staff 			= models.BooleanField(default = False)
	is_superuser 		= models.BooleanField(default = False)
	is_admin 			= models.BooleanField(default = False)

	objects = MyAccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __str__(self):
		return self.username

	def has_perm(self, perm, object = None):
		return self.is_admin	

	def has_module_perms(self, app_label):
		return True	

