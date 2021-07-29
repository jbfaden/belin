# This shows that you can use the same variable name "_" with nested loops
i = 0
for _ in range(4):
    for _ in range(5):
        i = i + 1
        print( i )
    _ = 5    
