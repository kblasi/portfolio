'''
Dictionaries - data structure
- similar to has tables in other languages
- a container with sets of keys associated with values
- keys are user defined as opposed to the indices used with lists or tuples
unique value as the key, keys can't be repeated. Value associated with key
'''
#oscar_winners = {2007: 'The Departed', 2008: 'No Country for Old Men', 2009: 'Slumdog Millionaire', 2010: 'The Hurt Locker'}

#to call one by the value use >>> oscar_winners[2008]
#this returns 'No Country for Old Men'

'''
- keys can be of any time as long as it is an immutable type (integers, strings, or tuples)
- index opporator = put the key in
- length function still works, gives the # of key/value pairs
'''

# put this in shell and it adds it to the dictionary: oscar_winner[2011] = "The King's Speech"

#length for dictionaries: gives you the number of keys you have in it
#can't use +, *, or slicing
#in can be used to check if an object is in the dictionary

'''
dictionary methods
update() : updates key/value pairs (may mean overwrite or add)
example: my_update = {2012: "The artst', 2013: "Argo'}
oscar_winners.update(my_update)
^^^this adds in the new data that wasn't there before
'''

#keys() method
#gives you a list of the key values

#values() method
#gives list of the values at all the keys

#items() method
#returns list of key/values pairs as tuples

#get() method
#returns value at what's in get

#pop() method (used in lists as well)
#returns the value associated with the key and removes the key/value pair

'''
Using dictionaries as switch/case statements
-What if you have a really long statement with many branches?
-In othere languages, there are switch/case statements (C and Java)
------not in python but other languages
            switch{code}
                case 0:
                
                case 1:
------this is the equivalent to an if, elif statement

'''
#using old code, switch it to the switch/case statement

def profession_predictor():
    #greet user
    print("Welcome to the Hawkeye profession predictor.")
    
    #ask user for first name
    firstName = input("Enter your first name: ")
    
    #ask user for last name
    lastName = input("Enter your last name: ")
    
    #based on first name, assign an adjective for how well they'll do in the job.
    #we'll only use the first letter
    #ord finds the unicode for the first letter
    fn_unicode_sum = 0
    for curr_letter in firstName:
        fn_unicode_sum += ord(curr_letter)
        
    adjective_code = fn_unicode_sum % 5
    
    #set mapping between adjective codes and adjectives
    #can do spacing this way or in the long one line way
    adjective_dict = {0: "awful",
                      1: "mediocre",
                      2: "average",
                      3: "good",
                      4: "awesome"}
    
    adjective = adjective_dict[adjective_code]
    
    #based on last name, assign a profession
    
    ln_unicode_sum = 0
    for curr_let in lastName:
        ln_unicode_sum += ord(curr_let)
    
    prof_code = ln_unicode_sum % 5
    
    profession_dict = {0: "professor",
                      1: "funeral director",
                      2: "dentist",
                      3: "stand up comedian",
                      4: "programmer"}
    
    profession = profession_dict[prof_code]
    
    #inform user of future profession
    print("The Hawkeye profession predictor says that " + firstName + " " + lastName + " will be a " + adjective + " " + profession)
    


'''
Using dictionaries as counters: ex: counting how many times each item in a list occurs
'''
#ncaa winners counter
#this program opens a file with NCAA BB winners and counts how many times each school has won
def ncaa_winners():
    #open the file
    ncaa_file = open("ncaaw_bb_champs.csv")
    
    #read the lines
    winners_list = ncaa_file.readlines()
    
    #set up dictionary to count winners
    winners = {}
    
    #use dictionary to count number of wins per school
    for winner in winners_list:
        #[0] = year, [1] = school
        championship_list = winner.split(",")
        school = champtionship_list[1]
        
        if school in winners:
            #school has won before
            winners[school] +=1
        else:
            #this is the first time this school won
            winners[school] = 1
    
    #inform the user
    winners_count = winners.items()
    
    for win_count in winners_count:
        print(win_count[0] + " - " str(win_count[1]))