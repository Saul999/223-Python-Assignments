from weather import *

myfile = "weather.dat"

mychoice = 0
while(True):
    print("     *** TUFFY TITAN WEATHER LOGGER MAIN MENU")
    print()
    print("1. Set data Filename")
    print("2. Add Weather Data")
    print("3. Print Daily Report")
    print("9. Exit the program")

    choice = input("Enter Data Filename")

    print()
    if mychoice == 1:
        myfile = input("Enter Data Filename:")
        weather = read_data(myfile)
    elif mychoice  == 2:
        dt = int(input("Enter date: "))
        tm = input("enter time: ")
        t = int(input("Enter humidity: "))
        h = int(input("Enter the Rainfall: "))
        r = float(input("Enter rainfall: "))
        weather[dt+tm] = {'t':t,'h':h,'r':r}
        write_data(weather, myfile)
    elif mychoice == 3:
        d = input("Enter Date: ")
        display = report_daily(data = weather, date = d)
        print(display)

    elif mychoice == 4:
        display = report_historical(data = weather)
        print(display)


