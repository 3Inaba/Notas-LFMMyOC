#These are some notes form the book of the same name.


'''
print('Hello world')

class Dog:

    def __init__(self, name, month, day, year, speakText):
     self.name = name
     self.month = month
     self.day = day
     self.year = year
     self.speakText = speakText    

    def speak(self):
       return self.speakText

    def getName(self):
       return self.name

    def birthDate(self):
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)

    def changeBark(self,bark):
        self.speakText = bark

    def __add__(self,otherDog):
        return Dog("Puppy of " + self.name + " and " + otherDog.name, \
            self.month, self.day, self.year + 1, \
            self.speakText + otherDog.speakText)


M= Dog('Miles', 3, 1, 2000, 'guauuuu')

M.speak()
M.birthDate()
print(M.__dict__)

print(M.speak())

L=Dog('Sof', 2, 5, 4000, 'unu')

ML=M+L
print(ML.__dict__, ML.speak())
'''




#turtle graphics is an acient drawing module

from turtle import *
t = Turtle()

print(t.__dict__)

'''
The safe way to
import the turtle module would be as follows.
import turtle
t = turtle.Turtle()
Listing 1.9 Module Import 
'''

filename = input("Please enter drawing filename: ")
screen = t.getscreen()

# The next line opens the file for "r" or reading. "w" would open it for
# writing, and "a" would open the file to append to it (i.e. add to the
# end). In this program we are only interested in reading the file.
file = open(filename, "r")

for line in file: 
    # The strip method strips off the newline character at the end of the line
    # and any blanks that might be at the beginning or end of the line.
    text=line.strip()
    commandList = text.split(",")
    command = commandList[0]

    if command == "goto":
        # Writing float(commandList[1]) makes a float object out of the
        # string found in commandList[1]. You can do similar conversion
        # between types for int objects.
        x = float(commandList[1])
        y = float(commandList[2])
        width = float(commandList[3])
        color = commandList[4].strip()
        t.width(width)
        t.pencolor(color)
        t.goto(x,y)
    
    elif command == 'circle':
        radius = float (commandList[1])
        width = float(commandList[2])
        color = commandList[3].strip()
        t.width(width)
        t.pencolor(color)
        t.circle(radius)

    elif command == 'beginfill':
        color = commandList[1].strip()
        t.fillcolor(color)
        t.begin_fill()

    elif command == 'endfill':
        t.end_fill()

    elif command == "penup":
        t.penup()

    elif command == "pendown":
        t.pendown()

    else: 
        print ("Unknown command found in file:" ,command)

file.close()

#hide the turtle we used to draw
t.ht()

screen.exitonclick()
print ("Program Execution Completed.")



