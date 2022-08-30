import stack_array

original_list = [1, 2, 1, 4, 2]
newStack = stack_array.ArrayStack()
for item in original_list:
    newStack.push(item)

reversed_list = []
while newStack.is_empty() == False:
    reversed_list.append(newStack.pop())

print(reversed_list)