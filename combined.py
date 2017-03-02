
while True:                                              #infinite while loop, all statements true
    user_input=input("e to encrypt, d to decrypt: ")     #user input
    user_input=user_input.lower()                        #converts user input into lowercase letters                                                                                   
    #print(user_input)                                   #debugging use
    if user_input != 'e' and user_input != 'd':          #boolean statement for if user inputs letter other than e or d
        print("Please input the letter e to encript and d to decript your message.")   #prints personalized message
    
    else:                                           #if user inputs e or d, then follows through with else statements
        if  user_input=="e":                        #if user wants to encrypt
            user_input2=(input("Enter your message: "))
            firsthalf = ""                          #initializing the firsthalf variable 
            secondhalf = ""                         #initializing the firsthalf variable 
            placeholder = 0                         #starting at place 0 of string, which is the first character
            for c in user_input2:                   #for-loop in string user_input2
                if placeholder % 2 == 0:            #determines if index place is even
                    firsthalf = firsthalf + c       #adds character to variable firsthalf
                else:
                    secondhalf = secondhalf + c     #if index place is not even (odd) then adds characters to variable secondhalf
                placeholder = placeholder + 1       #counter for index place

            cipher= firsthalf + secondhalf          #concantenates the first half and second half of the enciphered message

            print('plain = "%s"; cipher = "%s"' %(user_input2,cipher))   #in print form
            break                                                        #breaks out of loop
        else:                                                      #for decrypting
            try:                                                   
                user_input3=(input("Enter your ciphertext: "))     #user input
                cipher_e=user_input3                               #reassigning variable user_input3 to cipher_e
            except KeyboardInterrupt:                              #exception handling
                print("You have killed the program!")              #instead of usual error message, prints my personalized message
            else:                                                    
                length_word=len(cipher_e)                          #gets the length of the cipher_e string (# of characters)
                midpoint=length_word//2                            #midpoint variable determines the halfpoint of the string
                if length_word%2==0:                               #if number of characters in input is even
                    deciphered_message=""                          #initializing variable deciphered_message
                    firsthalf_e=cipher_e[0:midpoint]               #defining firsthalf of deciphered message as starting from position 0 to halfpoint
                    secondhalf_e=cipher_e[midpoint:]               #defining secondhalf of deciphered message as starting from halfpoint to end of string
                    for c in range(midpoint):                      #goes through a for loop of each character position, endpoint is integer value of midpoint variable
                        deciphered_message=deciphered_message+firsthalf_e[c]+secondhalf_e[c]   #first character of firsthalf_e is added to first character of secondhalf_e, deciphered message is added first in order to initiate the concantenation
                    print('cipher = "%s"; plain = "%s"' %(cipher_e,deciphered_message))        #formatted print form
                    break                                                                      #breaks out of loop
                else:                                              #if number of characters in input is not even, (odd)
                    deciphered_message=""                          #initializing variable deciphered_message
                    firsthalf_e=cipher_e[0:midpoint+1]             #defining firsthalf of deciphered message as starting from position 0 to halfpoint+1 (+1 because the middle character goes with the firsthalf of the split string)
                    secondhalf_e=cipher_e[midpoint+1:]             #defining secondhalf of deciphered message as starting from halfpoint+1 to end of string    
                    for c in range(midpoint):                      #goes through a for loop of each character position, endpoint is integer value of midpoint variable
                        deciphered_message=deciphered_message+firsthalf_e[c]+secondhalf_e[c]  #first character of firsthalf_e is added to first character of secondhalf_e, deciphered message is added first in order to initiate the concantenation
                    deciphered_message=deciphered_message+firsthalf_e[-1]                     #adds the middle character of string, or the last character of first half to end of deciphered_message 
                    print('cipher = "%s"; plain = "%s"' %(cipher_e,deciphered_message))       #formatted print form
                    break                                                                     #breaks out of loop

                        

