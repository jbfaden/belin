import turtle as t

def box(size):
  for _ in range(4):
      t.forward(size)
      t.left(90)

for _ in xrange(15):
  box(30)
  forward(100)
  left(15)
  
