from vars import var1, var2

'''
Without SRP
'''

def operation(first_var: float, second_var: float)->None:
    add = first_var + second_var
    subs = first_var - second_var
    return (add, subs)

res = operation(var1, var2)
print(f'Add : {res[0]}')
print(f'Substract : {res[1]}')



'''
With SRP
'''

def add(first_var: float, second_var: float)->None:
    return first_var + second_var
    
def substract(first_var: float, second_var: float)->None:
    return first_var - second_var

print(f'Add : {add(var1, var2)}')
print(f'Substract : {substract(var1, var2)}')
