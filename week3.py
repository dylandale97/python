#opgave 1 en 2
'''
Opgave 1a:
i = 3, j = 0
i = 4, j = 0

Opgave 1b:
I am class A
I am class B
i = 1
i = 1, j = 2
opgave 2
staat in me map getekend.
'''
#opgave 3
class Circle():
    def init(self, straal, pie = 3.14):
        self.straal = straal
        self.pie = pie

    def getOppervlakte(self):
        oppervlakte = self.straal * self.straal * self.pie
        print(oppervlakte)

    def getOmtrek(self):
        omtrek = (self.straal + self.straal) * self.pie
        print(omtrek)

new_circle = Circle(8)
new_circle.getOppervlakte()
new_circle.getOmtrek()
#opgave 4
class Roman(object):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    @classmethod
    def roman_to_int(cls, roman):
        res = 0
#       for letter in roman:
        for i in range(len(roman)):
            roman_digit = roman[i]
            if i < len(roman) - 1:
                next_roman_digit = roman[i+1]
                if Roman.rom_val[next_roman_digit] > Roman.rom_val[roman_digit]:
                    # volgende >= huidig
                    res -= Roman.rom_val[roman_digit]
                else:
                   # volgende <= huidige
                    res += Roman.rom_val[roman_digit]
            else:
                res += Roman.rom_val[roman_digit]


        print(roman, res)
        return res


assert Roman.roman_to_int('C') == 100
assert Roman.roman_to_int('XLIX') == 49
assert Roman.roman_to_int('MMMCMLXXXVI') == 3986
#opgave 5

#opgave 6
class StopWatch():
    startTime = 0
    endTime = 0

    # def __init__(self, start_time):
    #     self.startTime = start_time

    def __init__(self):
        self.startTime = 0

    def start(self, st):
        self.startTime = st
        # print(self.startTime)
    
    def stop(self, ht):
        self.endTime = ht

    def get_elapsed_time(self):
        return self.endTime - self.startTime
    
    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime
    

from StopWatch import StopWatch
size = 1000000
stopWatch = StopWatch()
stopWatch.start(size)
sum = 0
for i in range(1, size + 1):
    sum += i
    
stopWatch.stop(sum)
print("The loop time is", stopWatch.get_elapsed_time(), "milliseconds")

#opgave 7
#a) Ja statement 3 wordt dan nog uitgevoerd.
#b) Nee, de statement wordt dan niet uitgevoerd.
#c) Ja statement 4 wordt dan alsnog uitgevoerd.

#opgave 8
#a) 
import json, requests, sys from pprint import pprint


# get command line arguments
if len(sys.argv) < 2:
 print('Usage: quick_weather.py location')
 sys.exit()
# argument 0 is program name
location = ' '.join(sys.argv[1:])
# download JSON data
url = "api.openweathermap.org/data/2.5/weather?id=2744344"
response = requests.get(url)
response.raise_for_status()
# load JSON data into Python variable
weatherData = json.loads(response.text)
w = weatherData['list']

#pprint(w)
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

#b) Wat doet de methode json.loads ?  idk

#opgave 9

# Check results
# =============

# W293:14:1:blank line contains whitespace
# W293:20:1:blank line contains whitespace
# W293:26:1:blank line contains whitespace
# E402:28:1:module level import not at top of file
# W293:35:1:blank line contains whitespace
# W391:39:1:blank line at end of file