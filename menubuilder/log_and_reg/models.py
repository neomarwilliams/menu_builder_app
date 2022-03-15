from django.db import models
# import re
# import bcrypt


# # Create your models here.
# class UserManager(models.Manager):
#     def user_validator(self, postData):
#         errors = {}
#         EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._]+\.[a-zA-Z]+$')
#         users = User.objects.all()
#         email_check = User.objects.filter(email=postData['email'])
#         username_check = User.objects.filter(username=[postData['username']])
#         if email_check:
#             errors['duplicate_email']='This email is already in use'
#         if username_check:
#             errors['duplicate_username']='This username is taken'
#         if len(postData['first_name']) < 2:
#             errors['first_name'] = 'First name must be at least 2 characters.'
#         if len(postData['last_name']) < 2:
#             errors['last_name'] = 'Last name must be at least 2 characters.'
#         if not EMAIL_REGEX.match(postData['email']):
#             errors['email'] = 'Please provide a valid email adress.'
#         if len(postData['username']) < 2:
#             errors['username'] = 'Username must be at least 2 characters'
#         if len(postData['password']) < 8:
#             errors['password'] = 'Password must be at least 8 characters.'
#         if not postData['password'] == postData['conf_password']:
#             errors['pw_not_match'] = 'Passwords do not match'

#         return errors

class User(models.Model):
    # //changed name field
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    # new field needs validations
    # added validations for duplicate username and min length
    username = models.CharField(max_length=16)

    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = UserManager()