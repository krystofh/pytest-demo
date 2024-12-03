from functions import add, subtract, multiply, divide
from service import get_todos

if __name__ == "__main__":
    print("Hi")
    add(1, 2)
    data = get_todos()
    print(data[0])
