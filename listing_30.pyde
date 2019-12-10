l1x1 = int (0)
l1y1 = int (0)
l1x2 = int (500)
l1y2 = int (500)
flug = int (1)

mr = float (10)
mg = float (150)
mb = float (100)
    
def setup():
    
    background(255)
    size(500, 500)
    smooth()
    
def draw():
    
    global l1x1, l1y1, l1x2, l1y2, flug, i, k, mr, mg, mb
    
    background(0)
    strokeWeight(120)
    stroke (mr, mg, mb, 25)
    line(l1x1, l1y1, l1x2, l1y2)
    
    for i in range (1, 11):
        k = i*50
        stroke(mr, mg, mb, (255/11)*i)
        line(l1x1+k, l1y1, l1x2, l1y2-k)
        line(l1x1, l1y1+k, l1x2-k, l1y2)
        if (l1x1 == l1x2 or (l1x1+k) == l1x2 or l1x1 == (l1x2-k)):
            mr = random (0, 150)
            mg = random (0, 150)
            mb = random (0, 150)
        
    l1x1 = l1x1+flug
    l1y1 = l1y1+flug
    l1x2 = l1x2-flug
    l1y2 = l1y2-flug
    
    if (l1y2<0 or l1y2>500):
        flug=(-1)*flug
