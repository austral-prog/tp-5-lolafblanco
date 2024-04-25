def max_of_two(x, y):
    if x<= y:
        return y 
    else: 
        return x
print(max_of_two(1,2)) 
def max_of_three(x, y, z):
    if x<= y and z<= y:
        return y 
    elif x >= y and x>= z:
        return x 
    else:
        return z          
print(max_of_three(1,2,3))
