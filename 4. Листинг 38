flug=50

def setup():
    
    size(500, 500)
    smooth()
    background(150)
    strokeWeight(1)

def draw():
    
    fill(flug, random(0, 50))
    myY2 = mouseY + random (-10, 10)
    myX2 = mouseX + random (-10, 10)
    ellipse (mouseX, mouseY, myX2/10, myY2/10)

def keyPressed():
    
    if (key == 'w'):
        flug = 255

    if (key == 'b'):
        flug = 0

    if (key == 's'):
        saveFrame ("myProcessing.png")
