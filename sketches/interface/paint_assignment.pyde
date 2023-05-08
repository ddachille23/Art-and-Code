import time

add_library('sound')

brush_color = "black" # default value
brush_shape = "circle"


def setup():
    global osc, freq, black_sound, white_sound, red_sound, orange_sound, \
    yellow_sound, green_sound, blue_sound, purple_sound, pink_sound, \
    last_triggered_times, debounce_time, circle_sound, square_sound, \
    triangle_sound, star_sound, colors_sound, shapes_sound
    size(1400,800)
    background(255)
    
    # use for debouncing
    last_triggered_times = {} # dictionary to store trigger times
    debounce_time = 500  # in milliseconds
        
    # sine wave oscillator 
    osc = SinOsc(this) # initialize
    osc.play() # play the sound    
    
    # # this loads the file based on the file name
    # global red_sound
    # load color sounds
    black_sound = SoundFile(this, "black.wav")
    white_sound = SoundFile(this, "white.wav")
    red_sound = SoundFile(this, "red.wav")
    orange_sound = SoundFile(this, "orange.wav")
    yellow_sound = SoundFile(this, "yellow.wav")
    green_sound = SoundFile(this, "green.wav")
    blue_sound = SoundFile(this, "blue.wav")
    purple_sound = SoundFile(this, "purple.wav")
    pink_sound = SoundFile(this, "pink.wav")
    
    # shape sounds
    circle_sound = SoundFile(this, "circle.wav")
    square_sound = SoundFile(this, "square.wav")
    triangle_sound = SoundFile(this, "triangle.wav")
    star_sound = SoundFile(this, "star.wav")

    # text sound
    colors_sound = SoundFile(this, "colors.wav")
    shapes_sound = SoundFile(this, "shapes.wav")

    # text
    f = createFont("Arial",16)
    textFont(f,24)   
    fill(0)
    text("Colors", 15, 35)
    text("Shapes", 140, 35)

    # color
    ## black square
    fill(0)
    square(15,50,70)
    ## white square
    fill(255)
    square(15,130,70)
    ## red square
    fill(255,0,0)
    square(15,210,70)
    ## orange square
    fill(255,165,0)
    square(15,290,70)
    ## yellow square
    fill(255,255,0)
    square(15,370,70)
    ## green square
    fill(0,255,0)
    square(15,450,70)
    ## blue square
    fill(0,0,255)
    square(15,530,70)
    ## purple square
    fill(128,0,128)
    square(15,610,70)
    ## pink square
    fill(255,192,203)
    square(15,690,70)
    
    # shapes
    ## circle
    noFill()
    square(110, 50, 150)
    fill(0)
    circle(110+75,50+75, 100)
    noFill()
    
    ## square
    square(110, 210, 150)
    fill(0)
    square(110+25, 210+25, 100)
    noFill()
    
    ## triangle
    square(110, 370, 150)
    fill(0)
    triangle(110+75, 370+20, 110+20, 370+150-20, 110+150-20, 370+150-20)
    noFill()
    
    # star
    square(110, 530, 150)
    fill(0)
    pushMatrix();
    translate(185, 605)
    scale(0.9)
    star(0, 0, 30, 70, 5); 
    popMatrix();
    
    # filler
    rect(110, 690, 150, 70)
    

def draw():
    global osc, freq, brush_color, brush_shape
    
    x = mouseX
    y = mouseY
    cx = 567.5+265
    cy = height/2
    
    distance_center = dist(x, y, cx, cy)
    max_distance = dist(0, 0, cx, cy)
    freq = map(distance_center, 0, max_distance, 200, 1000)
    osc.freq(freq) # dynamically set the freq
    
    # set sound to only play on drawing part of canvas
    if mouseX < 265:
        osc.amp(0)
    else:
        osc.amp(0.1)
    
   
    if mousePressed:
        noStroke()
        # brush color
        if brush_color == "black":
            fill(0)
        if brush_color == "white":
            fill(255)
        if brush_color == "red":
            fill(255,0,0)
        if brush_color == "orange":
            fill(255,165,0)
        if brush_color == "yellow":
            fill(255,255,0)
        if brush_color == "green":
            fill(0,255,0)
        if brush_color == "blue":
            fill(0,0,255)
        if brush_color == "purple":
            fill(128,0,128)
        if brush_color == "pink":
            fill(255,192,203)
        # brush shape
        if brush_shape == "circle":
            if mouseX > 265:
                circle(mouseX, mouseY, 50)
        if brush_shape == "sqaure":
            if mouseX > 265:
                square(mouseX, mouseY, 50)
        if brush_shape == "triangle":
            if mouseX > 265:
                triangle(mouseX, mouseY-20, mouseX-20, mouseY+20, mouseX+20, mouseY+20)
        if brush_shape == "star":
            if mouseX > 265:
                star(mouseX, mouseY, 18, 42, 5); 
                

