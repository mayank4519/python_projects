from collections import deque

friends = deque(('Ross', 'Monica', 'Chandler', 'Rachel', 'Joey', 'Phoebe'))

def friends_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f"{greeting} {friend}")

def greet(g):
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)

greeting = greet(friends_upper())
greeting.send(None)
greeting.send('Hello')
greeting.send('Heyy')