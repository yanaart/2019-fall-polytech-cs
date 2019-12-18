class MyLine:
    
    centerX = float()
    centerY = float()
    length = float()
    angle = float()
    weight = float()

    def render(self):
        
        x1 = self.centerX - cos(self.angle)*self.length/2
        y1 = self.centerY + sin(self.angle)*self.length/2
        x2 = self.centerX + cos(self.angle)*self.length/2
        y2 = self.centerY - sin(self.angle)*self.length/2
        
        stroke (50, 100) 
        strokeWeight(self.weight)
        line (x1, y1, x2, y2)
        
        stroke(50)
        strokeWeight(5)
        line(x2, y2, x2, y2)
        line(x1, y1, x1, y1)
    
lineObj = MyLine()
counter = float()
radius = float()

def setup():
    
    size(500 , 500) 
    smooth()
    background(255) 

    lineObj.centerX = width/2
    lineObj.centerY = height/2
    lineObj.length = 350
    lineObj.angle = PI/4
    lineObj.weight = 1
    radius = 50

def draw():
    
    global counter, radius
    
    counter += 0.05
    
    if ( counter > TWO_PI ):
        counter = 0
        radius = radius+50
    
    lineObj.centerX = width/2 + sin(counter)*radius 
    lineObj.centerY = height/2 + cos(counter)*radius 
    lineObj.angle = counter*2
    lineObj.render()
