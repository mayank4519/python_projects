import functools

user = {'username': 'mayank4519', 'password':'admin'}

def check_permission(func):
    @functools.wraps(func)
    def secure_fn():
        if user.get('password') == 'admin':
            return func()
    return secure_fn

#Set the decorator here
@check_permission
def delete_account():
    return "Account deleted!"

#Set another decorator
@check_permission
def another_fn():
    pass

print(delete_account())
print(delete_account.__doc__)
print(delete_account.__name__)
print(another_fn.__name__)