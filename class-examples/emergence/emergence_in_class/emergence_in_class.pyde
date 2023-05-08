# emergence in class
from agent_helper import *

def setup():
    global pig_list
    global robot_list
    global truffle_list
    size(500,500)
    
    pig_list = []
    for i in range(10):
        pig = Agent(x = random(width),
                    y = random(height),
                    draw = draw_pig,
                    max_speed = 5,
                    size = 34,
                    oinkiness = 50)
        pig.bump(random(360), 1) # degree, speed
        pig_list.append(pig)
    
    robot_list = []
    for i in range(2):
        robot = Agent(x = random(width),
                      y = random(height),
                      draw = draw_robot,
                      size = 50,
                      max_speed = 3)
        robot.bump(random(360), 1.0)
        robot_list.append(robot)
        
    truffle_list = []
    for i in range(2):
        truffle = Agent(x = random(width),
                      y = random(height),
                      draw = draw_truffle,
                      size = 15,
                      max_speed = 0)
        truffle.bump(random(360), 1.0)
        truffle_list.append(truffle) 
    
def draw():
    global pig_list
    global robot_list
    global truffle_list

    background(255)
    
    # every 500 frames
    if frameCount % 100 == 0:
        truffle = Agent(x = random(width),
                      y = random(height),
                      draw = draw_truffle,
                      size = 15,
                      max_speed = 0)
        truffle.bump(random(360), 1.0)
        truffle_list.append(truffle) 
    
    for pig in pig_list: 
        pig.draw()
        pig.move()
        pig.collide(pig_list)
        
        pig.seek(pig_list,200,0.1) # who, radius, strength
        pig.avoid(pig_list, 75, 0.2)
        pig.align(pig_list, 200, 0.1)
        
        pig.avoid(robot_list, 300, 5)
        
        pig.seek(pig.closest(truffle_list), 300, 2)
        
        for truffle in truffle_list:
            if pig.touching(truffle):
                truffle_list.remove(truffle)
                pig.size += 50
        
    for robot in robot_list:
        robot.draw()
        robot.move()
        
        robot.collide(robot_list)
        robot.avoid_edges(50,1)
    
        robot.seek(robot.closest(pig_list), 200, 1)
        
        for pig in pig_list:
            if robot.touching(pig):
                pig_list.remove(pig)
    
    for truffle in truffle_list:
        truffle.draw()
        
def draw_robot(robot):
    strokeWeight(2)
    stroke(200)
    fill(100)
    square(robot.x-15, robot.y-15, 30)
    circle(robot.x+6, robot.y-3, 6)
    circle(robot.x-6, robot.y-3, 6)
    fill(255)
    circle(robot.x, robot.y+7, swing(0, 10, 10))
    
def draw_pig(pig):
    fill(245,86,222)
    circle(pig.x, pig.y, 25)
    circle(pig.x, pig.y-(0.34*pig.size), 0.5*pig.size)
    fill(0)
    circle(pig.x-3, pig.y-15, 3)
    circle(pig.x+3, pig.y-15, 3)
    
def draw_truffle(truffle):
    fill(0)
    square(truffle.x, truffle.y, 20)
    
