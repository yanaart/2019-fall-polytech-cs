jpg1 = 0
jpg2 = 0

def setup():
    
    global jpg1, jpg2
    
    size(600, 800)
    background(100)
    smooth()
    noStroke()
    
    jpg1 = loadImage('sp.jpg')
    jpg2 = loadImage('sp1.jpg')

def draw():
    
    if(frameCount==1):
        image(jpg2, 0, 0)
        
    pointSize = map(mouseX, 0, width, 0, 100)
    pointAlpha = map(mouseY, 0, height, 0, 255)
    
    x=int(random(jpg1.width))
    y=int(random(jpg1.height))
    
    loc = x + y*jpg1.width
    
    jpg1.loadPixels()
    
    r = red(jpg1.pixels[loc])
    g = green(jpg1.pixels[loc])
    b = blue(jpg1.pixels[loc])
    
    fill(r, g, b, pointAlpha)
    ellipse(x, y, pointSize, pointSize)
    
    tint(255, 2)
    image(jpg2, 0, 0)
    
def keyPressed():
    saveFrame("78"+str(frameCount)+".jpg")
