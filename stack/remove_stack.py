import stack_array

srcStack = stack_array.ArrayStack()
srcStack.push(1)
srcStack.push(2)
srcStack.push(3)
srcStack.push(4)
print("src stack before", srcStack.get())

def remove_all_elements(stack):
    if stack.is_empty():
        return
    else:
        stack.pop()
        remove_all_elements(stack)

remove_all_elements(srcStack)

print("src stack after", srcStack.get())