class FunnyRect:
    
    cx = 0
    cy = 0
    fsize = 0
    
    def setCenter (self, x, y):
        
        self.cx = x
        self.cy = y
        
    def setSize (self, size):
        
        self.fsize = size 

    def render(self):
        
        rect (self.cx, self.cy, self.fsize, self.fsize)

funnyRect = FunnyRect()

def setup():
    
    global funnyRect
    size(600, 600) 
    smooth()
    noStroke()
    rectMode(CENTER)
    funnyRect.setSize(50)

def draw():
    
    global funnyRect
    background(255) 
    fill(50)
    funnyRect.setCenter(mouseX, mouseY)
    funnyRect.render()
