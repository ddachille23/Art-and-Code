# paint agent

from agent_helper import *

def setup():
    global mouse_agent, chase_agent
    size(500,500)
    pixelDensity(2)
    
    mouse_agent = Agent(x = random(width),
                        y = random(height),
                        draw = None)
    chase_agent = Agent(x = random(width),
                        y = random(height),
                        draw = draw_chaser,
                    max_speed = 5)
    chase_agent.bump(random(360), 0.5)
def draw():
    global mouse_agent, chase_agent
    
    if keyPressed:
        if key == "s":
            print("hi")
    
    mouse_agent.x = mouseX
    mouse_agent.y = mouseY
    
    if mousePressed:
        chase_agent.draw()
        chase_agent.move()
        chase_agent.avoid_edges(200,1)
        chase_agent.seek(mouse_agent, 100,1)
def draw_chaser(agent):
    fill(255)
    circle(agent.x, agent.y,10)

def mouseClicked():
    global chase_agent
    chase_agent.x = mouseX
    chase_agent.y = mouseY
