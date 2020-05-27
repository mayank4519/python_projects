import json

file = open('csv_file.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines]
json_list = []
json_str = {"club": "club",
            "city": "city",
            "country": "country"}

for line in lines:
    club,city,country = line.split(',')
    json_str["club"] = club
    json_str["city"] = city
    json_str["country"] = country

    json_list.append(json_str)

print(json_list)

json_file = open('json_file.txt', 'w')
json.dump(json_list, json_file)
json_file.close()