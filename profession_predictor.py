'''
This is a fun game that based on your name, predicts your future profession
We'll use it to illustrate if statements, and we will use the ord() function
'''

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

if adjective_code == 0:
    adjective = "awesome"
elif adjective_code == 1:
    adjective = "mediocre"
elif adjective_code ==2:
    adjective = "average"
elif adjective_code == 3:
    adjective = "good"
else:
    adjective = "awful"

#based on last name, assign a profession

ln_unicode_sum = 0
for curr_let in lastName:
    ln_unicode_sum += ord(curr_let)

prof_code = ln_unicode_sum % 5

if prof_code == 0:
    profession = "professor"
elif prof_code == 1:
    profession = "funeral director"
elif prof_code == 2:
    profession = "dentist"
elif prof_code == 3:
    profession = "stand up comedian"
else:
    profession = "programmer"

#inform user of future profession
print("The Hawkeye profession predictor says that " + firstName + " " + lastName + " will be a " + adjective + " " + profession)
