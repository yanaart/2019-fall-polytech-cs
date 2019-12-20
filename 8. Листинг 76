jpg1 = 0
jpg2 = 0

def setup():
    
    global jpg1, jpg2
    size(1190, 270)
    background(100)
    smooth()
    colorMode(HSB)
    
    jpg1 = loadImage('bd.jpg')
    jpg2 = loadImage('ba.jpg')
    
def draw():
    
    global jpg1, jpg2
    background(100)
    
    for i in range(10):
        tint(i*25, 150, 255)
        
        if mouseX < i*120 + 120 and mouseX > i*120:
            noTint()
            image(jpg2, i*120, 0)
            
        else:
            image(jpg1, i*120,0)
