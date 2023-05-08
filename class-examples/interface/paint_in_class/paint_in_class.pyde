def setup():
    global brush
    size(500,500)
    background(255)
    brush = "red_circle"
    
def draw():
    global brush
    
    # draw the buttons
    ## red button
    fill(255,0,0)
    square(10,10,30)
    
    ## green button
    fill(0,255,0)
    square(10,50,30)
    
    if mousePressed == True:
        noStroke()
        if brush == "red_circle":
            fill(255,0,0, 25)
            square(mouseX, mouseY, 50)
        elif brush == "green_square":
            fill(0,255,0, random(0,50))
            square(mouseX-25, mouseY-25, 50)

def mouseClicked():
    global brush
    
    # red button
    if mouseX > 10 and mouseX < 40 and mouseY > 10 and mouseY < 40:
        print("the red button was clicked")
        brush = "red_circle"
    
    # green button
    if mouseX > 10 and mouseX < 40 and mouseY > 50 and mouseY < 80:
        print("the green button was clicked")
        brush = "green_square"
        
