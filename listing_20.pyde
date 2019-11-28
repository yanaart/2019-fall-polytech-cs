def setup():
    
    size(500, 500)
    smooth()
    background(255)
    
    strokeWeight(30)
    noLoop()
    stroke(0,50)

def draw():
    
    for i in range (1,8):
        for k in range (1,4):
            line(i*50, 100*k, 150+(i-1)*50, 100+100*k)
            line(i*50+100, 100*k, 50+(i-1)*50, 100+100*k)
