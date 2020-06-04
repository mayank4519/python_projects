user = {'username':'mayank4519', 'password':'admin'}

#Simple decorator fn creation
def check_permission(func):
    def secure_fn():
        if user.get('password') == 'admin':
            return func()
    return secure_fn

def delete_account():
    return "Account deleted!"

my_secure_fn = check_permission(delete_account)
print(my_secure_fn())
