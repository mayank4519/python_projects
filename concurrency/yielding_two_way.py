from collections import deque

friends = deque(('Ross', 'Monica', 'Chandler', 'Rachel', 'Joey', 'Phoebe'))

def get_friend():
    yield from friends

def greet(g):
    while True:
        try:
            greeting = next(g)
            yield f'Hi, {greeting}'
        except StopIteration:
            print(f"Done executing")

friend = get_friend()
g = greet(friend)

print(next(g))
print(next(g))
print(next(g))