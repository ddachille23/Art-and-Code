# animation in class 2

def setup():
    global x, y, direction
    size(600,600)
    background(255)
    
    x = width/2
    y = height/2
    direction = 0

def draw():
    global x, y, direction
    
    direction = int(random(4))
    
    if direction == 0:
        x += 10
    elif direction == 1: # left
        x -= 10
    elif direction == 2: # up
        y -= 10
    elif direction == 3: # down
        y += 10
    
    if x < 0:
        x = 0
    elif x > width:
        x = width
    if y < 0:
        y = 0
    elif y > height:
        y = height
    
    # every 100 frames
    if frameCount % 100 == 0:
        fill(random(255), random(255), random(255))
    
    square(x,y,10)
