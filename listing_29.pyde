l1x1 = 0
l1y1 = 0
l1x2 = 500
l1y2 = 500
flug = 1

def setup ():
    background (255)
    size (500, 500)
    smooth ()

def draw ():
    
    global l1x1, l1y1, l1x2, l1y2, flug, i, k
    
    background (255)
    strokeWeight (50)
    stroke (10, 150, 100, 20)
    line (l1x1, l1y1, l1x2, l1y2)
    
    for i in range (1, 20):
        k = i *50;
        stroke (10, 150, 100, 20+i*10)
        line (l1x1+k, l1y1, l1x2, l1y2-k)
        line (l1x1, l1y1+k, l1x2-k, l1y2)

    l1x1 = l1x1+flug 
    l1y1 = l1y1+flug 
    l1x2 = l1x2-flug
    l1y2 = l1y2-flug
    if ( l1y2<0 or l1y2>500):
        flug = flug *(-1)
