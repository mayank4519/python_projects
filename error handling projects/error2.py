class myCustomError(TypeError):
    def __init__(self, message, code):
        super().__init__(f'Error code : {message}, {code}')
        self.code = code

raise myCustomError('An error happened!', 500)

