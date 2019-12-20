jpg1 = 0
jpg2 = 0
img1 = 0
img2 = 0

def setup():
    
    global jpg1, jpg2
    background(100) 
    smooth()
    size(1200, 700)
    noStroke()
    jpg1 = loadImage ('br1.jpg')
    jpg2 = loadImage ('bread1.gif')

def draw():
    
    global jpg1, jpg2
    
    if ( frameCount == 1):
        image (jpg1 ,0 ,0)

    val1 = int (random (0, 150))
    val2 = int (random (0, 150))

    img1 = jpg1.get(mouseX+val1, 0, 20, height)
    img2 = jpg1.get(mouseX+val2, 0, 5, height)

    blendMode (SUBTRACT)
    tint (255, 20)
    image (img1, mouseX+val1, random(0, height ))

    blendMode ( BLEND )
    noTint()
    image (img2, mouseX-val2, 0)
    
    image (jpg2, 0, 0)

def keyPressed():
    if key == 's':
        saveFrame( "myProcessing" + str(frameCount) + ".jpg ")