def mouseClicked():
    global brush_color, brush_shape
    ## colors
    ### black
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 50 and mouseY <= 120:
            brush_color = "black"
    ### white
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 130 and mouseY <= 200:
            brush_color = "white"
    ### red
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 210 and mouseY <= 280:
            brush_color = "red"
    ### orange
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 290 and mouseY <= 360:
            brush_color = "orange"
    ### yellow
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 370 and mouseY <= 440:
            brush_color = "yellow"
    ### green
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 450 and mouseY <= 520:
            brush_color = "green"
    ### blue
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 530 and mouseY <= 600:
            brush_color = "blue"
    ### purple
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 610 and mouseY <= 680:
            brush_color = "purple"
    ### pink
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 690 and mouseY <= 760:
            brush_color = "pink"
            
    ## shapes
    if mouseX >= 110 and mouseX <= 260 and mouseY >= 50 and mouseY <= 200:
            brush_shape = "circle"
    if mouseX >= 110 and mouseX <= 260 and mouseY >= 210 and mouseY <= 360:
            brush_shape = "sqaure"
    if mouseX >= 110 and mouseX <= 260 and mouseY >= 370 and mouseY <= 520:
            brush_shape = "triangle"
    if mouseX >= 110 and mouseX <= 260 and mouseY >= 530 and mouseY <= 680:
            brush_shape = "star"
    
# gets called everytime the mouse is moved    
def mouseMoved():
    trigger = "mouseMoved"
    trigger_event(trigger)
        
def trigger_event(trigger):
    global last_triggered_times
    
    current_time = int(round(time.time() * 1000))
    if trigger in last_triggered_times and current_time - last_triggered_times[trigger] < debounce_time:
        return
    # Do the action for the trigger event here
    
    # text
    if mouseX <= 80 and mouseY <= 40:
            colors_sound.play()
            
    if mouseX >= 120 and mouseX <= 240 and mouseY <= 40:
            shapes_sound.play()
    
    ## colors
    ### black
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 40 and mouseY <= 120:
            black_sound.play()
    ### white
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 130 and mouseY <= 200:
            white_sound.play()
    ### red
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 210 and mouseY <= 280:
            red_sound.play()
    ### orange
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 290 and mouseY <= 360:
            orange_sound.play()
    ### yellow
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 370 and mouseY <= 440:
            yellow_sound.play()
    ### green
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 450 and mouseY <= 520:
            green_sound.play()
    ### blue
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 530 and mouseY <= 600:
            blue_sound.play()
    ### purple
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 610 and mouseY <= 680:
            purple_sound.play()
    ### pink
    if mouseX >= 15 and mouseX <= 85 and mouseY >= 690 and mouseY <= 760:
            pink_sound.play()
    
    ## shapes
    if mouseX >= 110 and mouseX <= 260 and mouseY >= 50 and mouseY <= 200:
            circle_sound.play()
    if mouseX >= 110 and mouseX <= 260 and mouseY >= 210 and mouseY <= 360:
            square_sound.play()
    if mouseX >= 110 and mouseX <= 260 and mouseY >= 370 and mouseY <= 520:
            triangle_sound.play()
    if mouseX >= 110 and mouseX <= 260 and mouseY >= 530 and mouseY <= 680:
            star_sound.play()
    
    last_triggered_times[trigger] = current_time
    

# for making stars
def star(x, y, radius1, radius2, npoints):
    angle = TWO_PI / (npoints * 2)
    half_angle = angle / 2.0
    beginShape()
    for a in range(npoints * 2):
        sx = x + cos(angle * a) * radius2
        sy = y + sin(angle * a) * radius2
        vertex(sx, sy)
        sx = x + cos(angle * a + half_angle) * radius1
        sy = y + sin(angle * a + half_angle) * radius1
        vertex(sx, sy)
    endShape(CLOSE)


    
