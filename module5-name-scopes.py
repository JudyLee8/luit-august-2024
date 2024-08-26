def show_truth():
    global mysterious_var
    mysterious_var = 'New surprise!'
    print(mysterious_var)

mysterious_var = 'Suprise!'
print(mysterious_var)
show_truth()  
print(mysterious_var) 

def show_truth():
    mysterious_var.append('New surprise!')
    print(mysterious_var)

mysterious_var = ['Suprise!']
print(mysterious_var)
show_truth()  
print(mysterious_var)  