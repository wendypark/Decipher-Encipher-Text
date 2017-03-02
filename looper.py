while True:                                                             #infinite while loop
    try:                 
        user_input=input("e to encrypt, d to decrypt, q to quit: ")     #user input
        user_input=user_input.lower()                                   #converts user input into lower case letters       
        #print(user_input)                                              #debugging purpose
    except KeyboardInterrupt:                                           #exception handling for control c
        print ("You have quit the program!")                            #prints personalized message
        break                                                           #breaks out of while loop
    if user_input=='q':                                                 #if user inputs q
        break                                                           #quits the program
    else:                                                            
        if user_input != 'e' and user_input != 'd' and user_input != 'q':                 #if user doesn't input write letter
            print("Please input the letter e to encrypt, d to decrypt, and q to quit.")   #prints personalized message and runs until the user does
        else:                                           #if user does input one of the correct letters...goes through with following statements
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
                    else:                                              #if number of characters in input is not even, (odd)
                        deciphered_message=""                          #initializing variable deciphered_message
                        firsthalf_e=cipher_e[0:midpoint+1]             #defining firsthalf of deciphered message as starting from position 0 to halfpoint+1 (+1 because the middle character goes with the firsthalf of the split string)
                        secondhalf_e=cipher_e[midpoint+1:]             #defining secondhalf of deciphered message as starting from halfpoint+1 to end of string    
                        for c in range(midpoint):                      #goes through a for loop of each character position, endpoint is integer value of midpoint variable
                            deciphered_message=deciphered_message+firsthalf_e[c]+secondhalf_e[c]  #first character of firsthalf_e is added to first character of secondhalf_e, deciphered message is added first in order to initiate the concantenation
                        deciphered_message=deciphered_message+firsthalf_e[-1]                     #adds the middle character of string, or the last character of first half to end of deciphered_message 
                        print('cipher = "%s"; plain = "%s"' %(cipher_e,deciphered_message))       #formatted print form
        

                            


