import turtle as t

def box(size):
  for _ in range(4):
      t.forward(size)
      t.left(90)

r = 0
g = 50
b = 255
for _ in range(25):
  box(30)
  t.forward(20)
  t.left(15)
  r = r + 15
  if r>255: 
    r = 0
  t.color( '#%02x02x02x' % ( r, g, b ) )
  
          
