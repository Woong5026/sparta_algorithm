import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    input = sys.stdin.readline().split()

    if input[0] == 'push':
        stack.append(input[1])
    # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif input[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif input[0] == 'size':
        print(len(stack))

    elif input[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    # top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif input[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

