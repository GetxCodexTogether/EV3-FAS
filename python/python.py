
def testPy():
    print("Hello World1")
    def fib(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
        print()
    fib(1000)
    print("Hello World2")