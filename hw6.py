'''
This program uses dictionaries to obtain information about a particular
state or geography. It opens and reads the lines of a file and then assigns a
higher dictionary with the FIPS codes as keys and states' dictionaryes with their
information as the value. It takes user input for a FIPS key and then returns all
three pieces of information about the state/geography. If the user enters nothing,
it will thank them and exit. If the key isn't in the dictionary, it will prompt
them again and explain the instructions.
'''

#Author: Katie Blasi

fips_file = open("fips.txt")

#read content into list of lines (returns list of strings that are 1 line in the file)
fips_file_records = fips_file.readlines()


#read first line with metadata (string of first line with headers)
metadata_line = fips_file_records[0]
#remove the \n from the end
metadata_line = metadata_line.strip('\n')

#list of strings with the headers in the first line
metadata_items = metadata_line.split("|")

#create dictionary of state records (High level dictionary)
high_dict = {}

#goes through a different state/geography
for line_index in range(1, len(fips_file_records)):
    #create dictionary to keep track of states info
    state_dict = {}
    
    #split the record about a state/geography into a list
    record_list = fips_file_records[line_index].split("|")
    #remove the \n from the last element
    record_list[-1] = record_list[-1].strip('\n')
    

    #get the name of the state/geography
    fips_codes = record_list[0]
    
    #this iterates through each information of a state/geography
    for index in range(1, len(record_list)):
        #add the values to the inside dictionary
        state_dict[(metadata_items[index])] = (record_list[index])
        
    #add the record to the high level dictionary
    high_dict[fips_codes] = state_dict


#make it interactive with user input
#Welcome statement with instructions
print("Please enter a FIPS code in range of 01 to 78 to retrieve information about that state/geography")
print("Press enter to exit")

#set up boolean statement
entering_fips = True

#iterate through conditions
while entering_fips:
    #ask user for input
    user_input = input("Enter in FIPS code: ")
    
    #if user enters nothing, exit loop
    if user_input == '':
        print("Thank you for using our service")
        entering_fips = False
    
    #if input not a key in the dictionary tell them and ask again    
    elif not(user_input in high_dict):
        print("This code is not in the dictionary, try again")
    
    #otherwise, it's in dictionary and give them all the information about the state/geography
    else:
        print("You've entered the state of " + str(high_dict[user_input]['STATE_NAME']))
        print("The STUSAB for this state is " + str(high_dict[user_input]['STUSAB']))
        print("The STATENS for this state are " + str(high_dict[user_input]['STATENS']))
        
#close the file
fips_file.close()