## Exercise 9-12 Multiple Modules


from admin_priveleges import Admin



my_admin = Admin('Storage','EMC',23,1096362)

my_admin_privileges = ['create accounts',
                       'delete accounts',
                       'change permissions',
                       ]

my_admin.privileges.privileges = my_admin_privileges

my_admin.privileges.show_privileges()
