# Dan Dachille
# Sketch #2: Repitition

# canvas setup
size(600, 400)
background(255)

# make geometric sunlight
for i in range(width, 50, -8): 
    strokeWeight(i/2)
    for j in range(8):
        for k in range(5): 
            noFill()
            stroke(250,i/(2+j/100), 20, 255)
            square(i/(k+0.1), height/4, 50+j)
            rotate(radians(1.8))

# save image
save("dan_repetition.png")


                
