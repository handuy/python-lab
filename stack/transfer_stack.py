import stack_array

srcStack = stack_array.ArrayStack()
srcStack.push(1)
srcStack.push(2)
srcStack.push(3)
srcStack.push(4)
print("src stack", srcStack.get())

dstStack = stack_array.ArrayStack()
while srcStack.is_empty() == False:
    dstStack.push(srcStack.pop())

print("dst stack", dstStack.get())