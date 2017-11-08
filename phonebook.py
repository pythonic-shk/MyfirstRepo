import csv
import os
t = 0
def viewPhone():
    if os.path.getsize('phonebook.csv') > 0:
        with open('phonebook.csv', 'rb') as fp:
            reader = csv.reader(fp)
            for row in reader:
                print(" ".join(row))
    else:
        print("No Records Found")
    raw_input("Press Any Key to goto Main Menu: ")
def term():
    global t 
    t = 1
def AddCont():
    while(1):
        name_inp = raw_input("Enter the Name of the Contact: ")
        with open("phonebook.csv") as f:
            dict_list = dict(filter(None, csv.reader(f)))
            if name_inp.upper() in dict_list:
                print("Contact Already Present")
            else:
                num_inp = raw_input("Enter the Number of the Contact: ")
                if (name_inp == "" or num_inp == ""):
                    print("Fields can't be left empty")
                else:
                    try:
                        long(num_inp)
                        if (len(num_inp)!=10):
                            print("Contact number should be 10 digits")
                        else:
                            with open('phonebook.csv', 'ab') as fp:
                                a = csv.writer(fp, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                                data = [[name_inp.upper(),num_inp]]
                                a.writerows(data)
                                print("Contact Added")
                    except ValueError:
                        print("Contact should be a number")
        addc = raw_input("Press y to Add Contact.Any other key to goto Main Menu: ")
        if addc.upper() != "Y":
            break
        os.system('cls')
def DelCont():
    while(1):
        if os.path.getsize('phonebook.csv') > 0:
            with open('phonebook.csv', 'rb') as fp:
                reader = csv.reader(fp)
                for row in reader:
                    print(" ".join(row))
            del_name = raw_input("Enter Name of the contact to be deleted: ")
            with open("phonebook.csv") as f:
                dict_list = dict(filter(None, csv.reader(f)))
            if del_name.upper() in dict_list:
                del dict_list[del_name.upper()]
                filename = "phonebook.csv"
                f = open(filename, "wb")
                f.close()
                with open('phonebook.csv', 'wb') as csv_file:
                    writer = csv.writer(csv_file)
                    for key, value in dict_list.items():
                        writer.writerow([key, value])
                print("Contact Deleted")
            else:
                print("The Name does not match the records")
        
            cont = raw_input("Press y to try again.Any Other Key to goto Main Menu: ")
            if cont.upper() != "Y":
                break
            os.system('cls')
        else:
            print("No Records Found")
            raw_input("Press Any Key to goto Main Menu: ")
            break
def errhandler ():
    print "Your input has not been recognized"
    raw_input("Press Any Key to goto Main Menu: ")
def ModCont ():
    while(1):
        if os.path.getsize('phonebook.csv') > 0:
            with open('phonebook.csv', 'rb') as fp:
                reader = csv.reader(fp)
                for row in reader:
                    print(" ".join(row))
            with open("phonebook.csv") as f:
                dict_list = dict(filter(None, csv.reader(f)))
            name_inp = raw_input("Contact Name to Modify: ")
            if name_inp.upper() not in dict_list: 
                print("The name didn't match the records")
            else:
                change_name = raw_input("Modify Name to: ")  
                change_num = raw_input("Modify Number to: ")
                
                if (change_name == "" or change_num == ""):
                    print("Fields can't be left empty")
                else:
                    try:
                        long(change_num)
                        if (len(change_num)!=10):
                            print("Contact number should be 10 digits")
                        else:
                            del dict_list[name_inp.upper()]
                            dict_list[change_name.upper()] = change_num
                            filename = "phonebook.csv"
                            f = open(filename, "wb")
                            f.close()
                            with open('phonebook.csv', 'wb') as csv_file:
                                writer = csv.writer(csv_file)
                                for key, value in dict_list.items():
                                    writer.writerow([key, value])
                            print("Contact Modified")
                    except ValueError:
                        print("Contact should be a number")
            cont = raw_input("Press y to modify contact. Any Other Key to goto Main Menu: ")
            if cont.upper() != "Y":
                break
            os.system('cls')
        else:
            print("No Records Found")
            raw_input("Press Any Key to goto Main Menu: ")
            break
def ClrCont():
    if os.path.getsize('phonebook.csv') > 0:
        with open('phonebook.csv', 'rb') as fp:
            reader = csv.reader(fp)
            for row in reader:
                print(" ".join(row))
        print("Warning! This will erase all your Contacts. Restore Not Possible")
        resp = raw_input("Click y to proceed.Any Other Key to Cancel: ")
        if resp.upper() == "Y":
            filename = "phonebook.csv"
            f = open(filename, "wb")
            f.close() 
            print("All contacts Deleted")
        else:
            print("Action Aborted")
        raw_input("Press Any Key to goto Main Menu: ")
    else:
        print("No Records Found")
        raw_input("Press Any Key to goto Main Menu: ")

def createFile():
	try:
		fr = open('phonebook.csv','rb')
		fr.close()
	except:
		fw = open('phonebook.csv','wb')
		fw.close()
		
os.system('cls')
print("Hello User! Welcome to Phone Book\n") 
raw_input("Press Any Key to goto Main Menu: ")

while(1):
	createFile()
	os.system('cls')
	print("1.View Phone Book")
	print("2.Add Contact")
	print("3.Delete Contact")
	print("4.Modify")
	print("5.Clear All Contacts")
	print("6.Exit")
	inp = raw_input("Select your Option: ")
	os.system('cls')
	takeaction = {
			"1": viewPhone,
			"2": AddCont,
			"3": DelCont,
			"4": ModCont,
			"5": ClrCont,
			"6": term
		}
	takeaction.get(inp,errhandler)()
	if t:
		print('{:*^30}'.format('Thank You'))
		break
    
        