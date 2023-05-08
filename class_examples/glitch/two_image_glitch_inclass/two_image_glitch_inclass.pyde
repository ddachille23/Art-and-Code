size(400,400)
source = loadImage("kyle-mcdonald-modified.jpeg")
source2 = loadImage("facework-image.jpeg")
background(255)

for y in range(0, height, 1):
    for x in range(0, width, 1):
        pixel = source.get(x,y)
        r = red(pixel)
        g = green(pixel)
        b = blue(pixel)
        
        pixel2 = source2.get(x,y)
        r2 = red(pixel2)
        g2 = green(pixel2)
        b2 = blue(pixel2)
        
        if r < 200 and b < 100:
            stroke(r2,g2,b2)
            point(x,y)

# # weird square stuff
# for y in range(0, height, 5):
#     for x in range(0, width, 5):
#         pixel = source.get(x,y)
#         r = red(pixel)
#         g = green(pixel)
#         b = blue(pixel)
        
#         pixel2 = source2.get(x,y)
#         r2 = red(pixel2)
#         g2 = green(pixel2)
#         b2 = blue(pixel2)
        
#         if random(100) < 50:
#             fill(r2, g2, b2)
#             square(x,y,10)
                
