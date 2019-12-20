jpg1 = 0
jpg1 = 0

def setup():

    global jpg1, jpg2
    
    size(500, 500)
    background(100)
    smooth()
    
    jpg1 = loadImage('milos1.png')
    jpg2 = loadImage('milos2.png')
    
def draw():
    
    global jpg1, jpg2
    
    myTintBO = map(mouseX, 0, width, 0, 255)
    myTintVP = map(mouseX, 0, width, 255, 0)
    
    tint(255, myTintVP)
    image(jpg1, 0, 0)
    
    tint(255, myTintBO)
    image(jpg2, 0, 0)
