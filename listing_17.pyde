def setup ():
    size (500, 500)
    smooth ()
    background (255)
    strokeWeight (30)
    noLoop ()

def draw ():
    stroke (20)
    for i in range(1,8):
        line (i*50, 200, 150+(i-1)*50, 300)
