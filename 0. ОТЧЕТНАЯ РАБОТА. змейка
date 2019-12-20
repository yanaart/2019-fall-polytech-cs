x = []
y = []
w = 30
h = 30
bs = 20
dir = 2
ax = 12
ay = 10
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
gameover=False

def setup():
    
    global x, y
    size(600, 600)
    x.append(5)
    y.append(5)

def draw():
    
    global w, h, bs, dir,ax,ay, dx, dy, gameover, x, y
    
    background(255)
    
    for i in range(w):
        line(i*bs, 0, i*bs, height)
        
    for i in range(h):
        line(0, i*bs, width, i*bs)
        
    for i in range(len(x)):
        fill(0, 255, 0)
        rect(x[i]*bs, y[i]*bs, bs, bs)
        
    if not gameover:
        fill(255, 0, 0)
        rect(ax*bs, ay*bs, bs, bs)
        
        if frameCount%5==0:
            x.insert(0, x[0]+dx[dir])
            y.insert(0, y[0]+dy[dir])
            if not (x[0]==ax and y[0]==ay):
                x.pop()
                y.pop()
            else:
                ax = int(random(0, w))
                ay = int(random(0, h))
                
        if x[0] < 0 or y[0] < 0 or x[0] >= w or y[0] >= h:
            gameover = True
            
        for i in range(1, len(x)-1, 1):
            if x[0] == x[i] and y[0]==y[i]:
                gameover = True
                if x[0]==ax and y[0]==ay:
                    ax = int(random(0, w))
                    ay = int(random(0, h))
                else:
                    x.pop()
                    y.pop()
                break
    else:
        
        fill(120, 8, 8)
        textSize(50)
        textAlign(CENTER)
        text("GAME OVER. Press space", width/2, height/2)
        
        if keyPressed and key==' ':
            x = list()
            y = list()
            x.append(5)
            y.append(5)
            gameover = False
            
def keyPressed():
    global x, y, dir
    if key=='s':
        nd = 0
    elif key=='w':
        nd = 1
    elif key=='d':
        nd = 2
    elif key=='a':
        nd = 3
    else:
        nd = -1
    dir = nd
        
