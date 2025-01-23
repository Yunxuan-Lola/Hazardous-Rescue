import os
import sys

w1 = os.path.dirname(os.path.realpath(sys.executable))

w2 = os.path.dirname(os.path.dirname(os.path.realpath(sys.executable)))

print(w1)
print(w2)