
f=open("station_vl.txt", "r")
f1 = f.readlines()

NUMBER_OF_DAYS = 10
NUMBER_OF_HOURS = 24
data = []
data1 = []

for line in f1:
    if line[0] == '#':
        continue
    data.append(line.strip().split())


for item in data:
    print(item[1])


# for i in range(NUMBER_OF_DAYS):
#     data.append([])
#  for j in range(NUMBER_OF_HOURS): data[i].append([])

# read input using input redirection from a file





 # ... hier jouw code ...
# print("Gemiddelde temperaturen: ")
# find the average daily temperature
# for i in range(NUMBER_OF_DAYS):

 # ... hier jouw code ...