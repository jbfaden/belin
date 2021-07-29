import turtle as t

def sayHello( x,y ):
    print( 'Hello {x} {y}.' )

def dragTurtle( x,y ):
    t.goto( x,y )
    
t.onclick( sayHello )
t.ondrag( dragTurtle )
