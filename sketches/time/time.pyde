# casino carpet
def setup():
    size(800, 800)
    global time
    global base_carpet_source
    global bottom_left_moon_source
    global flower_pedal
    global middle_circle
    global swirly_circle
    global bottom_right_circle
    time = 0
    frameRate(60)
    
    # image loading
    base_carpet_source = loadImage("casino-carpet-edited.png")
    bottom_left_moon_source = loadImage("bottom-left-moon.png")
    flower_pedal = loadImage("flower-pedal.png")
    middle_circle = loadImage("middle-circle.png")
    swirly_circle = loadImage("swirly-circle.png")
    bottom_right_circle = loadImage("bottom-right-circle.png")
def draw():
    global time
    global base_carpet_source
    global bottom_left_moon_source
    global flower_pedal
    global middle_circle
    global swirly_circle
    global bottom_right_circle
    
    # base layer
    image(base_carpet_source, 0,0)
    
    # rotate swirly circle
    scale_factor = 0.8 + 0.2 * sin(millis() / 1600.0)
    push()
    translate(716,476)
    rotate(radians(change(360,0, 150)))
    image(swirly_circle, -716,-476, swirly_circle.width*scale_factor, swirly_circle.height*scale_factor)
    pop()
    
    # draw blue spinning balls top right
    time += 1/60.0
    strokeWeight(0.5)
    fill(20, 90, 100)
    num_small_circles = 50
    num_large_circles = 3
    circle_radius = 60
    for i in range(num_small_circles):
        angle = i * 2 * PI / num_small_circles
        x = width/2 + cos(time + i) * circle_radius
        y = height/2 + sin(time - i) * circle_radius 
        for j in range(0,num_large_circles*num_small_circles,num_small_circles): 
            ellipse(50+x+j, y-375, 10, 10)
    
    strokeWeight(0)
    stroke(208,144,46)
    fill(208,144,46)
    circle(width/2-2,height/2+29,345)
    
    # blue circle center-outside
    strokeWeight(0)
    stroke(70,80,157)
    fill(70,80,157)
    circle(width/2-2,height/2+29,320)
    
    # draw green spinning blue balls middle-outside
    time += 1/10000.0
    strokeWeight(8)
    stroke(33,40,29)
    fill(125,151,78)
    num_circles = 24
    circle_radius = 143
    for i in range(num_circles):
        angle = i * 2 * PI / num_circles
        x = width/2 + cos(time + angle) * swing(-circle_radius + 25, -circle_radius - 3, 24)
        y = height/2 + sin(time + angle) * swing(circle_radius - 25, circle_radius + 3, 24)
        ellipse(x, y+30, 23, 23)
    stroke(0)
    
    # rotate middle circle with teal pegs
    image(middle_circle, 0,0)
    ## rotation
    push()
    translate(398,430) # center point that it rotates around
    rotate(radians(change(360,0, 250)))
    image(middle_circle, -398,-430)
    pop()
    
    # draw red spinning blue balls middle
    time += 1/10000.0
    strokeWeight(2)
    fill(174,0,41)
    num_circles = 12
    circle_radius = 92
    for i in range(num_circles):
        angle = i * 2 * PI / num_circles
        x = width/2 + cos(time + angle) * circle_radius
        y = height/2 + sin(time + angle) * circle_radius
        ellipse(x, y+30, 23, 23)
        
    # draw middle circles
    strokeWeight(0)
    fill(170,51,110)
    circle(width/2-2,height/2+29,180)
    fill(174,0,41)
    strokeWeight(0)
    circle(width/2-2,height/2+29,145)
    strokeWeight(2)
    fill(174,0,41)
    
    # rotate center flower pedal
    #image(flower_pedal, 0,0)
    ## rotation
    push()
    translate(width/2,430) # center point that it rotates around
    rotate(radians(change(360,0, 200)))
    image(flower_pedal, -width/2,-430)
    pop()
    
    # rotate bottom left moon ball
    push()
    translate(214,628) # center point that it rotates around
    rotate(radians(change(360,0, 200)))
    image(bottom_left_moon_source, -214,-628)
    pop()
    
    # top left static circles
    # grey/blue outer
    noStroke()
    fill(46,46,52)
    ellipse(200, 20, 270, 265)
    fill(68,82,154)
    ellipse(200, 20, 190, 185)
    
    #fill(130,147,95)
    fill(swing(130,47,20), swing(147,45,20), swing(47,95,20))
    ellipse(200, 20, 145, 140)
    # fill(47,45,47)
    fill(swing(47,210,20), swing(45,147,20), swing(47,40,20))
    ellipse(200, 20, 105, 100)
    #fill(210,147,40)
    fill(swing(210,47,20), swing(147,45,20), swing(40,47,20))
    ellipse(200, 20, 60, 57)
    #fill(180,93,45)
    fill(swing(130,180,20), swing(147,93,20), swing(95,45,20))
    ellipse(200, 20, 30, 30)
    fill(204,55,59)
    ellipse(200, 20, 15, 15)
    
    noFill()
    strokeWeight(3)
    stroke(212,146,43)
    ellipse(200, 20, 240, 230)
    
    # draw red spinning yellow balls top
    time += 1/10000.0
    noStroke()
    fill(212,146,43)
    num_circles = 24
    circle_radius = 120
    for i in range(num_circles):
        angle = i * 2 * PI / num_circles
        x = width/2 + cos(time + angle) * circle_radius
        y = height/2 + sin(time + angle) * circle_radius
        ellipse(x-200, y-385, 20, 20)
    
    # solid bottom right circle
    fill(212,146,43)
    circle(766, 618, 150)
    fill(68,82,154, change(50, 255, 30))
    circle(766, 618, 100)
    fill(180,93,45,change(50, 255, 30))
    circle(766, 618, 50)
    fill(204,55,59, change(50, 255, 60))
    circle(766, 618, 25)
    
    # rotate bottom right circle
    push()
    translate(766-60,618)
    rotate(radians(change(0,360, 210)))
    image(bottom_right_circle, -766-60,-618)
    pop()
    
    # reset stroke
    stroke(1)
def swing(start, stop, duration, offset=0): 
    position = sin(2 * PI * change(0, 1, duration * 2, offset)) * .5 + .5
    return (position * (stop - start)) + start 
    
def change(start, stop, duration, offset=0):
    return map((frameCount + offset) % duration, 0, duration, start, stop)

    
    
