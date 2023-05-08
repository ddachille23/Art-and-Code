# emergence assignment
# import our helper code
from agent_helper import *
import time

def setup():
    global zone_1_2_walkers, zone_1_4_walkers, zone_1_5_walkers, \
           zone_2_1_walkers, zone_3_attractors, zone_3_2_walkers, \
           zone_4_attractors, zone_2_attractors, zone_5_attractors, \
           zone_1_attractors, zone_4_1_walkers, zone_5_1_walkers, cars_3_attractors, \
           zone_2_3_walkers, zone_4_5_walkers, zone_5_4_walkers, cars_1_3, \
           wall_list, walking_sign, last_update, flip_attractor, light_counter, \
           time_remaining, WALK_DURATION

    size(600, 870)
    
    WALK_DURATION = 20 # seconds
    walking_sign = False
    flip_attractor = False
    light_counter = 0
    time_remaining = 0
    
    # Initialize the last update time
    last_update = time.time()
    
    
    # sometimes improves graphics
    pixelDensity(2)   
    
    # cars get complicated --> can add in a future project
    # # driving cars
    # cars_1_3 = []
    # for i in range(5):
    #     car_1_3 = Agent(x=random(0,50),
    #                 y=random(500,640), 
    #                 draw=draw_car,
    #                 car_height = 30,
    #                 car_width = 15,
    #                 max_speed=1
    #                 ) 
    #     cars_1_3.append(car_1_3)  
    #     car_1_3.bump(60, 2)  
        
    # # car attractors
    # ## road zone 3 attractors
    # cars_3_attractors = []
    # for i in range(5):
    #     cars_3_attractor = Agent(x=599,
    #                 y=random(200,300), 
    #                 draw=draw_car,
    #                 car_height = 1,
    #                 car_width = 1,
    #                 max_speed=0
    #                 ) 
    #     cars_3_attractors.append(cars_3_attractor) 
        
      
    # zone 1 walkers 
    ## zone 1 to 2 walkers
    zone_1_2_walkers = []
    for i in range(40):
        zone_1_2_walker = Agent(x=random(210,380),
                    y=random(600,750), 
                    draw=draw_walker,
                    size=10,
                    max_speed=1.2
                    ) 
        zone_1_2_walkers.append(zone_1_2_walker)
        
        # bump zone_1_2_walker in random direction
        #zone_1_2_walker.bump(random(360), random(0.5))
    
    ## zone 1 to 4 walkers
    zone_1_4_walkers = []
    for i in range(40):
        zone_1_4_walker = Agent(x=random(210, 380), 
                    y=random(600,750), 
                    draw=draw_walker,
                    size=10,
                    max_speed=1.4
                    ) 
        zone_1_4_walkers.append(zone_1_4_walker)
        
        # bump zone_1_2_walker in random direction
        #zone_1_4_walker.bump(random(360), random(0.5))
        
    ## zone 1 to 5 walkers
    zone_1_5_walkers = []
    for i in range(20):
        zone_1_5_walker = Agent(x=random(210, 380), 
                    y=random(600,750), 
                    draw=draw_walker,
                    size=10,
                    max_speed=1.2
                    ) 
        zone_1_5_walkers.append(zone_1_5_walker)
        
        # bump zone_1_2_walker in random direction
        #zone_1_5_walker.bump(random(360), random(0.5))
    
    # zone 2 walkers
    ## zone 2 to 1 walkers
    zone_2_1_walkers = []
    for i in range(40):
        zone_2_1_walker = Agent(x=random(-5,50),
                    y=random(270,410), 
                    draw=draw_walker,
                    size=10,
                    max_speed=1.2
                    ) 
        zone_2_1_walkers.append(zone_2_1_walker)
    # zone 2 to 3 walkers
    zone_2_3_walkers = []
    for i in range(40):
        zone_2_3_walker = Agent(x=random(-5,50),
                    y=random(270,410), 
                    draw=draw_walker,
                    size=10,
                    max_speed=1.2
                    ) 
        zone_2_3_walkers.append(zone_2_3_walker)
    
    # zone 3 walkers
    ## zone 3 to 2 walkers
    zone_3_2_walkers = []
    for i in range(40):
        zone_3_2_walker = Agent(x=random(100,220),
                    y=random(5,140), # 130, 30
                    draw=draw_walker,
                    size=10,
                    max_speed=1.2
                    ) 
        zone_3_2_walkers.append(zone_3_2_walker)
    
    # zone 4 walkers
    ## zone 4 to 1 walkers
    zone_4_1_walkers = []
    for i in range(40):
        zone_4_1_walker = Agent(x=random(320,525),
                    y=random(80,230), 
                    draw=draw_walker,
                    size=10,
                    max_speed=1.4
                    ) 
        zone_4_1_walkers.append(zone_4_1_walker)
    ## zone 4 to 5 walkers
    zone_4_5_walkers = []
    for i in range(40):
        zone_4_5_walker = Agent(x=random(320,525),
                    y=random(80,230), 
                    draw=draw_walker,
                    size=10,
                    max_speed=1.2
                    ) 
        zone_4_5_walkers.append(zone_4_5_walker)
    
    # zone 5 walkers
    ## zone 5 to 1 walkers
    zone_5_1_walkers = []
    for i in range(40):
        zone_5_1_walker = Agent(x=random(480,width),
                    y=random(420,550), 
                    draw=draw_walker,
                    size=10,
                    max_speed=1
                    ) 
        zone_5_1_walkers.append(zone_5_1_walker)
    ## zone 5 to 4 walkers
    zone_5_4_walkers = []
    for i in range(40):
        zone_5_4_walker = Agent(x=random(480,width),
                    y=random(420,550), 
                    draw=draw_walker,
                    size=10,
                    max_speed=1
                    ) 
        zone_5_4_walkers.append(zone_5_4_walker)
        
    # zone 1 attractors
    zone_1_attractors = []
    for i in range(0,80, 2):
        zone_1_attractor = Agent(x = 160+random(i+180), y = 630+random(i+150),
                                  draw = draw_walker,
                                  size = 10,
                                  max_speed = 0)
        zone_1_attractors.append(zone_1_attractor)
        
        
    # zone 2 attractors
    zone_2_attractors = []
    for i in range(0,80, 2):
        zone_2_attractor = Agent(x = -5+random(i+20), y = 300+random(i+20),
                                  draw = draw_walker,
                                  size = 10,
                                  max_speed = 0)
        zone_2_attractors.append(zone_2_attractor)
    
    # zone 3 attractors
    zone_3_attractors = []
    for i in range(0,120, 3):
        zone_3_attractor = Agent(x = 130+random(i+20), y = 30+random(i+20),
                                  draw = draw_walker,
                                  size = 10,
                                  max_speed = 0)
        zone_3_attractors.append(zone_3_attractor)
    
    # zone 4 attractors
    zone_4_attractors = []
    for i in range(0,200, 5):
        zone_4_attractor = Agent(x = 315+random(i), y = 60+random(i),
                                  draw = draw_walker,
                                  size = 10,
                                  max_speed = 0)
        zone_4_attractors.append(zone_4_attractor)
        
    # zone 5 attractors
    zone_5_attractors = []
    for i in range(0,200, 5):
        zone_5_attractor = Agent(x = 475+random(i), y = 420+random(i),
                                  draw = draw_walker,
                                  size = 10,
                                  max_speed = 0)
        zone_5_attractors.append(zone_5_attractor)
        

    # walls
    wall_list = []
    for i in range(1):
        wall = Wall(random(width), random(height),
                    random(width), random(height),
                    thickness = random(1,20))
        wall_list.append(wall)

