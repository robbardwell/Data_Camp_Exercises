#1, 
print(3/8)

#2.
#Given the following list(x), what does x[-1] return?
x = [2, 1, -4, 3, -1, 5]

x[-1]

#3.
#Complete the code to return the output
foo = [0.2, 1.7, "A", "Wed", "1.5"]
foo[3:5] = ['E', 'F']
print(foo)
#Required Output
[0.2, 1.7, 'A', 'E', 'F']

#4.
#Which one of these will throw an error?
print(str(True) + "python") #Works
print(True + 0) #Works
print("python" + True) #Error TypeError: can only concatenate str (not "bool") to str
print(True + True + 3) #Works

#5.
#What does ndarray stand for? 
#n dimensional array

#6.
#Complete code to return the output
import numpy as np
data = [1,2,3]
np.array(data)

#7.
#Complete code to return the output
name = "Bob"
surname = " Smith"
print(name + surname)