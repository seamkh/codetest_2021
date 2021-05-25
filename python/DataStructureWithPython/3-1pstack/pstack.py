def push(item):
    stack.append(item)

def peek():
    if len(stack) != 0 :
        return stack[-1]

def pop():
    if len(stack) != 0:
        item = stack.pop(-1)

stack = []
push('apple')
push('orange')
push('cherry')
print('사과, 오렌지, 체리 push 후 :\t', end = '')
print(stack,'\t<= top')
print('top 항목: ', end = '')
print(peek())
push('pear')
print('배 push 후 :\t\t', end = '')
print(stack, '\t<= top')
pop()
push('grape')
print('pop(), 포도 push 후 :\t', end = '')
print(stack, '\t<- top')

