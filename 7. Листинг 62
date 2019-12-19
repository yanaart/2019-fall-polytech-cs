xCoordinate1 = [10]
xCoordinate2 = [10]

def setup():
    
    size (500, 500) 
    smooth ()
    noStroke ()
    
    for i in range (0, 10):
        xCoordinate1.append(35*i+90)
        
    for i in range (0, 10):
        xCoordinate2.append(405-35*i)


def draw():
    
    background (50) 
    
    for i in range(0, 10):
        
        fill (200, 40)
        ellipse (xCoordinate1[i], 200, 15*i, 15*i)
        
        fill (0)
        ellipse (xCoordinate1[i], 200, 3, 3)
        
        fill (200, 40)
        ellipse (xCoordinate2[i], 300, 15*i, 15*i)
        
        fill (0)
        ellipse (xCoordinate2[i], 300, 3, 3)


def keyPressed():
    
    if (key == 's'):
        saveFrame ("myProcessing . png")
