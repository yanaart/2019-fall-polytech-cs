class MyEllipse:
    
    centerX = float()
    centerY = float()
    angle = float()
    size = float()
    weight = float()

    def __init__(self, cX, cY, cA, eS, Ew):
        
        self.centerX = cX
        self.centerY = cY
        self.angle = cA
        self.size = eS
        self.weight = Ew


    def render(self):
        
        fill (200, self.size/20)
        
        x1 = self.centerX - cos(self.angle)*self.size/2
        y1 = self.centerY + sin(self.angle)*self.size/2
        
        stroke(250, 100) 
        strokeWeight(self.weight)
        ellipse(x1, y1, self.size, self.size)


ellipseObj = 0
counter = float()

def setup():
    global ellipseObj
    size (500 , 500) 
    smooth ()
    background (10) 
    ellipseObj = MyEllipse(width/2, width/2, 0, 150, 1)
    
def draw():
    
    global counter
    
    counter += 0.01
    
    if (counter>TWO_PI):
        counter = 0

    ellipseObj. size = sin(counter*4)* mouseX 
    ellipseObj.render ()
