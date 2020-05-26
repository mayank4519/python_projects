class UncountableError(ValueError):
    def __init__(self, message):
        super().__init__(f'Non negative number {message} not allowed.')

def count_from_zero_to_n(n):
    if n < 0:
      raise UncountableError(n)
    for x in range(0, n+1):
        print(x)

count_from_zero_to_n(-99)