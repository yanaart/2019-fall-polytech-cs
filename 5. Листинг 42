counter = float()
counter1 = float()
cx = float()
cy = float()
nx = float()
ny = float()
cRadius = float(20)

def setup():
    
    size(350, 350)
    smooth()
    background(0)
    strokeWeight(5)

def oneLineDraw (ncx=float(), ncy=float()):
    
    x1 = ncx-sin(counter1)*(100)
    y1 = ncy-cos(counter1)*(100) 
    x2 = ncx+sin(counter1)*(100) 
    y2 = ncy+cos(counter1)*(100) 
    
    line(x1, y1, x2, y2)

def draw():
    
    global counter, counter1, cRadius
    stroke (200,25)

    cx = width /2
    cy = height/2
    
    nx = sin(counter1)*cRadius+cx
    ny = cos(counter1)*cRadius+cy

    x1 = nx - sin(counter)*(150)
    y1 = ny - cos(counter)*(150)
    x2 = nx + sin(counter)*(150)
    y2 = ny + cos(counter)*(150)

    oneLineDraw (x2, y2)
    oneLineDraw (x1, y1)

    counter += 0.1
    
    if (counter > 2*PI):
        counter = 0
   
    counter1 += 0.01
    cRadius += counter/20
    
    if (counter1 > 2*PI):
        counter1 = 0
