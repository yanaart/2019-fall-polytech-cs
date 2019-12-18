j=int (random(5,15))
xCoordinate = []

def setup():
    
    global xCoordinate, j
    
    size (500, 500) 
    smooth()
    noStroke()
    
    for i in range (0, j):
        xCoordinate.append(35*i + 90)

def draw():
    
    background (50)
    noStroke() 

    for coordinate in xCoordinate:
        
        fill (random(0,500), random(0,500), random(0,500), 150) 
        ellipse (coordinate, 250, 35, 35)
                
        fill (255)
        ellipse (coordinate, 250, 5, 5)
        
def keyPressed():
    
    if (key == 's'):
        saveFrame ("myProcessing . png")
