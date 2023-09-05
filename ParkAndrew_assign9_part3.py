"""
Assignment #9, Part 3
Andrew Park
"""

import ssl
import urllib.request
import turtle
image = input("Enter an image filename: ")
imurl = image+".txt"


# define a location for our file
url = ("https://cs.nyu.edu/~cardona/python/assignment9_image_data_files/"+imurl)
ssl_context = ssl._create_unverified_context()
# open a connection to the URL
try:
    response = urllib.request.urlopen(url, context=ssl_context)
    # read data from URL as a string
    data = response.read().decode('utf-8')
except:
    print("Sorry, '",imurl,"' doesn't exist",sep="")
else:
    print("Success! I was able to find '",imurl,"'",sep="")
    turt = turtle.Turtle()
    window = turtle.Screen()
    # Read from image1.txt
    f = data
    #split the data
    info = f.split(",")
    print(info)
    window.setup(width=int(info[0]),height=int(info[1]),)
    window.title("Image Parser")
    window.bgcolor(float(info[2]),float(info[2]),float(info[2]))
    turtle.penup()
    x = -250
    y = 250
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color("black")
    for i in info[4:]:
        if "b" in i:
            x = -250
            y = 200
            turtle.goto(x,y)
        else:
            turtle.fillcolor(float(i),float(i),float(i))
            turtle.begin_fill()
            for s in range(4):
                turtle.pendown()
                turtle.forward(int(info[3]))
                turtle.right(90)
                turtle.up()
                move = 12.5
                x += move
                
            turtle.goto(x,y)
            turtle.down()
            turtle.penup()
            turtle.end_fill()



    print("Prepared Screen with background color {}".format(info[2]))

    window.mainloop()



