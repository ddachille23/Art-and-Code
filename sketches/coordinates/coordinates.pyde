# set canvus properties
def setup(): 
    size(1054, 694) # width, height
    background(255)
    
# tree object
'''
recursive tree 

Parameters
----------
x_location:int
    location of the tree along the x-axis (0-width)(no default)
    * note: set equal to width/2 for the middle of the canvas
y_location:int
    location of the tree along the y-axis (0-height)(no default)
    * note: set equal to height for the bottom of the canvas
size_input:int
    overall scale of the tree (default = 120)
red_val:int 
    red value for the stroke of the tree (0-255)(default = 0)
green_val:int
    green value for the stroke of the tree (0-255)(default = 0)
blue_val:int
    blue value for the stroke of the tree (0-255)(default = 0)
angle:int
    angle of the tree top (0-90)(default = 30)
branch_prop:float
    determines how big the next branch will be relative to the last drawn one (0-1)(default = 0.67)

example using defaults
----------------------
myTree = Tree(320, 360)
def draw():
    myTree.display()
'''

class Tree(object): 

    ## constructor
    def __init__(self, x_location, y_location, size_input = 120, red_val = 0, green_val = 0, blue_val = 0, angle = 30, branch_prop = 0.67): 
        self.xloc = x_location
        self.yloc = y_location
        self.size_input = size_input
        self.r = red_val
        self.g = green_val
        self.b = blue_val
        self.a = angle
        self.bp = branch_prop
        
    
    # draws the recursive tree
    def display(self): 
        stroke(self.r, self.g, self.b)
        strokeWeight(1.5)
        # angle 0 to 90 degrees
        angle = float(self.a)
        # # Convert it to radians
        global theta 
        theta = radians(angle)
        # tree positioning
        translate(self.xloc,self.yloc)
        # # Draw a line 120 pixels
        line(0,0,0, -self.size_input)
        # # Move to the end of that line
        translate(0,-self.size_input)
        # # Start the recursive branching!
        self.branch(self.size_input)
    
    # defining the tree
    def branch(self, h):
        # Each branch will be self.bp the size of the previous one
        h *= self.bp;
        # exit condition is 2
        # Here, ours is when the length of the branch is 2 pixels or less
        if h > 2:
            pushMatrix();    # Save the current state of transformation (i.e. where are we now)
            rotate(theta);   # Rotate by theta
            line(0, 0, 0, -h);  # Draw the branch
            translate(0, -h); # Move to the end of the branch
            self.branch(h);       # call self to draw two new branches
            popMatrix();     # pop in order to restore the previous matrix state
            line(0, 0, 0, -h);
        # Repeat the same thing, only branch off to the "left" this time
            pushMatrix();
            rotate(-theta);
            line(0, 0, 0, -h);
            translate(0, -h);
            self.branch(h);
            popMatrix();
            
            

