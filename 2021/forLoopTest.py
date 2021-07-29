# This shows that you can use the same variable name "_" with nested loops
i = 0
for _ in range(10):
    for _ in range(10):
        i = i + 1
        print( i )
    _ = 10    