def draw():
    global zone_1_2_walkers, zone_1_4_walkers, zone_1_5_walkers, \
           zone_2_1_walkers, zone_4_1_walkers, zone_5_1_walkers, \
           zone_4_attractors, zone_2_attractors, zone_5_attractors, \
           zone_1_attractors, zone_3_attractors, zone_3_2_walkers, cars_3_attractors, \
           zone_2_3_walkers, zone_4_5_walkers, zone_5_4_walkers, cars_1_3, \
           wall_list, walking_sign, last_update, flip_attractor, light_counter, \
           time_remaining, WALK_DURATION

    background(248,248,248)
    fill(0)
    textSize(8)
        
    # Get the current time
    current_time = time.time()
    
    # Check if X seconds have passed since the last update
    if current_time - last_update >= WALK_DURATION:
        # Flip the walking sign value
        walking_sign = not walking_sign
        light_counter+=1 # keep track of the number of light switches
        if light_counter % 2 == 0: # every other time flip the attractor
            flip_attractor = not flip_attractor
        
        # Update the last update time
        last_update = current_time
        
    time_remaining = WALK_DURATION - (current_time - last_update)
        
   
    #draw_attractors() # for testing
    
    draw_walking_sign(walking_sign)
    draw_crosswalk(walking_sign)
    fill(0)
    draw_walkers()
    
    # cars get complicated --> can add in a future project
    # # draw cars_1_3
    # ## draw 1 --> 4 walkers
    # counter_car_1_3 = 0
    # for car_1_3 in cars_1_3:
    #     car_1_3.draw()
    #     if walking_sign == False:
    #         car_1_3.move()
    #         car_1_3.seek(cars_3_attractors[counter_car_1_3], 900, 0.9)
    #         # if flip_attractor == True:
    #         #     zone_1_4_walker.seek(zone_1_attractors[counter_1_4], 800, 0.8)
    #         # else:
    #         #     zone_1_4_walker.seek(zone_4_attractors[counter_1_4], 800, 0.8)
    #         counter_car_1_3+=1
    
