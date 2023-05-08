# animation in class

# processing will call setup no matter what
# the function is an event handler
def setup():
    global x, y, vx, vy, diameter
    size(400,400)
    x = 200
    y = 200
    vx = -1
    vy = 1.2
    diameter = 30
    frameRate(120)

# draw is also an event handler
def draw():
    background(255)
    global x, y, vx, vy, diameter
    
    print(frameCount % 100)
        
    circle(x,y,diameter)
    square(x,y,diameter)
    x += vx
    y -= vy   
    
    if x > width - diameter/2:
        vx *= -1
    elif x < 15: 
        vx *= -1
    
    if y > height - diameter:
        vy *= -1
    elif y < diameter/2:
        vy *= -1
    
    if frameCount % 100 == 0:
        fill(random(255), random(255), random(255))
        diameter += 10
    
    
    # if frameCount > 250:
    #     square(width/2, height/2,30)
        
    
