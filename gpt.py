import matplotlib.pyplot as plt

def bellman(s, a, V, gamma, p):
    sHeads = s + a
    sTails = s - a
    
    
    vReturn = p*V[sHeads] + (1-p)*V[sTails]
    
    return vReturn

gamma = 1
p = 0.4
theta = 1.0e-8

numNonTermStates = 99
numStates = numNonTermStates + 2 # 101 states

# initialize V with all 0s
V = [0 for i in range(numStates)]
V[0] = 0 # no money left
V[-1] = 1 # Final state of 100 has value +1 

# 1.7976931348623157e+308
delta = float("inf")
numIterations = 0

while delta > theta:
    numIterations += 1
    delta = 0
    for Si in range(1, numStates-1):
        v = V[Si]
        
        s = Si

        actions = [i for i in range(0, min(s, (numStates-1)-s+1))]
        Q = [-100 for i in range(len(actions))]
        #print(actions)
        for Ai in range(0, len(actions)):
            Q[Ai] = bellman(s, actions[Ai], V, gamma, p)
        
        V[Si] = max(Q)
        #print(V[Si])
        delta = max(delta, abs(v-V[Si]))

    if numIterations == 1:
        x = [i for i in range(0, 101)]
        plt.plot(x, V)
