import turtle
def draw_circle():

    window=turtle.Screen()
    window.bgcolor("red")

    ebube=turtle.Turtle()
   #ebube.circle(50)
    ebube.speed(7)
    ebube.color("blue")
    ebube.shape("turtle")
    for i in range(1,13):
        
        ebube.circle(55)
        ebube.left(10)
    for i in range(1,13):
        ebube.circle(30)
        ebube.left(10)
        ebube.speed(1)

        



    
    window.exitonclick()





    
draw_circle()
