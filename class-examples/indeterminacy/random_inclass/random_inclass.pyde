# canvas
size(500,500)
#randomSeed(0)

circle(width/2, height/2, 100)

for i in range(100):
    for j in range(50): 
        circle(random(width), random(height), j)
        stroke(i, j*5, 255, 25)
        fill(random(255), 0, i, 30)


for i in range (100): 
    strokeWeight(random(0,100))
    fill(20 * i/2, 30, 55, 1.5)
    stroke(20 * i/2, 30, 55,1.5)
    triangle(random(width), random(height), random(width),
         random(width), random(height), random(width))
