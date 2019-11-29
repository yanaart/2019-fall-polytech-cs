def setup():
    size(500, 500)
    smooth()
    noLoop()
    noStroke()
    ellipseMode(CENTER)


def draw():
    background(255)
    border = float (50)
    
    nw = (width -2*border)
    nh = float(height -2*border)
    number = float(5)
    nWstep = float(nw / number)
    nHstep = float(nh / number)
    for i in range (0, 5):
        for j in range (0, 5):
            x = float(border + j*nWstep + nWstep/2)
            y = float(border + i*nHstep + nHstep/2)
            size = float(5 + (j+i)*10)
            mColor = float(size*1.5)
            fill(mColor , 20, 50)
            ellipse(x, y, size , size)
            fill(250)
            ellipse(x, y, 3, 3)
