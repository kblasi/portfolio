#function that returns hawkID in a list
def getHawkIDs():
    return ["kblasi"]

#helper function
#this function gives the index of the string's character
def getIndex(alpha, char):
    #start index at zero
    index = 0
    #iterate through the string while index in range
    while index < len(alpha):
        #when we find the correct character, return its index
        if char == alpha[index]:
            return index
        #if it's not it, add one and move on to the next index to check
        else:
            index+=1
    #return if something is wrong
    return "value not found"

#the shift cipher encryption
#make sure it's between 0 and 31 inclusive
#make sure the order of the characters is as follows
#"abcdefghijklmnopqrstuvwxyz ';.?,"
#example: shiftEncryt("apple", 3) should return "dssoh"
#10 Points
def shiftEncrypt(plainText, shift):
    #new empty cipher content string
    cipherstr = ""
    #string with allowed letters in it
    alpha = "abcdefghijklmnopqrstuvwxyz ';.?,"
    
    #iterate through the plain text
    for i in range(len(plainText)):
        #plain text character must be in alpha
        if plainText[i] in alpha:
            #get index of the character within alpha
            wordIndex = getIndex(alpha, plainText[i])
            #make sure the string is connected at both ends to go through
            Index = wordIndex%32
            #new index is original plus the shift
            cipherIndex = Index + shift
            #make sure if near the end, goes back to the beginning
            correctIndex = cipherIndex%32
            #add alpha at the correct index into the cipher string
            cipherstr+=alpha[correctIndex]
        #if character in plain text, not in alpha, add to the string
        else:
            cipherstr+=plainText[i]
    #return the string        
    return cipherstr
            

#the shift cipher decryption
#assume value of shift between 0 and 31 inclusive
#make sure the order of the characters is as follows
#"abcdefghijklmnopqrstuvwxyz ';.?,"
#example: shiftDecrypt("dssah", 3) should return "apple"
#10 Points
def shiftDecrypt(plainText, shift):
    #make empty decryption string
    decrypstr = ""
    #original alpha string
    alpha = "abcdefghijklmnopqrstuvwxyz ';.?,"
    
    #iterate through the plain text
    for i in range(len(plainText)):
        #if the character is in alpha
        if plainText[i] in alpha:
            #find the index of the plain text letter
            crpIndex = getIndex(alpha, plainText[i])
            #go to beginning if we reach the end
            Index = crpIndex%32
            #subtract the original shift from last problem
            cipherShift = Index - shift
            #go to the beginning if close to the end
            correctIndex = cipherShift%32
            #add alpha at the corrected index to the decryption string
            decrypstr+=alpha[correctIndex]
        #if character isn't in alpha, add to string as is
        else:
            decrypstr+=plainText[i]
    #return the decryption string        
    return decrypstr


#takes string and returns a list seperating each character in the same order
#example: listFromString("hello") should return ['h','e','l','l','o']
#3 Points
def listFromString(aString):
    #new empty list to append to
    newlist=[]
    #iterate through the string
    for element in aString:
        #append each element to the list
        newlist.append(element)
    #return the list
    return newlist

def MultiAlphaCipher(theKeys, plainFile):
    #open the file with the keys in them to read
    fileName = theKeys
    outputFile=open(fileName,"r")
    #counter that will count the # of lines in order to move on to the next one
    countline = 0
    #each line in the file represents a shuffling of the characters and punctuation
    #that will be used as a key. create 3 variables, line0, line1, and line2 that
    #contain the 3 lines of text from the file theKeys
    #line0 should contain the first line in the file
    #line1 should contain the second line in the file
    #line2 should contain the third line in the file    
    for line in outputFile:
        #call first line line0
        if countline ==0:
            line0 = line
            #add to count line to go to next
            countline+=1
        #call 2nd line line1
        elif countline ==1:
            line1 = line
            #add to countline to go to next
            countline+=1
        #call 3rd line line2
        elif countline ==2:
            line2 = line
    #close the file
    outputFile.close()
    
    #use helper function from listFromString(aString) to create lists from
    #the three key strings
    #key0 should be list from line0
    #key1 should be list from line1
    #key2 should be list form line2    
    key0list = listFromString(line0)
    key0=[]
    #get rid of the "\n" in the line
    for item in range(len(key0list)-1):
        key0.append(key0list[item])
    
    key1list = listFromString(line1)
    key1=[]
    #get rid of the "\n" in the line
    for item in range(len(key1list)-1):
        key1.append(key1list[item])
        
    key2 = listFromString(line2)
    
    #open file with the plain text in it to read
    fileName2 = "plainFile.txt"
    outputFile2 = open(fileName2,"r")
    #empty string for file contents
    fileContents=""
    #iterate through file and add the items into the string
    for item in outputFile2:
        fileContents+=item
    
    #close the file
    outputFile2.close()
    
    #take the string with file contents in it and make it all lowercase letters
    fileContents = fileContents.lower()
    
    #create file to write to called "cipherText.txt"
    fileName3 = "cipherText.txt"
    outputFile3 = open("cipherText.txt","w")
    #empty string to put cipher text into
    cipher=""
    #string with correct letters/indices
    alpha = "abcdefghijklmnopqrstuvwxyz ';.?,"
    #counter to keep track of indices
    count=0
    #iterate through the string
    for i in range(len(fileContents)):
        #counter to go back to the first of the 3 keys when alternating
        rotateInd=count%3
        #what to do when the counter is 0
        if rotateInd ==0:
            #account for only characters that are in key0
            if fileContents[i] in key0:
                #get the index of i within key0
                help = getIndex(alpha, fileContents[i])
                #make sure that it rotates back to beginning
                newInd= (help)%32
                #new encrypted letter obtained in key 0 at the new index
                encrypLet = key0[newInd]
                #add letter to cipher string
                cipher+=encrypLet
                #add to counter to go to next
                count+=1
            #if character not in key 0 (ex. Numbers), just add to cipher string
            else:
                cipher+=fileContents[i]
                
        #what to do when counter is 1        
        if rotateInd ==1:
            #account for only characters in key1
            if fileContents[i] in key1:
                #get index of i with in key1
                help = getIndex(alpha, fileContents[i])
                #make sure that it starts oven when it gets to the end
                newInd= (help)%32
                #new encrypted letter obtained in key1 at the new index
                encrypLet = key1[newInd]
                #add letters to the cipher string
                cipher+=encrypLet
                #add to count to go to the next key
                count+=1
            #if character not in key1 (numbers) just add it as is to the string
            else:
                cipher+=fileContents[i]
                
        #what to do when counter is 2
        if rotateInd ==2:
            #accoutn only for characters in key2
            if fileContents[i] in key2:
                #get index of i within key2
                help = getIndex(alpha, fileContents[i])
                #account for end of the string
                newInd= (help)%32
                #new letter is in key2 at the new index
                encrypLet = key2[newInd]
                #add letter to the cipher string
                cipher+=encrypLet
                #add to count to go to next key
                count+=1
            #if character isn't in key2, add it as is to the cipher string
            else:
                cipher+=fileContents[i]
    
    #write the string to the designated file
    outputFile3.write(cipher)
    #close the file
    outputFile3.close()  
    

