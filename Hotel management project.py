class data:
    def package_charges(self):
        print("Packages are 1.Normal package \t2.Delux package \t3.Super-Delux Package")
        e = input("Which package you chose: ")
        if(e=="1"):
            print("Your charges are Rs3000")
            print("\nThanks for booking🤗🤩")
        elif(e=="2"):
            print("Your charges are Rs7000")
            print("\nThanks for booking🤗🤩")
        elif(e=="3"):
            print("Your charges are Rs14,500")
            print("\nThanks for booking🤗🤩")
        else:
            print("Please enter correct choice")
            obj.package_charges()
    
    # filling ur choice for booking of rooms in direct booking section
    def booking_section(self):
        print("N = Normal, D = Delux, SD = Super-Delux, SB = Single Bed, DB = Double Bed, KB = King Bed")
        c = input("Which category you chose(N, D, SD): ")
        if(c=="N" or c=="D" or c=="SD"):
            d = input("Enter type of room(SB, DB, KB): ")
            if(d=="SB" or d=="DB" or d=="KB"):
                e = int(input("How many nights u want to stay: "))
                obj.booking_charges(c,d,e)
            else:
                print("Please enter correct data")
                d = input("Enter type of room(SB, DB, KB): ")
                e = int(input("How many nights u want to stay: "))
                obj.booking_charges(c,d,e)
        else:
            print("Please enter correct data")
            c = input("Which category you chose(N, D, SD): ")
            d = input("Enter type of room(SB, DB, KB): ")
            e = int(input("How many nights u want to stay: "))
            obj.booking_charges(c,d,e)

    def booking_charges(self, category, type, nights):
        if(category == "N"):
            if(type=="SB"):
                print("Yours total charges are Rs", nights*500)
                print("\nThanks for booking🤗🤩")
            elif(type=="DB"):
                print("Yours total charges are Rs", nights*900)
                print("\nThanks for booking🤗🤩")
            elif(type=="KB"):
                print("Yours total charges are Rs", nights*2000)
                print("\nThanks for booking🤗🤩")
            else:
                print("Please enter correct data")
                d = input("Enter type of room(SB, DB, KB): ")
        elif(category == "D"):
            if(type=="SB"):
                print("Yours total charges are Rs", nights*1200)
                print("\nThanks for booking🤗🤩")
            elif(type=="DB"):
                print("Yours total charges are Rs", nights*2000)
                print("\nThanks for booking🤗🤩")
            elif(type=="KB"):
                print("King Bed is not available in this category")
                print("Please re-enter the data")
                d = input("Enter type of room(SB, DB, KB): ")
                e = int(input("How many nights u want to stay: "))
                obj.booking_charges(type,d,e)
            else:
                print("Please enter correct data")
                d = input("Enter type of room(SB, DB, KB): ")
                e = int(input("How many nights u want to stay: "))
                obj.booking_charges(category,d,e)

        elif(category == "SD"):
            if(type=="SB"):
                print("Yours total charges are Rs", nights*2500)
            elif(type=="DB"):
                print("Yours total charges are Rs", nights*3800)
            elif(type=="KB"):
                print("King Bed is not available in this category")
                print("Please re-enter the data")
                d = input("Enter type of room(SB, DB, KB): ")
                e = int(input("How many nights u want to stay: "))
                obj.booking_charges(category,d,e)
            else:
                print("Please enter correct data")
                d = input("Enter type of room(SB, DB, KB): ")
                e = int(input("How many nights u want to stay: "))
                obj.booking_charges(category,d,e)

    # shows room details
    def booking_section_selection(self):
        while(1):
            a = input("Would you like to check more room details(y/n): ")
            if(a=="y"):
                b = input("\nWhich type of room you would like to see(Normal, Delux, Super-Delux): ")
                if(b=="Normal"):
                    print("Rooms in this category are: ")
                    print("1.Single Bed : Rs 500/day\n2.Double bed : Rs 900/day\n3.King bed : Rs 2000/day")
                    print("\nFacilities are:")
                    print("1.TV\n2.Chair/Desk\n3.Cupboards\n4.Single bathroom\n ")
                    obj.booking_section_selection()
                    break;
                    
                elif(b=="Delux"):
                    print("Rooms in this category are: ")
                    print("1.Single Bed : Rs 1200/day\n2.Double bed : Rs 2000/day")
                    print("\nFacilities are:")
                    print("1.LED\n2.Chair/Desk\n3.Cupboards\n4.Private bathroom\n5.Telephone\n6.Room service\n7.Fully AC")
                    obj.booking_section_selection()
                    break;
                elif(b=="Super-Delux"):
                    print("Rooms in this category are: ")
                    print("1.Single Bed : Rs 2500/day\n2.Double Bed : Rs 3800/day")
                    print("\nFacilities are:")
                    print("1.LED\n2.Chair/Desk\n3.Cupboards\n4.Private bathroom\n5.Telephone\n6.Room service") 
                    print("7.Free unlimited wi-fi 8.Fully AC")
                    obj.booking_section_selection()
                    break;
                else:
                    print("Please enter correct data")
            elif(a=="n"):
                f = input("\nIn which section you would like to do booking(1.Packages, 2.Direct booking): ")
                if(f=="1"):
                    obj.package_charges();
                    break;
                else:
                    obj.booking_section();
                    break;
            else:
                print("Please enter correct information")
                obj.booking_section_selection()
                break;

    def choice_to_check_booking_section(self):
        while(1):
            a = input("\nWould you like to check direct booking option also(y/n): ")
            if(a=="y"):
                obj.choose_option();
                break;
            elif(a=="n"):
                obj.package_charges();
                break;
            else:
                print("Please enter correct information")
                obj.choice_to_check_booking_section()
                break;

    # choose one of the thre given options
    def choose_option(self):
        print("Choose an option \n1.Packages \t\t2.Direct Booking \t\t3.Change login password")
        while(1):
            option = input("Enter your choice(1 or 2 or 3):")
            if(option=="1"):
                packages =('''\nPackages are
1.Normal Package                    2.Delux Package                3.Super-Delux Package")
* Double Bed                        * Double Bed                   * Double Bed
* 5 days 4 nights                   * 5 days 4 nights              * 5 days 4 nights
* Charges: Rs3000                   * Charges: Rs7000              * Charges: Rs14,500
* Free wi-fi                        * Free wi-fi                   * Free wi-fi
* Free breakfast                    * Free breakfast+Lunch         * Free food(3 times)''')
                print(packages)
                obj.choice_to_check_booking_section()
                break;
            elif(option == "2"):
                print("\nRooms available here are ", Room_types)
                obj.booking_section_selection()
                break;
            elif(option=="3"):
                change_password()
                break;
            else:
                print("Please enter correct choice")
                obj.choose_option()
                break;

obj = data()

def change_password():
    old_pswd = input("Enter old pswd: ")
    new_pswd = input("Enter new pswd: ")
    if(old_pswd == "Singla786"):
        print("Password updated successfully \n")
        name = input("Enter login ID: ")
        pswd = input("Enter password: ")

        while(name!="Chandni Singla" or pswd!=new_pswd):
            print("Wrong ID and Password, Re-enter it")
            name = input("Enter-login ID: ")
            pswd = input("Enter password: ")
        else:
            print("Logged in successfully")
            print("\nHi! customer😍\n")
            obj.choose_option();

    else:
        print("Incorrect old password")
        change_password()

Room_types = ["Normal", "Delux", "Super-Delux"]

start = "Hi Manager😊"
print(start)
name = input("Enter login ID: ")
pswd = input("Enter password: ")

# condition 4 checking whether login id and pswd r correct or not
while(name!="Chandni Singla" or pswd!="Singla786"):
    print("Wrong ID and Password, Re-enter it")
    name = input("Enter-login ID: ")
    pswd = input("Enter password: ")
else:
    print("Logged in successfully")
    print("\nHi! customer😍")
    print("WELCOME TO HOTEL CROWN PLAZA🏨\n")
    obj.choose_option();



