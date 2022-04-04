import numpy as np
import math
import random
from entropy import entropy, set_to_dist, I, Hp

import numpy as np
import matplotlib.pyplot as plt

#plt.title("p-I(p)")
#plt.xlabel("p")
#plt.ylabel("I(p")

for i in range(1,1000):
  p = i / 1000.0
  plt.plot(p, I(p), "r.")
 # plt.plot(p, Hp(p), "r.")
plt.show()