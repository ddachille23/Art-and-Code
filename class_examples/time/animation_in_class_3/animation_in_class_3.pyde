def setup():
    size(600, 600)
    colorMode(HSB, 360, 100, 100)
    
# def draw():
#     background(change(0,255,300))
    
#     circle(swing(25, width-25, 200), height/2, 50)
    
#     circle(swing(25, width-25, 200), swing(10, height-10, 100), 20)    
    
# def change(start, stop, duration, offset=0):
#     return map((frameCount + offset) % duration, 0, duration, start, stop)

# def swing(start, stop, duration, offset=0): 
#     position = sin(2 * PI * change(0, 1, duration * 2, offset)) * .5 + .5
#     return (position * (stop - start)) + start 

def draw():
    
    fill(30, 255, swing(0,100,255))
    background(change(0,255,300))
    
    # circle(swing(25, width-25, 200), height/2, 50)
    
    # circle(swing(20, width-25, 200), swing(10, height-10, 100), 20)    
    
    circle(swing(25, width-25, 200), height/2, 50)
    circle(swing(25, width-25, 200) + swing(-10, -10, 50), change(height/2, 0, 300), 20)
    circle(swing(25, width-25, 200) + swing(-10, -10, 60), change(height/2, 0, 300), 5)
    
    
    
def change(start, stop, duration, offset=0):
    return map((frameCount + offset) % duration, 0, duration, start, stop)

def swing(start, stop, duration, offset=0): 
    position = sin(2 * PI * change(0, 1, duration * 2, offset)) * .5 + .5
    return (position * (stop - start)) + start 
