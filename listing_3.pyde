def setup():
    size(500, 500)
    smooth()
    background(255)
    noLoop()
    fill(50, 80)
    stroke(100)
    strokeWeight(3)

def draw():
    ellipse(250,200,100,100)
    ellipse(250-50,250,100,100)
    ellipse(250+50,250,100,100)
    ellipse(250,250+50,100,100)
