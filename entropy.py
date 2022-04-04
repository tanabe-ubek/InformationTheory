import math
import random

def I(p):
  return -math.log(p,2)

def Hp(p):
  return p * I(p) + (1-p) * I(1-p)

def entropy(dist):
  sum = 0.0
  for p in dist:
    sum += p * math.log(p, 2)
  return -sum

def set_to_dist(set):
  hist = {}
  count = 0
  for item in set: #a number
    hist.setdefault(item, 0)
    hist[item]+=1
    count+=1
  dist = []
  #print(hist)
  for v in hist.values():
    dist.append(v / count)
  return dist

d = [0.25, 0.25, 0.25, 0.25]
#print(entropy(d)) # 2.0

S = [0, 0, 0, 1,1,1,2,2,2,2,2,2,2,2,2]
#print(entropy(set_to_dist(S)))

n = 100
sum = 0.0
for i in range(n):
  random.shuffle(S)
  #print(S)
  S0 = S[0:11]
  S1 = S[11:]

  E0 = entropy(set_to_dist(S0))
  E1 = entropy(set_to_dist(S1))
  E = 11/15 * E0 + 4/15 * E1
 # print(E)
  sum += E
sum /= n
#print(sum)

