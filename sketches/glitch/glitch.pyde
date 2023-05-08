# Glitch Sketch
# Dan Dachille

# setup
size(1000,1000)
background(255)

# image loading
powell_source = loadImage("powell-image.png")
tbill_source = loadImage("t-bill.png")
svb_source = loadImage("svb-logo-2.png")
fed_source = loadImage("fed-symbol.png")
flag_source = loadImage("flag.png")

# flag
for y in range(0, height, 1):
    for x in range(0, width, 1):
        pixel = flag_source.get(x,y)
        r = red(pixel)
        g = green(pixel)
        b = blue(pixel)
        
        stroke(r,g,b)
        point(x,y)

# powell and t-bill        
for y in range(0, height, 1):
    offset = 0
    if random(100) < 30:
        offset = int(random(50))
    for x in range(0, width, 1):
        pixel = powell_source.get(x+offset,y)
        r1 = red(pixel)
        g1 = green(pixel)
        b1 = blue(pixel)
        
        pixel2 = tbill_source.get(x,y)
        r2 = red(pixel2)
        g2 = green(pixel2)
        b2 = blue(pixel2)
        
        stroke(r2-20,g1,b1)
        point(x,y)
        
# svb            
color_offset = int(random(-100,100))
for y in range(0, width,2):
    for x in range(0, height,2):
        pixel = svb_source.get(x,y)
        r = red(pixel)
        g = green(pixel)
        b = blue(pixel)
        
        stroke(r+color_offset,b,g)
        fill(random(0,255)-r,g,b, random(10,15))
        noStroke()
        #point(x,y)
        circle(900-x, 900-y, 5)
        
# broken up fed symbol
start_x = 0
start_y = 0
flip = True
for i in range(50):
    start_x = int(random(width))
    stop_x = start_x + int(random(250))
    start_y = int(random(height))
    stop_y = start_y + int(random(250))
    
    offset_x = int(random(-200,200))
    offset_y = int(random(-200,200))
    
    if random(100) < 50:
        flip = True
    else:
        flip = False
    
    color_offset = int(random(-100,100))
    for y in range(start_x, stop_x):
        for x in range(start_y, stop_y):
            pixel = fed_source.get(x,y)
            r = red(pixel)
            g = green(pixel)
            b = blue(pixel)
            
            stroke(r+color_offset,g,b, random(80,120))

            if flip == True:
                point(width - (x+offset_x),y+offset_y)
            else:
                point(x,y)
                


    
    

        
