import stack_array

srcStack = stack_array.ArrayStack()
srcStack.push(1)
srcStack.push(2)
srcStack.push(3)
srcStack.push(4)
print("src stack before", srcStack.get())

tmpStack1 = stack_array.ArrayStack()
while srcStack.is_empty() == False:
    tmpStack1.push(srcStack.pop())

tmpStack2 = stack_array.ArrayStack()
while tmpStack1.is_empty() == False:
    tmpStack2.push(tmpStack1.pop())

while tmpStack2.is_empty() == False:
    srcStack.push(tmpStack2.pop())

print("src stack after", srcStack.get())