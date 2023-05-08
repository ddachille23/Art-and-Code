size(950,687)
background(255)
source = loadImage("skier.png")

#image(source, 0, 0)

# pixel = source.get(0,0)

# r = red(pixel)
# g = green(pixel)
# b = blue(pixel)

# print(r,g,b)

# for y in range(0,height,8):
#     for x in range(0,width,8):
#         pixel = source.get(x,y)
#         r = red(pixel)
#         g = green(pixel)
#         b = blue(pixel)
        
#         # stroke(255-r,255-g,100-b)
#         # point(width-x*1.08,y+y*1.03-x)
#         fill(random(0,255)-r,g,b, random(10,50))
#         # square(x,y,5)
#         noStroke()
#         circle(x,y*4,random(5,30))
#         circle(width-x,height-y,5)

# # gradient
# for y in range(0,height,1):
#     for x in range(0,width,1):
#         pixel = source.get(x,y)
#         r = red(pixel)
#         g = green(pixel)
#         b = blue(pixel)

#         stroke(x,g,b)
#         point(x,y)
      
# # pixel shift
# for y in range(0,height,1):
#     for x in range(0,width,1):
        
#         pixel_1 = source.get(x,y)
#         r_1 = red(pixel_1)
#         g_1 = green(pixel_1)
#         b_1 = blue(pixel_1)
        
#         pixel_2 = source.get(x+50,y)
#         r_2 = red(pixel_2)
#         g_2 = green(pixel_2)
#         b_2 = blue(pixel_2)

#         stroke(r_1,g_2,b_2)
#         point(x,y)


# # selective pixel shift
# for y in range(0,height,1):
    
#     offset = 0
#     if random(100) < 30:
#         offset = int(random(50))
            
#     for x in range(0,width,1):
#         pixel_1 = source.get(x,y)
#         r_1 = red(pixel_1)
#         g_1 = green(pixel_1)
#         b_1 = blue(pixel_1)
        
#         pixel_2 = source.get(x+offset,y)
#         r_2 = red(pixel_2)
#         g_2 = green(pixel_2)
#         b_2 = blue(pixel_2)

#         stroke(r_1,g_2,b_1)
#         point(x,y)

# # gradient
# for y in range(0,height,1):
#     for x in range(0,width,1):
#         pixel = source.get(x,y)
#         r = red(pixel)
#         g = green(pixel)
#         b = blue(pixel)

#         stroke(x,g,b)
#         point(x,y)

# # playing around
# for y in range(0,height,2):
    
#     offset = 0
#     if random(100) < 50:
#         offset = int(random(100))
            
#     for x in range(0,width,1):
#         pixel_1 = source.get(x,y)
#         r_1 = red(pixel_1)
#         g_1 = green(pixel_1)
#         b_1 = blue(pixel_1)
        
#         pixel_2 = source.get(x+offset,y)
#         r_2 = red(pixel_2)
#         g_2 = green(pixel_2)
#         b_2 = blue(pixel_2)

#         stroke(b_2,g_2,r_1)
#         point(width-x,y*1.3-x)
        
#         fill(r_1,g_2,b_1,50)
#         circle(900-x,y,random(20,22))
#         circle(x,y,random(5,20))
#         # circle(width-x,height-y,5)

## class 3/22 

# - half and half color
# for y in range(0, height):
#     for x in range(0, width):
#         pixel = source.get(x,y)
#         r = red(pixel)
#         g = green(pixel)
#         b = blue(pixel)
        
#         noStroke()
#         if x > width/2:
#             fill(b,r,g)
#         else:
#             fill(r,g,b)
#         square(x,y,1)
        
# making an inverted square
# for y in range(0, height):
#     for x in range(0, width):
#         pixel = source.get(x,y)
#         r = red(pixel)
#         g = green(pixel)
#         b = blue(pixel)
        
#         noStroke()
#         # square inversion
#         if x > 730 and x < 830 and y > 120 and y < 220:
#             fill(b,r,g)
#         # snow effect
#         elif x > 10 and x < 900 and y > 200 and y < 300:
#             stroke(r,g,b)
#             point(x + random(-2,2), y + random(-2,2))
#         else:
#             fill(r,g,b)
#         square(x,y,1)
        
# drawing part of the image


start_x = 0
start_y = 0
flip = True
for i in range(150):
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
            pixel = source.get(x,y)
            r = red(pixel)
            g = green(pixel)
            b = blue(pixel)
            
            stroke(r+color_offset,g,b)
            
            if flip == True:
                point(width - (x+offset_x),y+offset_y)
            else:
                point(x,y)
