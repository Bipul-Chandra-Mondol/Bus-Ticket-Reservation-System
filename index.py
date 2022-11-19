"""
Bus Ticket Reservation System ,,,,,,Both user and Admin # admin username=admin and password=1234
Author: Bipul Chandra Mondol 
"""

class User:
    def __init__(self,username,password) -> None:
        self.username=username
        self.password=password


class Bus:
    def __init__(self,coach,driver,arrival,departure,from_des,to) -> None:
        self.coach=coach
        self.driver=driver
        self.arrival=arrival
        self.departure=departure
        self.from_des=from_des
        self.to=to
        self.seat=["empty" for i in range(20)]


class PhitronCompany:
    total_bus=5
    total_bus_list=[] #dummy Database
    def install(self):
        bus_no=int(input("Enter Bus NO : "))
        flag=1
        for bus in self.total_bus_list:      # checking this bus is already available or not 
            if bus_no==bus['coach']:
                print('This bus is already installed')
                flag=0
                break
        if flag:
            bus_driver=input("Enter bus driver Name: ")
            bus_arrival=input('Enter arrival time: ')
            bus_departure=input('Enter departure time: ')
            bus_from=input('Enter bus start from: ')
            bus_to=input('Enter bus destination To: ')
            self.new_bus=Bus(bus_no,bus_driver,bus_arrival,bus_departure,bus_from,bus_to)
            self.total_bus_list.append(vars(self.new_bus))
            print('\n Bus installed successfully\n')


class BusCounter(PhitronCompany):   # for only user or counter officer
    user_list=[]  #user database
    def reservation(self):
        bus_num=int(input("Enter Bus number: "))
        bus_found=False
        for bus in self.total_bus_list:
            if bus_num==bus['coach']:
                bus_found=True
                passenger=input("Enter Your Name: ")
                seat_no=int(input("Enter Your seat Number:"))
                if seat_no-1>19:
                    print("Only 20 seat are Available ")
                elif bus['seat'][seat_no-1] != 'empty':
                    print('This seat is alredy booked')
                else:
                    bus['seat'][seat_no-1]=passenger
        if not bus_found:
            print('This bus is not available')

    def showBusInfo(self):
        bus_no=int(input("Enter Bus No: "))
        for bus in self.total_bus_list:
            if bus['coach']==bus_no:
                print('*'*50)
                print()
                print(f"{' '*10} {'#'*10} Bus INFO {'#'*10}")
                print(f"Bus Number : {bus_no} \t\t Driver Name: {bus['driver']}")
                print(f"Arrival Time: {bus['arrival']} \t\t Departure Time :{bus['departure']}")
                print(f"start from: {bus['from_des']} \t\t Destination : {bus['to']}")
                # print(bus['seat'])
                # print bus sit in decorated way
                a=1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}.{bus['seat'][a-1]} \t",end='')
                        a+=1
                    print('\t',end="")
                    for j in range(2):
                        print(f"{a}.{bus['seat'][a-1]} \t",end='')
                        a+=1
                    print()

    def get_users(self):
        return self.user_list

    def create_account(self):
        name=input("Enter your user name: ")
        flag=0
        for user in self.get_users():
            if user['username']==name:
                print("Username alrady exist")
                flag=1
                break
            
        if flag==0:
            password=input("Enter your password: ")
            self.new_user=User(name,password)
            self.user_list.append(vars(self.new_user))
            print("Account created Sucessfully")

    def available_buses(self):
        if len(self.total_bus_list)==0:
            print("No buses Available")

        else:  # buses are available
            for bus in self.total_bus_list:
                print('*'*50)
                print()
                print(f"{' '*10} {'#'*10} Bus INFO__coach:{bus['coach']} {'#'*10}")
                print(f"Bus Number : {bus['coach']} \t\t Driver Name: {bus['driver']}")
                print(f"Arrival Time: {bus['arrival']} \t\t Departure Time :{bus['departure']}")
                print(f"start from: {bus['from_des']} \t\t Destination : {bus['to']}")
                # print(bus['seat'])
                # print bus sit in decorated way
                a=1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}.{bus['seat'][a-1]} \t",end='')
                        a+=1
                    print('\t',end="")
                    for j in range(2):
                        print(f"{a}.{bus['seat'][a-1]} \t",end='')
                        a+=1
                    print()


if __name__=="__main__":
    while True:
        counter=BusCounter()
        print("1. Create An account \n 2.Log in To your account \n 3.Exit")
        user_input=int(input("Enter Your choice:"))
        if user_input==3:
            break
        elif user_input==1:
            counter.create_account()
        elif user_input==2:
            name=input("Enter your Name:")
            password=input("Enter your password:")
            isAdmin=False
            flag=0
            if name=="admin" and password=="1234":
                isAdmin=True
            if isAdmin==False:
                for user in counter.get_users():
                    if user['username']==name and user['password']==password:
                        flag=1
                        break
                if flag:
                    while True:
                        print(f"1.Available Buses \n 2.Show Bus info \n 2.Reservation \n 4.Exit")
                        a=int(input("Enter Your Choice: "))
                        if a==4:
                            break
                        elif a==1:
                            counter.available_buses()
                        elif a==2:
                            counter.showBusInfo()
                        elif a==3:
                            counter.reservation()
                else:
                    print("Your Account Not Found \n Please Create an account")
            else:
                while True:
                    print("Hello Admin, Welcome back")
                    print(f"1.Install Bus \n 2.Available Buses \n3.Show Bus Info \n 4.Show user List \n 5.Exit")
                    a=int(input("Enter Your choice: "))
                    if a==5:
                        break
                    elif a==1:
                        counter.install()
                    elif a==2:
                        counter.available_buses()
                    elif a==3:
                        counter.showBusInfo()
                    elif a==4:
                        print(counter.get_users())
                

                    

# company=PhitronCompany()
# company.install()
# print(company.total_bus_list)

# ticket=BusCounter()
# ticket.reservation()

# for bus in ticket.total_bus_list:
#     print(bus['seat'])

# ticket.showBusInfo()
# user=BusCounter()
# user.create_account()
# b=BusCounter()
# b.install()
# b.install()
# b.available_buses()


