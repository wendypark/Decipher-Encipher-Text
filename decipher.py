
try:                                                        #exception handling
    cipher_e=input("Enter your ciphertext: ")               #ciphered text input
except KeyboardInterrupt:                                   #if user inputs control c, there will be a KeyboardInterrupt error
    print("You have killed the program!")                   #instead of error message, prints my personalized message
else:                                                       #if input is valid follow through with else statements                               
    length_word=len(cipher_e)                               #takes the length of the input and stores into length_word variable
    midpoint=length_word//2                                 #midpoint variable determines the halfpoint of the string

    if length_word%2==0:                                    #if number of characters in input is even
        deciphered_message=""                               #initializing variable deciphered_message
        firsthalf_e=cipher_e[0:midpoint]                    #defining firsthalf of deciphered message as starting from position 0 to halfpoint
        secondhalf_e=cipher_e[midpoint:]                    #defining secondhalf of deciphered message as starting from halfpoint to end of string
        for c in range(midpoint):                           #goes through a for loop of each character position, endpoint is integer value of midpoint variable
            deciphered_message=deciphered_message+firsthalf_e[c]+secondhalf_e[c]   #first character of firsthalf_e is added to first character of secondhalf_e, deciphered message is added first in order to initiate the concantenation
        print('cipher = "%s"; plain = "%s"' %(cipher_e,deciphered_message))        #formatted print form
    else:                                                                          #if number of characters in input is not even, meaning odd
        deciphered_message=""                                                      #initializing variable deciphered_message
        firsthalf_e=cipher_e[0:midpoint+1]                                         #defining firsthalf of deciphered message as starting from position 0 to halfpoint+1 (+1 because the middle character goes with the firsthalf of the split string)
        secondhalf_e=cipher_e[midpoint+1:]                                         #defining secondhalf of deciphered message as starting from halfpoint+1 to end of string    
        for c in range(midpoint):                                                  #goes through a for loop of each character position, endpoint is integer value of midpoint variable
            deciphered_message=deciphered_message+firsthalf_e[c]+secondhalf_e[c]   #first character of firsthalf_e is added to first character of secondhalf_e, deciphered message is added first in order to initiate the concantenation
        deciphered_message=deciphered_message+firsthalf_e[-1]                      #adds the middle character of string, or the last character of first half to end of deciphered_message
        print('cipher = "%s"; plain = "%s"' %(cipher_e,deciphered_message))        #formatted print form

