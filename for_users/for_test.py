import os

race_list = []
directory = os.fsencode("staticData/races")
for file in os.listdir(directory):
    class_name = os.fsdecode(file)
    with open(f"staticData/races/{class_name}") as my_file:
        race_list.append(my_file.read())
print(race_list)


