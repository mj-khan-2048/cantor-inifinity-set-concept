import requests
import string

v = True
while v:
    #Get length of constructed float
    while True:
        length = input("Enter Final Constructed Value Length [2-20]: ")

        if not length.isdigit() or (int(length) < 2 or int(length) > 20):
            print("Error: Input not accepted \n")
            continue
        else: 
            break

    #Pull true random numbers from random.org
    source = "https://www.random.org/decimal-fractions/?num=" + str(length) + "&dec=" + str(length) + "&col=1&base=10&format=plain&rnd=new"

    num = (requests.get(source).text).split()

    #Init final string
    fin = '0.'

    print("Random Generation Set: ")
    for i in range(int(length)):
        
        temp = num[i]
        
        #add +1 or -1 
        print(str('%2d' % (i+1)) + ": " + str(temp))

        temp2 = int(temp[i+2])

        if temp2 == 9:
            digit = temp2 - 1
        elif temp2 < 9:
            digit = temp2 + 1

        fin += str(digit)

    print("\nConstructed Value Based on Set:\n    " + fin)

    while True:
        proceed_status = input("Generate More? (y/n): ")
        
        print("")

        if proceed_status in ["y","Y","yes","Yes","YES"]:
            break
        elif proceed_status in ["n","N","no","No","NO"]:
            v = False
            break
        else:
            print("Error: Input not accepted\n")
            continue

