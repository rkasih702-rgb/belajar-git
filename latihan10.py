x = [1, 2, 3]
def func(x) :
    x[1] = 67 #this affecte the caller!
func(x)
print(x) # prints: (1, 67, 3)