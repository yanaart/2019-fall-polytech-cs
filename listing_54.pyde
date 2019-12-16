class FunnyRect:
    
    cx = 0
    cy = 0 
    fsize = 0
    
    def setCenter(self, x, y):
        
        self.cx = x
        self.cy = y
    
    def setSize(self, size):
        
        self.fsize = size
    
    def render(self):

        ellipse(self.cx, self.cy, self.fsize, self.fsize)
    
    def colors(self, h, n, p):
        
        fill(h, n, p)
        
funnyRect = FunnyRect()
funnyRect1 = FunnyRect()

counter = 0

def setup():
    
    size(600, 600)
    smooth()
    noStroke()
    rectMode(CENTER)
    funnyRect.setSize(50)
    funnyRect1.setSize(20)
    
def draw():
    
    global counter
    
    background(0)
    fill(50)
    
    objX = mouseX + sin(counter)*150
    objY = mouseY + cos(counter)*150
    
    funnyRect.colors(235, 190, 14)
    funnyRect.setCenter(mouseX, mouseY)
    funnyRect.render()
    
    funnyRect1.colors(38, 124, 222)
    funnyRect1.setCenter(objX, objY)
    funnyRect1.render()
    
    counter += 0.05
    
def mouseClicked():
    
    currentSize = funnyRect.fsize
    currentSize += 5
    funnyRect.setSize(currentSize)