def draw_attractors():
    for zone_1_attractor in zone_1_attractors:
        zone_1_attractor.draw()
    for zone_2_attractor in zone_2_attractors:
        zone_2_attractor.draw()
    for zone_3_attractor in zone_3_attractors:
        zone_3_attractor.draw()
    for zone_4_attractor in zone_4_attractors:
        zone_4_attractor.draw()
    for zone_5_attractor in zone_5_attractors:
        zone_5_attractor.draw()
    # for cars_3_attractor in cars_3_attractors:
    #     cars_3_attractor.draw()
        
def draw_walkers():
    # zone 1 walkers
    ## draw 1 --> 2 walkers
    switch = False
    counter_1_2 = 0
    for zone_1_2_walker in zone_1_2_walkers:
        zone_1_2_walker.draw()
        if walking_sign == True:
            zone_1_2_walker.move()
            # send the walkers to the opposite side of the road
            if flip_attractor == True:
                zone_1_2_walker.seek(zone_1_attractors[counter_1_2], 600, 0.9)
            else:
                zone_1_2_walker.seek(zone_2_attractors[counter_1_2], 600, 0.9)
                # prevent them from shaking (this gets them stuck here)
                # if zone_1_2_walker.touching(zone_2_attractors[counter_1_2]):
                #     zone_1_2_walker.max_speed = 0
            counter_1_2+=1
    
    ## draw 1 --> 4 walkers
    counter_1_4 = 0
    for zone_1_4_walker in zone_1_4_walkers:
        zone_1_4_walker.draw()
        if walking_sign == True:
            zone_1_4_walker.move()
            if flip_attractor == True:
                zone_1_4_walker.seek(zone_1_attractors[counter_1_4], 800, 0.8)
            else:
                zone_1_4_walker.seek(zone_4_attractors[counter_1_4], 800, 0.8)
        counter_1_4+=1
        
    ## draw 1 --> 5 walkers
    counter_1_5 = 0
    for zone_1_5_walker in zone_1_5_walkers:
        zone_1_5_walker.draw()
        if walking_sign == True:
            zone_1_5_walker.move()
            if flip_attractor == True:
                zone_1_5_walker.seek(zone_1_attractors[counter_1_5], 800, 0.7)
            else:
                zone_1_5_walker.seek(zone_5_attractors[counter_1_5], 800, 0.7)
        counter_1_5+=1
        
    # zone 2 walkers
    ## draw 2 --> 1 walkers
    counter_2_1 = 0
    for zone_2_1_walker in zone_2_1_walkers:
        zone_2_1_walker.draw()
        if walking_sign == True:
            zone_2_1_walker.move()
            if flip_attractor == True:
                zone_2_1_walker.seek(zone_2_attractors[counter_2_1], 800, 0.8)
            else:
                zone_2_1_walker.seek(zone_1_attractors[counter_2_1], 800, 0.8)
        counter_2_1+=1
    ## draw 2 --> 3 walkers
    counter_2_3 = 0
    for zone_2_3_walker in zone_2_3_walkers:
        zone_2_3_walker.draw()
        if walking_sign == True:
            zone_2_3_walker.move()
            if flip_attractor == True:
                zone_2_3_walker.seek(zone_2_attractors[counter_2_3], 800, 0.8)
            else:
                zone_2_3_walker.seek(zone_3_attractors[counter_2_3], 800, 0.8)
        counter_2_3+=1
        
    # zone 3 walkers
    ## draw 3 --> 2 walkers
    counter_3_2 = 0
    for zone_3_2_walker in zone_3_2_walkers:
        zone_3_2_walker.draw()
        if walking_sign == True:
            zone_3_2_walker.move()
            if flip_attractor == True:
                zone_3_2_walker.seek(zone_3_attractors[counter_3_2], 800, 0.8)
            else:
                zone_3_2_walker.seek(zone_2_attractors[counter_3_2], 800, 0.8)
        counter_3_2+=1
        
    # zone 4 walkers
    ## draw 4 --> 1 walkers
    counter_4_1 = 0
    for zone_4_1_walker in zone_4_1_walkers:
        zone_4_1_walker.draw()
        if walking_sign == True:
            zone_4_1_walker.move()
            if flip_attractor == True:
                zone_4_1_walker.seek(zone_4_attractors[counter_4_1], 800, 0.8)
            else:
                zone_4_1_walker.seek(zone_1_attractors[counter_4_1], 800, 0.8)
        counter_4_1+=1
    ## draw 4 --> 5 walkers
    counter_4_5 = 0
    for zone_4_5_walker in zone_4_5_walkers:
        zone_4_5_walker.draw()
        if walking_sign == True:
            zone_4_5_walker.move()
            if flip_attractor == True:
                zone_4_5_walker.seek(zone_4_attractors[counter_4_5], 800, 0.8)
            else:
                zone_4_5_walker.seek(zone_5_attractors[counter_4_5], 800, 0.8)
        counter_4_5+=1
    
    # zone 5 walkers
    ## draw 5 --> 1 walkers
    counter_5_1 = 0
    for zone_5_1_walker in zone_5_1_walkers:
        zone_5_1_walker.draw()
        if walking_sign == True:
            zone_5_1_walker.move()
            if flip_attractor == True:
                zone_5_1_walker.seek(zone_5_attractors[counter_5_1], 800, 0.8)
            else:
                zone_5_1_walker.seek(zone_1_attractors[counter_5_1], 800, 0.8)
        counter_5_1+=1
    ## draw 5 --> 4 walkers
    counter_5_4 = 0
    for zone_5_4_walker in zone_5_4_walkers:
        zone_5_4_walker.draw()
        if walking_sign == True:
            zone_5_4_walker.move()
            if flip_attractor == True:
                zone_5_4_walker.seek(zone_5_attractors[counter_5_4], 800, 0.8)
            else:
                zone_5_4_walker.seek(zone_4_attractors[counter_5_4], 800, 0.8)
        counter_5_4+=1
    
