#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #:     w0402993
#Student Name:  Andrew Beaver

def main():
    #Establish usage rate variables
    usageLevelOne = 20
    usageLevelTwo = 0.105
    usageLevelThree = 0.11
    usageLevelFour = 118

    #Display welcome message
    print("Erewhon Mobile Data Plans")

    #Prompt user for their data usage
    usage = float(input("\nEnter data usage (Mb): "))

    #Establish statements to get the rate for each total data usage category
    if usage <= 200:
        usageRate = usageLevelOne
    elif usage > 200 and usage <= 500:
        usageRate = usage * usageLevelTwo
    elif usage > 500 and usage <= 1024:
        usageRate = usage * usageLevelThree
    else:
        usageRate = usageLevelFour

    #Display the data fee to the user
    print("\nTotal charge is ${0:.2f}".format(usageRate)) 

main()