def setup():
    
    size(600, 600)
    noLoop()

def drawMyScene(myColor = float()):
    
    fill(myColor)
    rect(0,50, 150, 50)
    rect(50,0, 50, 150)
    
def draw():
    
    background(20)
    smooth()
    noStroke()
    
    pushMatrix()
    translate(100, 0)
    rotate(PI/4) 
    drawMyScene(180)
    pushMatrix()
    rotate(0)
    translate(330, -60)
    
    rotate(PI/4)
    scale(2)
    drawMyScene(220)
    popMatrix()

    pushMatrix()
    translate(500, 140)
    rotate(-PI/2)
    scale(1.4)
    drawMyScene(80)
    popMatrix()
