i = 0
k = 1
flug = 1

def setup ():
    
    size (500, 500)
    smooth ()
    background (0)
    strokeWeight (1)

def draw ():
    
    global i, k, flug
    stroke (i, 20)
    
    if ( flug == 1):
        line ( mouseX, mouseY, 500, random (0, 500))
    else: 
        line ( mouseX, mouseY , 0, random (0 ,500))

    i = i + k
    
    if (i == 255):
        k = -1
        
    if (i == 0):
        k = 1

def keyPressed ():
    
    if (key == 'q'):
        flug = flug*(-1)

    if (key == 's'):
        saveFrame ( " myProcessing . png " )