def draw(): 
    
    # upper half background 
    #------
    stroke(0)
    fill(252, 240, 198)
    rect(0,0,width, height)
    #------
    
    # circle pattern in background
    fill(175, 38, 2, 10)
    stroke(255, 50)
    for i in range(0, width, 30):
        for j in range(0, height, 30):
            ellipse(i, j, 60, 60)

    # green floating circles [BACK]
    #------
    fill(19, 25, 83, 150)
    circle(1000, 220, 120)
    circle(950, 200, 105)
    circle(900, 180, 115)
    circle(850, 165, 100)
    circle(800, 160, 130)
    circle(750, 150, 125)
    circle(700, 145, 115)
    circle(650, 140, 140)
    circle(600, 140, 122)
    
    circle(550, 160, 150)
    circle(500, 150, 122)

    #------
    
    # arc 1
    #------
    fill(179, 0, 189, 60)
    beginShape()
    ## start
    curveVertex(0, 310)
    curveVertex(0, 310)
    ## intermediate anchor points
    curveVertex(width/4,180)
    curveVertex(width,320)
    ## end
    curveVertex(width, height)
    curveVertex(width, height)
    endShape()
    #------
    # arc 2
    #------
    fill(22, 0, 189, 90)
    beginShape()
    ## start
    curveVertex(0, 310)
    curveVertex(0, 310)
    ## intermediate anchor points
    curveVertex(width/4,230)
    curveVertex(width,320)
    ## end
    curveVertex(width, height)
    curveVertex(width, height)
    endShape()
    #------
    # arc 3
    #------
    fill(179, 0, 189, 80)
    beginShape()
    ## start
    curveVertex(0, 310)
    curveVertex(0, 310)
    ## intermediate anchor points
    curveVertex(width/4,280)
    curveVertex(width,320)
    ## end
    curveVertex(width, height)
    curveVertex(width, height)
    endShape()
    #------
    
    
    # grey path above orange bowl 
    #------
    fill(138, 121, 113)
    beginShape()
    ## start
    curveVertex(0, 310)
    curveVertex(0, 310)
    ## intermediate anchor points
    curveVertex(164,314)
    curveVertex(428,322)
    curveVertex(705,347)
    curveVertex(width, 418)
    curveVertex(width, 492)
    ## end
    curveVertex(0, 380)
    curveVertex(0, 380)
    endShape()
    #-------
    
    # little house 
    ## base
    #------
    fill(192, 44, 14)
    rect(759,300,270, 115)
    #------
    ## roof
    fill(240, 141, 40)
    beginShape()
    vertex(759, 300)
    vertex(868, 220)
    vertex(759+270, 300)
    endShape()
    #------
    ## detail
    line(759, 315, 1000, 315)
    line(1000, 315, 1000, 400)
    line(1000, 400, 800, 400)
    
    
    
    # orange bowl shape
    #------
    fill(226, 111, 20)
    beginShape()
    ## start
    curveVertex(0, 358)
    curveVertex(0, 358)
    ## intermediate anchor points
    curveVertex(647,375)
    curveVertex(846,406)
    curveVertex(1021,472)
    curveVertex(995, 583)
    curveVertex(742,664)
    curveVertex(742,664)
    curveVertex(0,height)
    ## end
    curveVertex(0, 583)
    curveVertex(0, 583)
    endShape()
    #-------
    
    # bottom blue mountain line thing
    #------
    fill(23, 35, 75)
    beginShape()
    ## start
    curveVertex(0, 550)
    curveVertex(0, 550)
    ## intermediate anchor points
    curveVertex(150,460)
    curveVertex(458,598)
    curveVertex(413,685)
    ## end
    curveVertex(0, 638)
    curveVertex(0, 638)
    endShape()
    #------
    
    # blue tunnel thing in middle right
    #------
    fill(6, 9, 54, 220)
    beginShape()
    ## start
    curveVertex(550, 585)
    curveVertex(550, 585)
    ## intermediate anchor points
    curveVertex(551, 557)
    curveVertex(572,538)
    curveVertex(600,530)
    curveVertex(645,550)
    curveVertex(650,595)
    curveVertex(600,640)
    ## end

    curveVertex(550, 585)
    endShape()
    #------
    
    # blue stuff bottom right
    #------
    fill(120, 122, 144)
    beginShape()
    ## start
    curveVertex(230, height)
    curveVertex(230, height)
    ## intermediate anchor points
    curveVertex(316,663)
    curveVertex(446,583)
    curveVertex(553,584)
    curveVertex(627,605)
    curveVertex(713,556)
    curveVertex(width,565)
    curveVertex(width,630)
    ## end
    curveVertex(352, height)
    curveVertex(352, height)
    endShape()
    #------
    
    
    # yellow stuff bottom right
    #------
    fill(234, 162, 2)
    beginShape()
    ## start
    curveVertex(654, height)
    curveVertex(654, height)
    ## intermediate anchor points
    curveVertex(664,669)
    curveVertex(724,639)
    curveVertex(739,565)
    curveVertex(721,497)
    curveVertex(774,483)
    curveVertex(915,587)
    curveVertex(1027,540)
    curveVertex(1030,470)
    curveVertex(width,470)
    curveVertex(width,565)
    curveVertex(width,630)
    ## end
    curveVertex(841, height)
    curveVertex(841, height)
    endShape()
    #------
    
    # bottom middle orange
    #------
    fill(226, 111, 20)
    beginShape()
    ## start
    curveVertex(346, height)
    curveVertex(346, height)
    ## intermediate anchor points
    curveVertex(427,652)
    curveVertex(516,625)
    ## end
    curveVertex(730, height)
    curveVertex(730, height)
    endShape()
    #------
    
    # bottom right orange
    #------
    fill(226, 111, 20)
    beginShape()
    ## start
    curveVertex(840, height)
    curveVertex(840, height)
    ## intermediate anchor points
    curveVertex(900,665)
    curveVertex(1000,624)
    curveVertex(1050,615)
    ## end
    curveVertex(width, height+10)
    curveVertex(width, height+10)
    endShape()
    #------
    
    
    # bottom left green leaf
    #------
    fill(127, 128, 35)
    beginShape()
    ## start
    curveVertex(0, 425)
    curveVertex(0, 425)
    ## intermediate anchor points
    curveVertex(7,460)
    curveVertex(4,471)
    curveVertex(23,461)
    curveVertex(23,480)
    curveVertex(30,481)
    curveVertex(25,492)
    curveVertex(24,506)
    curveVertex(37,506)
    curveVertex(35,514)
    curveVertex(55,503)
    curveVertex(53,511)
    curveVertex(70,506)
    curveVertex(62,516)
    curveVertex(71,516)
    curveVertex(62,526)
    curveVertex(59,535)
    curveVertex(54,550)
    curveVertex(57,566)
    curveVertex(34,583)
    curveVertex(34,603)
    curveVertex(13,606)
    curveVertex(17,623)
    ## end
    curveVertex(0, 638)
    curveVertex(0, 638)
    endShape()
    #------
    
    # bottom right orange tree 
    #------
    fill(10, 32, 82)
    beginShape()
    ## start
    curveVertex(838, 594)
    curveVertex(838, 594)
    ## intermediate anchor points
    curveVertex(871,521)
    curveVertex(875,448)
    curveVertex(917,358)
    curveVertex(857,102)
    curveVertex(810,0)
    curveVertex(793,0)
    curveVertex(810,53)
    curveVertex(851,73)
    curveVertex(902,0)
    curveVertex(920,0)
    curveVertex(888,92)
    curveVertex(959,351)
    curveVertex(920,490)
    ## end
    curveVertex(907, 610)
    curveVertex(907, 610)
    endShape()
    #------
    
    
    # bottom right tree leaves on top
    #------
    fill(147, 16, 0, 235)
    beginShape()
    ## start
    curveVertex(789, 86)
    curveVertex(789, 86)
    ## intermediate anchor points
    curveVertex(763,54)
    curveVertex(710,60)
    curveVertex(700,0)
    curveVertex(987,0)
    curveVertex(974,22)
    curveVertex(941,34)
    curveVertex(886,32)
    curveVertex(859,69)
    ## end
    curveVertex(789, 86)
    curveVertex(789, 86)
    endShape()
    #------
    
    
    # bottom right tree blue sap stuff
    #------
    fill(72, 89, 73)
    beginShape()
    ## start
    curveVertex(838, 594)
    curveVertex(838, 594)
    ## intermediate anchor points
    curveVertex(802,647)
    curveVertex(750,688)
    curveVertex(785,682)
    ## end
    curveVertex(907, 610)
    curveVertex(907, 610)
    endShape()
    #------
    # small black circle bottom of tree
    fill(0,0,0)
    beginShape()
    ## start
    curveVertex(838, 594)
    curveVertex(838, 594)
    ## intermediate anchor points
    curveVertex(852,602)
    ## end
    curveVertex(907, 610)
    curveVertex(907, 610)
    endShape()
    
    # middle tree leaves
    #------
    fill(244, 182, 9, 150)
    beginShape()
    ## start
    curveVertex(318, 538)
    curveVertex(318, 538)
    ## intermediate anchor points
    curveVertex(246, 338)
    curveVertex(198,131)
    curveVertex(304,23)
    curveVertex(380, 150)

    ## end
    curveVertex(358, 538)
    curveVertex(358, 538)
    endShape()
    #------
    
    # middle tree stem
    #------
    fill(175, 38, 2)
    beginShape()
    ## start
    curveVertex(301, 583)
    curveVertex(301, 583)
    ## intermediate anchor points
    curveVertex(310, 500)
    curveVertex(315,351)
    curveVertex(304,100)
    curveVertex(312,100)
    curveVertex(354,505)
    curveVertex(388,580)
    ## end
    curveVertex(301, 583)
    curveVertex(301, 583)
    endShape()
    #------
    
    # middle tree #2 thicker leaves
    #------
    fill(55, 85, 35, 240)
    beginShape()
    ## start
    curveVertex(378, 127)
    curveVertex(378, 127)
    ## intermediate anchor points
    curveVertex(340, 8)
    curveVertex(665,30)
    curveVertex(607,166)
    curveVertex(380, 150)

    ## end
    curveVertex(378, 127)
    endShape()
    #------
    
    # middle tree stem #2 thicker
    #------
    fill(90, 100, 109)
    beginShape()
    ## start
    curveVertex(440, 645)
    curveVertex(440, 645)
    ## intermediate anchor points
    curveVertex(487, 451)
    curveVertex(493,224)
    curveVertex(446,177)
    curveVertex(402,78)
    curveVertex(380,30)
    #curveVertex(300,50)
    
    #curveVertex(320,40)
    curveVertex(400,50)
    curveVertex(499,208)
    curveVertex(535,50)
    
    ## end
    curveVertex(520, 625)
    curveVertex(520, 625)
    endShape()
    #------
    
    # tumbstone thingy
    #------
    fill(74, 71, 64)
    beginShape()
    ## start
    curveVertex(219-50, 649)
    curveVertex(219-50, 649)
    ## intermediate anchor points
    curveVertex(211-50, 557)
    curveVertex(238-50,530)
    curveVertex(275-50,550)
    curveVertex(303-50,622)
    curveVertex(300-50,630)
    ## end

    curveVertex(219-50, 649)
    endShape()
    #------
    
    # tumbstone thingy interior shape
    #------
    fill(212, 108, 35)
    beginShape()
    ## start
    curveVertex(236-50, 612)
    curveVertex(236-50, 612)
    ## intermediate anchor points
    curveVertex(235-50, 589-20)
    curveVertex(238-50,581-20)
    curveVertex(254-50,580-20)
    curveVertex(257-50,586-20)
    curveVertex(259-40,605)
    ## end

    curveVertex(236-50, 612)
    endShape()
    #------
    
    # tumbstone thingy yellow top
    fill(200, 145, 0, 220)
    circle(167, 562, 8)
    circle(167+7, 562, 8)
    circle(167+13, 562, 8)
    circle(167, 555, 8)
    circle(167+7, 555, 8)
    circle(167+14, 555, 8)
    circle(167+20, 555, 8)
    circle(167+26, 555, 8)
    circle(167+32, 555, 8)
    circle(167+38, 555, 8)
    circle(167+44, 555, 8)
    circle(167+50, 555, 8)
    circle(167+55, 555, 8)
    circle(167, 548, 8)
    circle(167+7,548, 8)
    circle(167+14, 548, 8)
    circle(167+20, 548, 8)
    circle(167+26, 548, 8)
    circle(167+32, 548, 8)
    circle(167+38, 548, 8)
    circle(167+44, 548, 8)
    circle(167+50, 548, 8)
    circle(167+7,542, 8)
    circle(167+14, 542, 8)
    circle(167+20, 542, 8)
    circle(167+26, 542, 8)
    circle(167+32, 542, 8)
    circle(167+38, 542, 8)
    circle(167+44, 542, 8)
    circle(167+14, 536, 8)
    circle(167+20, 536, 8)
    circle(167+26, 536, 8)
    circle(167+32, 536, 8)
    
    
    # green floating circles [FRONT]
    #------
    fill(73, 120, 16, 150)
    circle(870, 280, 150)
    circle(910, 270, 130)
    circle(950, 250, 100)
    circle(980, 210, 80)
    circle(1000, 250, 80)
    circle(1020, 220, 70)
    #------
    
 
    
    # fractal trees
    myTree = Tree(x_location = 1054/10, y_location = 680, 
                  size_input = 120, angle = 25, 
                  branch_prop = 0.67, 
                  red_val = 28, green_val = 77, blue_val = 0)
    myTree.display()
    myTree = Tree(x_location = 600, y_location = 180, 
                  size_input = 120, angle = 25, 
                  branch_prop = 0.67, 
                  red_val = 177, green_val = 40, blue_val = 10)
    myTree.display()

    save("dan-landscape.png")
