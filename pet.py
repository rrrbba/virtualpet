from graphics import *
import time
import random


#Global variables for pet's needs
hunger = 0
fatigue = 0 
stress = 0
day = 0

#Function that changes pet display image in response to its stats
def changePicture(win):
    global hunger
    global fatigue
    global stress

    #Coords for pet image display in the window
    imgCenter = Point(162,180)

    default = Image(imgCenter, "default.gif")
    mild = Image(imgCenter, "mild.gif")
    spicy = Image(imgCenter, "spicy.gif")
    thaihot = Image(imgCenter, "thaihot.gif")
    death = Image(imgCenter, "gameOver.gif")

    #Update the display file to the pet's status
    if hunger > 99 or fatigue > 99 or stress > 99:
        Image.draw(death, win)
    elif hunger > 74 or fatigue > 74 or stress > 74:
        Image.draw(thaihot,win)
    elif hunger > 49 or fatigue > 49 or stress > 49:
        Image.draw(spicy, win)
    elif hunger > 24 or fatigue > 24 or stress > 24:
        Image.draw(mild, win)
    elif hunger > 0 or fatigue > 0 or stress > 0:
        Image.draw(default,win)

#Function registers a 'button' click to satisy a need. The 'button' is simulated by a user click in a bounded region of the window
def buttonPress(win):
    global hunger
    global fatigue
    global stress

    mouseClick = win.checkMouse()

    #If the user clicks a 'button' that day
    if mouseClick != None:
        #Eval the x-value to determine the user's input
        x = mouseClick.getX()

        #If the the x-value of the click coord. is in range of a button
        if 244.0 < x < 291.0:

            #Eval the y-value to determin which button was chosen
            y = mouseClick.getY()
            
            #These are the y-coord. of the three potential buttons
            #When a button is clicked, the corres. stat decreases by 10
            if 347.0 < y < 374.0:
                hunger -= 10
            elif 387.0 < y < 419.0:
                fatigue -= 10
            elif 427.0 < y < 454.0:
                stress -= 10

#Function that updates variables as the user runs the game. The updating variables are the day count and stat levels
def alive(win):

    global hunger
    global fatigue
    global stress
    global day
    
    day += 1

    #Random integers are added ontot each stat once a day
    addHunger = random.randint(1, 10)
    addFatigue = random.randint(1, 10)
    addStress =  random.randint(1, 10)

    hunger += addHunger
    fatigue += addFatigue
    stress += addStress

    buttonPress(win)



#Main control loop and creates GUI
def main():

    #Before opening the graphic window, introduce the game
    print()
    print("Welcome to Rayven's Little Pet Shop!")
    print("Press 'Enter' to continue.")

    enter1 = input()

    #Instuctions for the game
    print("The goal is to keep your pet alive and happy!")
    print("You must satisfy your pet's hunger, stress and fatigue.")
    print("These stats increase with each passing day")
    print("You can tend to one stat per day by pressing the corresponding button.")
    print("Press 'Enter' to contine.")

    enter2 = input()

    #Where the user inputs the name
    print("Please enter your new pet's name!")

    name = input()

    #Creates window witht the user's inputted pet name
    win = GraphWin("Rayven's Little Pet Shop", 320, 500)
    petName = Text(Point(160, 18), name)
    petName.draw(win)

    #Display the day number in the window
    dayCount = Text(Point(157, 37), "Day Number ")
    dayCount.draw(win)





    #wait for the user to click to exit the window
    win.getMouse()
main()