import json
names = {'name': 'Carol','sex': 'female','age': 55}
def save_json(dict1):
    with open('file.json', 'w') as my_file:
        #saving to file and adding indent
        json.dump(dict1, my_file, indent=4)
save_json(names)
# Second function
def read_json():
    with open('file.json', 'r') as my_file:
        json_file = json.load(my_file) 
    return json_file
print(read_json())