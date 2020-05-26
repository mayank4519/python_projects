#another example
class RuntimeError(TypeError):
    """
    Error occured cos of exception
    """
    def __init__(self, message, code):
        super().__init__(f'Error code : {message}, {code}')
        self.code = code

err = RuntimeError('An error happened!', 500)
print(err.__doc__)