def MultiAlphaDecipher(theKeys, cipherFile):
    #open the sample keys file
    fileName4 = theKeys
    outputFile4 = open(fileName4,"r")
    #count the lines to know when to go to the next
    countline=0
    #iterate through the file
    for line in outputFile4:
        #on the first line, name it line0
        if countline==0:
            line0 = line
            countline+=1
        #on the 2nd line, name it line1
        elif countline==1:
            line1 = line
            countline+=1
        #on the 3rd line, name it line2
        elif countline==2:
            line2 = line
    #close the file
    outputFile4.close()
    
    #use list from string function to make key0 from line0
    key0list=listFromString(line0)
    key0=[]
    #delete the "\n" from the line
    for item in range(len(key0list)-1):
        key0.append(key0list[item])
                      
    #use listfromstring function to make key1 from line1
    key1list=listFromString(line1)
    key1=[]
    #delete the "\n" from the line
    for item in range(len(key1list)-1):
        key1.append(key1list[item])
    
    #use listfromstring funciton to make key2 from line2
    key2=listFromString(line2)
    
    #open file with the cipher text in it to read from
    fileName5 = "cipherText.txt"
    outputFile5 = open(fileName5,"r")
    #empty string to write its contents to
    cipherFileContents=""
    
    #iterate through the file
    for item in outputFile5:
        #add each item to the string
        cipherFileContents+=item
    #close the file
    outputFile5.close()
    
    #empty decipher string
    decipher=""
    #counter for indices
    count=0
    #string with correct letters/indices
    alpha = "abcdefghijklmnopqrstuvwxyz ';.?,"
    #iterate through cipherFileContents string
    for i in range(len(cipherFileContents)):
        #contine to go through each key depending on indice
        rotateInd=count%3
        #what to do when key0 is needed
        if rotateInd==0:
            #if the characters are in key0
            if cipherFileContents[i] in key0:
                #get the index of the character from key0
                help=getIndex(key0, cipherFileContents[i])
                #account for the end of the string
                newInd= (help)%32
                #get the decrypted letter using key0 at the correct indice
                decrypLet = alpha[newInd]
                #add the letteer to the decipher string
                decipher+=decrypLet
                #add to count to go to the next key
                count+=1
            #if the character isn't in key0 (ex: numbers)
            else:
                #add it to the string as it is
                decipher+=cipherFileContents[i]
                
        #what to do when key1 is needed
        if rotateInd==1:
            #if the cipher file content is in key1
            if cipherFileContents[i] in key1:
                #get the index of the character form key1
                help2= getIndex(key1, cipherFileContents[i])
                #account for the end of the string
                newInd = (help2)%32
                #get the decrypted letter by using key1 at the new indice
                decrypLet = alpha[newInd]
                #add the decrypted letter into the string
                decipher+=decrypLet
                #add to count to go to next key
                count+=1
            #if the character isn't in key1 (ex: numbers)
            else:
                #add it to the string as it is
                decipher+=cipherFileContents[i]
                
        #what to do when key2 is needed
        if rotateInd==2:
            #if the content is in key2
            if cipherFileContents[i] in key2:
                #get the index of the character within key2
                help3 = getIndex(key2, cipherFileContents[i])
                #account for the end of the string
                newInd = (help3)%32
                #the decrypted letter is at the new index within key2
                decrypLet = alpha[newInd]
                #add the decrypted letter to the decipher string
                decipher+=decrypLet
                #add to count to go to next key
                count+=1
            #if the character isn't in key2 (ex: numbers)
            else:
                #add it as is to the string
                decipher+=cipherFileContents[i]
    
    #open a file with designated name to write the deciphered text to
    outputFile6 = open("MyDecryptedText.txt","w+")
    #write the text to the file
    outputFile6.write(decipher)
    #close the file
    outputFile6.close()