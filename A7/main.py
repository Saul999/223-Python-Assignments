from flights import *

flights = Flights()


print("          *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU")

print("     1. Add flight\n2. Print flight schedule\n3. Set flight schedule filename\n9. Exit the program")

menuchoice = input("Enter Menu Choice: ")
if menuchoice == 1:
    origin = input("Enter origin:")
    destination = input("Enter destination:")
    flightnumber = input("Enter flight number:")
    departuretime = input("Enter departure time (HHMM):")
    arrivaltime = input("Enter arrival time (HHMM):")
    arrivalday = input("Is arrival next day (Y/N):")

    flights.add_flight(origin, destination, flightnumber,departuretime,arrivalday, arrivaltime)

    print()
elif menuchoice == 2:
    print("================== FLIGHT SCHEDULE ==================\nOrigin Destination Number Departure  Arrival Duration\n====== =========== ====== ========= ======== ========")

    f = flights.get_flights()
    print(f)

elif menuchoice == 3:
    fn = input('File name: ')
    flights = Flights(filename = fn)

elif menuchoice == 9:
    quit






