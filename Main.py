import matplotlib.pyplot as plt #Importing the libraries used in the program
import numpy as np

fig, ax = plt.subplots(2) 
loop_val = 4

#Written by Nathan Tucker
def getInput(aX, aB, aC, aD):   #Function written by Logan Catanese
                                #Local @Params aX, aB, aC, aD, are all created in the main function and passed to the function call
    aX = int(input("Enter aX: ")) #Prompt the user to input a value for aX
    aB = int(input("Enter aB: ")) #Prompt the user to input a value for aB
    aC = int(input("Enter aC: ")) #Prompt the user to input a value for aC
    aD = int(input("Enter aD: ")) #Prompt the user to input a value for aD
 

#Written by Matthew Koresky
def checkVal(aX, aB, aC, aD):   #Function written by Logan Catanese
                                #Local @Params aX, aB, aC, and aD are all created in the main function and passed as arguments
                                #Code inside function written by Matthew Koresky
    if aX >= 10:
        print("Value is too big. Please enter a smaller number.") #Check if the value is greater than or equal to 10, reset aX to 0 if this is true
    if aB >= 10:
        print("Value is too big. Please enter a smaller number.")
    if aC >= 10:
        print("Value is too big. Please enter a smaller number.")
    if aD >= 10:
        print("Value is too big. Please enter a smaller number.")

    return aX, aB, aC, aD
def graph(aX, aB, aC, aD):  #Function created by Logan Catanese
                #Local @Param aX is the array
                #Some of the code was written by Christopher
    x_values = np.array([aX])
    loop_val = 4
    for i in range (loop_val - 1):
    #Increment the previous x-vcalue by 4 and add it to the numpy array
        aX += 4

        x_values = np.append(x_values, aX) #Append the new x-value to the array 
    weekly_things = int()
    daily_things = int()
    #declareing var
    y_values = [0, 0, 0, 0] #whatever number of cells we decide on
    #filling the list
    for index in range(0, len(y_values)): #line 4
      for i in range(1, 2):  #can change this if 5 inputs is too annoying
        daily_things = int(input("Enter total things collected today:  ")) #could remove the question
        weekly_things = weekly_things + daily_things
  #end loop
      print("Total things collected this week:  ", weekly_things)  #text just here to help the user keep track, could remove
      y_values [index] = weekly_things
      weekly_things = 0

    print(y_values) #use (y-axis) as instead of var, and this will become the array the graph uses
     #Create the y_values for the graph which remain the same

    ax[0].plot(x_values, y_values, linestyle='--', marker='+', color='b', label='Graph with matplotlib for ITCS-1140') #Plotting the values with a marker "+" and a color of blue
    ax[1].plot([aX, aB, aC, aD], y_values)
#plt.figure
    plt.legend(loc='best') #Set the location of the plot to best
    plt.show()  #Show the plot

def main(): #Function created by Logan Catanese
    aX = int()  #Values localm to this function that are passed to the function calls
    aB = int()
    aC = int()
    aD = int()
    getInput(aX, aB, aC, aD)
    checkVal(aX, aB, aC, aD)
    graph(aX, aB, aC, aD)
main()