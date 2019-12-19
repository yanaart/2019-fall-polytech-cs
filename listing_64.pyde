num = int(60)

mx = [0 for x in range (num)]
my = [0 for y in range (num)]


def setup():
    
    size(720, 480) 
    noStroke()
    fill(201, 6, 6, 100) 

def draw():
    
    global num
    background(51) 

    which = frameCount%num
    mx[which] = mouseX 
    my[which] = mouseY 
    
    for i in range (0, num):
        index = (which+1+i)%num 
        ellipse (mx[index], my[index], i, i)
