user = {'username': 'mayank4519', 'password':'admin'}

def check_permission(func):
    def secure_fn(name):
        if user.get('password') == 'admin':
            return func(name)
    return secure_fn

#Set the decorator here
@check_permission
def delete_account(name):
    return f"{name} account is successfully deleted!"

print(delete_account.__name__, ('Mayank'))