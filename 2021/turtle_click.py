import turtle as t

def say_hello( x,y ):
    print( f'Hello {x} {y}.' )

def drag_turtle( x,y ):
    t.goto( x,y )
    
t.onclick( say_hello )
t.ondrag( drag_turtle )

t.done()
