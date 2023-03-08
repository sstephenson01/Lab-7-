# Sarah Stephenson and Breanna Eafon
# def fibonacci(n):
#     if n == 0:
#         print("F0 = 0")
#     elif n== 1:
#         print("F1 = 1")
#     else:
#         print("Fn =", fibonacci(n-1)+fibonacci(n-2))
#
# fibonacci(4)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(4))
