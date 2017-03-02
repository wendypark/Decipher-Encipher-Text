input1=input("Enter your message: ")    #user input of string
plain=input1                            #reassign variable

firsthalf = ""                          #initializing the firsthalf variable 
secondhalf = ""                         #initializing the secondhalf variable 
placeholder = 0                         #starting at place 0 of string, which is the first character

for c in plain:                         #forloop for string 
    if placeholder % 2 == 0:            #determines if index place is even
        firsthalf = firsthalf + c       #adds character to variable firsthalf (counter)
    else:
        secondhalf = secondhalf + c     #if index place is not even (odd) then adds characters to variable secondhalf
    placeholder = placeholder + 1       #counter for index place

cipher= firsthalf + secondhalf          #concantenates the first half and second half of the enciphered message

print('plain = "%s"; cipher = "%s"' %(plain,cipher))   #formatted in print form 




    




