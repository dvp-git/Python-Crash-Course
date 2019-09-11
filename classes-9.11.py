## Exercise 9-11 Imported Admin


from account import Admin


my_admin = Admin('Storage-Admin','EMC',24,1096362)


my_admin.privileges.privileges = ['can create accounts','can delete accounts','can modify accounts']


my_admin.describe_user()
my_admin.privileges.show_privileges()
