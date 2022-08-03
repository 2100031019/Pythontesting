

import pytest
import random
p=random.randbytes(3)
print(p)
p=random.randint(10,100)
print(p)
def sum_of_Number(n):
    return (n*(n+1))/2
def test():
    assert sum_of_Number(5)==15

def test():
    assert sum_of_Number(5)==15

import re
txt ="Use of the python in machine Learning"
x=re.search("^Use.*Learning$", txt)
if (x):
    print("YES! we have a match")
else:
    print("No match")
x=re.findall("in",txt)
print(x)