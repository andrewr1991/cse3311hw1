from typing import TypeVar, Generic
from typing import AnyStr
from typing import Iterator
import numpy as np
from numpy import linalg as la

def add(x: int, y: int) -> int:
    if (type(x) and type(y)) == type(int):
        print("int")
    return x + y

def subtract(x: int, y: int) -> int:
    return x - y

def multiply(x: int, y: int) -> int:
    return x * y

def divide(x: int, y: int) -> int:
    return x / y

def addFloats(x: float, y: float) -> int:
    return x + y

def evenOrOdd(x: int) -> int:
    if (x % 2 == 0):
        return x, "It's even!"
    else:
        return x, "It's odd!"

    print("End of function!")

# Function to concatenate 3 strings
def concatenate(str1: AnyStr, str2: float, str3: AnyStr) -> AnyStr:
    return str1 + str2 + str3

class Enemy:
    def __init__(self, health, position):
        self.health = health
        self.position = position
    def getEnemyHealth(self) -> int:
        return self.health
    def getEnemyPosition(self) -> float:
        return self.position

class Ninja(Enemy):
    def starAttack(self) -> float:
        return 1.5

# Practice with NumPY
perturbed = np.array([[0], [0], [0.5]])

A1 = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.91]])
b1 = np.array([[1.00], [2.80], [4.61]])
xa = la.solve(A1, b1)

b1Pert = np.add(b1, perturbed)
xaPert = la.solve(A1, b1Pert)

A2 = np.array([[0.1, 0.2, 0.3], [0.6, 0.5, 0.4], [0.1, 0.5, -0.8]])
b2 = np.array([[1.0], [3.2], [0.5]])
xb = la.solve(A2, b2)

b2Pert = np.add(b2, perturbed)
xbPert = la.solve(A2, b2Pert)

def objExists(obj: Enemy) -> None:
    if ('obj' in locals() or 'obj' in globals()):
        print("Object does exist")
    else:
        print("Object doesn't exist!")
        obj.starAttack()

type = TypeVar('type')

class GenericList(Generic[type]):
    def __init__(self) -> None:
        self.items: List[type] = []

    def appendToList(self, item: type) -> None:
        self.items.append(item)

    def printList(self) -> None:
        for element in self.items:
            print(element)

# Algorithm practice with NumPy
example1DArray = [1, 2, 3, 4, 5, 6, 7, 8, 3, 5, 6, 3, 2, 5, 7, 8]
emptyNPArray = []
data = np.array([])

for x in example1DArray:
    f = (440) * 2**((x - 49) / 12)
    emptyNPArray.append(f)

x = np.arange(0, 1, 1 / 8000)
x = x[0 : 4000]

for f in emptyNPArray:
    y = np.cos(2 * np.pi * f * x)
    data = np.append(data, y)
