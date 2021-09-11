#with open("weather_data.csv") as data_file_25:
 #   data = data_file_25.readlines()
  #  print(data)


#import csv

#with open("weather_data.csv") as data_file_25:
 #   data = csv.reader(data_file_25)
  #  temperatures = []
   # for row in data:
    #    if row[1] != "temp":
     #       temperatures.append(int(row[1]))
    #print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
#print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))

average = sum(temp_list) / len(temp_list)
print(average)

print(data["temp"].mean())

print(data["condition"])
print(data.condition)

print(data[data.day == "Monday"])
print(data.temp == data.temp.max())

data_dict = {
    "students": ["Rutu", "Piyu", "Sammu"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")



