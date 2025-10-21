#get to different sections
#for context RackB Lower = 1, RackB Upper = 2, RackA Upper = 3, RackA Lower = 4
#Starts at Bay exit facing north
from machine import Pin, PWM
from utime import sleep

def area_code(Rack, Level):
    if Rack == "Rack B" and Level == "Lower":
        return 1
    if Rack == "Rack B" and Level == "Upper":
        return 2
    if Rack == "Rack A" and Level == "Upper":
        return 3
    if Rack == "Rack A" and Level == "Lower":
        return 4

def get_to_area(area):
    if area == 1:
        go_to_area1() #goes to Purple lower
    elif area == 2:
        bay_exit_to_lower_junction() #goes to lower junction
        go_to_area2() #goes to Purple upper
    elif area == 3:
        bay_exit_to_lower_junction() #goes to lower junction
        go_to_area3() #goes to Orange upper
    elif area == 4:
        bay_exit_to_lower_junction() #goes to lower junction
        go_to_area4() #goes to Orange lower

if __name__ == "__main__":
    area = area_code(scaner_info[0], scanner_info[1])
    go_to_area(area)
        
