xCoordinate = []

def setup():
    
    size(500, 500) 
    smooth()
    noStroke()
    myInit()


def myInit():
    
    print('New coordinates:')
    
    for i in range(0, 30):
        xCoordinate.append(250+int(random(-100, 100))) 
        print(xCoordinate[i])

def draw():
    
    global xCoordinate
    background (30) 
    
    for i in range(0, 30):
        fill(250, 40) 
        ellipse (xCoordinate[i], 250, 5, 5)
        
        fill (250, 40)
        ellipse (xCoordinate [i], 250, 10*i, 10*i)

    if mouseX > 250:
        xCoordinate = []
        myInit ()


def keyPressed():
    
    if key == 's':
        saveFrame ("myProcessing . png")
