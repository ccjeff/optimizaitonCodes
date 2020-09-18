import cvxpy as cp
import numpy as np

y = np.array([
    [999,4,999,999,999,999,999,8,999],
    [4,999,8,999,999,999,999,11,999],
    [999,8,999,7,2,4,999,999,999],
    [999,999,7,999,999,14,999,999,9],
    [999,999,2,999,999,999,6,7,999],
    [999,999,4,14,999,999,2,999,10],
    [999,999,999,999,6,2,999,1,999],
    [8,11,999,999,7,999,1,999,999],
    [999,999,999,9,999,10,999,999,999]
    ])

x = cp.Variable((9,9),integer = True)


prob = cp.Problem(cp.Minimize(cp.sum(cp.sum(cp.multiply(y,x),axis = 1), axis = 0)),
                 [
                    cp.sum(x,axis = 0)[0] == 1,
                    cp.sum(x,axis = 1)[8] == 1,
                    cp.sum(x,axis = 0)[1] - cp.sum(x,axis = 1)[1] == 0,
                    cp.sum(x,axis = 0)[2] - cp.sum(x,axis = 1)[2] == 0,
                    cp.sum(x,axis = 0)[3] - cp.sum(x,axis = 1)[3] == 0,
                    cp.sum(x,axis = 0)[4] - cp.sum(x,axis = 1)[4] == 0,
                    cp.sum(x,axis = 0)[5] - cp.sum(x,axis = 1)[5] == 0,
                    cp.sum(x,axis = 0)[6] - cp.sum(x,axis = 1)[6] == 0,
                    cp.sum(x,axis = 0)[7] - cp.sum(x,axis = 1)[7] == 0,
                    cp.min(x) >= 0,
                    cp.max(x) <= 1
                 ])
prob.solve()

# Print result.
print("\nThe optimal value is", prob.value)
print("A solution x is")
print(x.value)
