def func():
    print("func in one.py")


print("Top level one.py")

if __name__ == '__main__':
    print("one.py is run diraclty")
else:
    print("one.py was impported")
