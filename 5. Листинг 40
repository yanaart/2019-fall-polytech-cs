counter = float()
cx = float(250)
cy = float(250)
cRadius = float(200)
mcolor = int() 

def setup ():
    
    size(500, 500)
    smooth()
    background(50)
    strokeWeight(2)
    stroke(250)

def draw():
    
    global counter, cx, cy, cRadius, mcolor
    
    x1 = sin(counter)*cRadius+cx
    y1 = cos(counter)*cRadius+cy
    mcolor = mcolor+1
    stroke (mcolor)
    line (cx, cy, x1, y1)
    counter = counter + 2*PI/255
    
    if ( counter > 2*PI):
        counter = 0
        mcolor = 0
        background (50) 

def keyPressed():
    if (key == 's'):
        saveFrame ( "myProcessing . png")
