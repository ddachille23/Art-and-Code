size(640, 480)
background(255)

# jittered squares
# for i in range(16): 
#     for j in range(12):
#         square(i*40 + random(0,5),j*40 + random(0,5), 30)
        


   
# for i in range(16): 
#     for j in range(12):
#         for k in range(5):
#             fill(random(255), 0, random(100), random(150))
#             square(i*40, j*40, 5*(random(4,8)-k))
#             #rect(i*40, j*40, (50-(k*5))*random(5,15), 20)
    
# fun graphic
for i in range(width):
    fill(i, 25, 200)
    noStroke()
    for j in range(50):
        fill(i, 25, 200, 4)
        for k in range(55): 
            circle(i, j + randomGaussian(), 5)
            rotate(radians(84.482))
    
            
# # rotation
# push()
# translate(100,100)
# rotate(radians(45))
# square(0,0,50)
# pop()
        
        
        
    
