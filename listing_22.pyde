def setup ():
    
    size (500, 500)
    smooth ()
    background (255)
    noStroke ()
    noLoop ()

def draw ():
    
    for i in range (0,10):
        for j in range (0,10):
            fill (i*20)
            rect(i*40+50,40*j+50,35,35) 
            
    for k in range(0,10):
        for l in range(0,10,2):
            fill(180-20*k)
            rect(k*40+50,40*l+90,35,35)
