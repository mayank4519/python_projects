friends = input("enter 3 friends seperated by commas").split(',')

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]
people.close()

friends_set = set(friends)
people_nearby = set(people_nearby)
friends_nearby_set = friends_set.intersection(people_nearby)


nearby_friends = open('nearby_friends.txt', 'w')
for f in friends_nearby_set:
    print(f"{f} is nearby. Add to the list!")
    nearby_friends.write(f'{f}\n')

nearby_friends.close()
