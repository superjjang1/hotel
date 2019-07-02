
hotel = {
 '1': {
   '101': ['George Jefferson', 'Wheezy Jefferson'],
   '102': [],
   '103': []
 },
 '2': {
   '201': ['Jack Torrance', 'Wendy Torrance'],
   '202': [],
   '239': []
 },
 '3': {
   '301': ['Neo', 'Trinity', 'Morpheus'],
   '302': [],
   '303': []
 }
}
def check_in():
    floor_num = input("What floor number? ") #input the floor
    guest_floor_selection = hotel.get(floor_num) #pulls from dictionary
    guest_list = []
    if guest_floor_selection == None:
        print("Not a valid floor number, please select a real floor.")
        check_in()#recalls the checkin function 
    room_num = input("what room number? ")
    if hotel.get(floor_num).get(room_num) == None: #if the user ends up choosing wrong room as well
        print("Not a valid room") #error message
        check_in() #return the function
    if hotel.get(floor_num).get(room_num) != []:#choose a room with people
        print("Sorry that room has people in it.")
        check_in()#return the function
    else:
        num_guests = int(input("How many in your party?: (enter a number)"))#occupants
        guest_list.append(input("What is your name?: (please write your name)")) #input name
        for num in range(0,num_guests -1): #for loop for yourself and the guests so it keeps asking their name till
            next_guest = input("Please enter the name of your next guest: ")# next person till the end
            guest_list.append(next_guest) #adds into dictionary of guests
        hotel[floor_num][room_num] = guest_list #this adds into dictionary
        print(f"Thank you {guest_list[0]}, enjoy your stay.")# thanks the first name entered

def check_out():
    floor_num = input("What was your floor number? (Enter the number): ")# floor number guest was staying in
    room_num = input("What was your room number? (enter the room number): ")#room number
    if hotel.get(floor_num).get(room_num) == []:
        room_num = input ("Sorry, that room had nobody in it, select a new room: (enter your room number) ")#error input of room with no occupants
    else:
        hotel[floor_num][room_num] = []
        print("Thanks for staying butt head. ")

#room1 is guests
#party_man is guest list
#floor 1 is floors
#room2 rooms
#room3 guests in rooms
def guest_list():
    party_man = [] #party
    for floor1, room1 in hotel.items():
        for room2,room3 in room1.items():
            if len(room3) != 0:
                for room1 in room3:
                    party_man.append(room1)
    print(",".join(party_man))

def checkin_menu():
    while True:
        menu = (input("""Please choose from the following
        Enter '1' to check in
        Enter '2' to check out
        Enter '3' for the guest list
        enter '4' to exit
        """)) #triple " to keep the line format
        if menu == '1':
            check_in()
        elif menu == '2':
            check_out()
        elif menu == '3':
            guest_list()
        elif menu == '4':
            break
        else:
            print("Invalid input")
checkin_menu()