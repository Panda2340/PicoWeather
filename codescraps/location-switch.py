#This script allows the user to press a button to change the location they are viewing the weather for.
location = 0
#0 - Toronto, ON
#1 - New York City, NY
#2 - Buffalo, NY
#3 - London, UK
#4 - Vancouver, BC
#5 - Los Angeles, CA
#6 - Montreal, QC
repeatfunc = 0
def locationswitch():
while True:
    if not button_a.value and location == 0():
      location = 1
    if not button_a.value and location == 1():
      location = 2
    if not button_a.value and location == 2():
      location = 3
    if not button_a.value and location == 3():
      location = 4
    if not button_a.value and location == 4():
      location = 5
    if not button_a.value and location == 5():
      location = 6
      repeatfunc = 1
  if repeatfunc == 1:
    locationswitch()
    repeatfunc = 0