def draw_walker(walker):
    fill(4, 73, 62)
    ellipse(walker.x, walker.y, 17, walker.size)
    fill(255)
    circle(walker.x, walker.y, 7)
    
def draw_car(car):
    fill(0,0,255)
    # pushMatrix()
    # rotate(radians(-35))
    # translate(-250, -100)
    rect(car.x, car.y, car.car_width, car.car_height)
    #popMatrix()
    
def draw_walking_sign(sign):
    global time_remaining, WALK_DURATION
    strokeWeight(2)
    
    # print time remaining
    #text(time_remaining, 150, height-40)
    
    if sign == True:
        # outside rectangle
        fill(0) # color black
        rect(28, 738, 84, 114)
                    
        # create light animation
        fill(0,255,0) # color green
        counter_sign = WALK_DURATION-2
        for i in range(0, 100, 10):
            if time_remaining <= counter_sign:
                fill(0)
            rect(31, 745+i, 5, 8, 2)
            rect(104, 745+i, 5, 8, 2)
            fill(0,255,0)
            counter_sign-=2
            
        # big inside rectangle
        rect(40, 750, 60, 90)
        # head
        circle(70,771, 15)
        
        # left arm
        pushMatrix()
        rotate(radians(15))
        translate(197,-40)
        rect(60,780,7,20)
        popMatrix()
        
        # right arm
        pushMatrix()
        rotate(radians(-15))
        translate(-188,-3)
        rect(60,780,7,20)
        popMatrix()
        
        # body
        rect(60,780,20,30)
        
        # right leg
        rect(72,810,8,20)
        # left leg
        rect(60,810,8,20)
        stroke(0)
        noFill()
    else:
        # outside rectangle
        fill(0) # color black
        rect(28, 738, 84, 114)
        
        # create light animation
        fill(255,0,0) # color red
        counter_sign = WALK_DURATION-2
        for i in range(0, 100, 10):
            if time_remaining <= counter_sign:
                fill(0)
            rect(31, 745+i, 5, 8, 2)
            rect(104, 745+i, 5, 8, 2)
            fill(255,0,0)
            counter_sign-=2
        
        fill(255,0,0)
        
        # big inside rectangle
        rect(40, 750, 60, 90)
        # head
        circle(70,771, 15)
        
        # left arm
        pushMatrix()
        rotate(radians(15))
        translate(197,-40)
        rect(60,780,7,20)
        popMatrix()
        
        # right arm
        pushMatrix()
        rotate(radians(-15))
        translate(-188,-3)
        rect(60,780,7,20)
        popMatrix()
        
        # body
        rect(60,780,20,30)
        
        # right leg
        rect(72,810,8,20)
        # left leg
        rect(60,810,8,20)
        stroke(0)
        noFill()
    

