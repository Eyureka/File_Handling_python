'''
Created on 31-Jul-2018

@author: WIN7
'''
'''
try:
    flight_file=open("flight.txt","r")
    text=flight_file.read()
    print(text)
    flight_file.write(",Good Morning")
    flight_file.close()
except:
    print("Error occurred")
    if flight_file.closed:
        print("File is closed")
    else:
        print("File is open")
        '''
try:
    hello_file=open("flight.txt","w")
    text="Hello everyone! Welcome"
    hello_file.write(text)
except:
    print("Error occurred, not able to write to file")
finally:
    hello_file.close()
try:
    hello_file=open("flight.txt","r")
    text_from_file=hello_file.read()
    print(text_from_file)
except:
    print("Error Occurred, not able to read from file")
finally:
    hello_file.close()        
    
    
    