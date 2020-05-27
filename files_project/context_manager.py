with open('csv_data.txt','r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

for line in lines:
    line = line.split(',')
    name = line[0].title()
    age = line[1]
    university = line[2].upper()
    degree = line[3].upper()

    print(f"{name} is {age}, studying {degree} at {university}")

sample_csv = ','.join(['Joey','30','DRAMA','HOLLYWOOD'])