def draw_crosswalk(sign):
    noFill()
    strokeWeight(3)
    
    # bottom sidewalk edge
    strokeWeight(1.5)
    
    beginShape()
    curveVertex(width, height)
    curveVertex(width, height)
    curveVertex(309, 550)
    curveVertex(0, 720)
    curveVertex(0, 720)
    endShape()
    
    beginShape()
    curveVertex(width, height-10)
    curveVertex(width, height-10)
    curveVertex(309, 550-10)
    curveVertex(0, 720-10)
    curveVertex(0, 720-10)
    endShape()
    
    # right sidewalk edge
    strokeWeight(1.5)
    beginShape()
    curveVertex(width, 660)
    curveVertex(width, 660)
    curveVertex(439, 461)
    curveVertex(width, 337)
    curveVertex(width, 337)
    endShape()
    
    beginShape()
    curveVertex(width, 660+15)
    curveVertex(width, 660+15)
    curveVertex(439-15, 461)
    curveVertex(width, 337-15)
    curveVertex(width, 337-15)
    endShape()
    
    # top right sidewalk edge
    strokeWeight(1.5)
    beginShape()
    curveVertex(width, 182)
    curveVertex(width, 182)
    curveVertex(378, 324)
    curveVertex(277, 272)
    curveVertex(296, 164)
    curveVertex(279, 0)
    curveVertex(279, 0)
    endShape()
    
    beginShape()
    curveVertex(width, 182-10)
    curveVertex(width, 182-10)
    curveVertex(378, 324-10)
    curveVertex(277+10, 272)
    curveVertex(296+10, 164)
    curveVertex(279+10, 0)
    curveVertex(279+10, 0)
    endShape()
    
    # top left sidewalk edge
    strokeWeight(1.5)
    beginShape()
    curveVertex(251, 0)
    curveVertex(251, 0)
    curveVertex(265, 154)
    curveVertex(215, 242)
    curveVertex(8, 0)
    curveVertex(8, 0)
    endShape()
    
    beginShape()
    curveVertex(251-10, 0)
    curveVertex(251-10, 0)
    curveVertex(265-10, 154)
    curveVertex(215, 242-10)
    curveVertex(8+10, 0)
    curveVertex(8+10, 0)
    endShape()
    
    
    # left sidewalk edge
    beginShape()
    curveVertex(0, 195)
    curveVertex(0, 195)
    curveVertex(127, 367)
    curveVertex(0, 463)
    curveVertex(0, 463)
    endShape()
    
    beginShape()
    curveVertex(0, 195+10)
    curveVertex(0, 195+10)
    curveVertex(127-10, 367)
    curveVertex(0, 463-10)
    curveVertex(0, 463-10)
    endShape()
    
    if sign == True:
        fill(0,255,0)
    else:
        fill(255,0,0)
        
    # cross walk markings
    ## main crosswalk
    pushMatrix()
    rotate(radians(10))
    for i in range(0, 210, 10):
        rect(345,267+i, 90, 5)
    popMatrix()
    
    ## left crosswalk
    pushMatrix()
    rotate(radians(-33))
    #translate(-200, 20)
    for i in range(0, 170, 8):
        rect(-180,402+i, 70, 4)
    popMatrix()
    
    ## right crosswalk
    pushMatrix()
    rotate(radians(-33))
    #translate(-200, 20)
    for i in range(0, 90, 8):
        rect(165,491+i, 70, 4)
    popMatrix()
    
    ## bottom crosswalk
    pushMatrix()
    rotate(radians(50))
    #translate(-200, 20)
    for i in range(0, 84, 7):
        rect(670,-5+i, 70, 4)
    popMatrix()
    
    ## top crosswalk
    pushMatrix()
    rotate(radians(50))
    for i in range(0, 115, 7):
        rect(240,2+i, 70, 4)
    popMatrix()
    
    
    
    
    
    

    
