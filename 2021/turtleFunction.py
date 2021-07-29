import turtle as t

def box(size):
  for _ in range(4):
      t.forward(size)
      t.left(90)

for _ in range(15):
  box(30)
  t.forward(20)
  t.left(15)
  
