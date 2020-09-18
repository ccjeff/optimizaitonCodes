import cvxpy as cp
import numpy as np

x = cp.Variable((5,5),integer = True)
y = np.array([[999,10,12,17,34],
                [10,999,18,8,46],
                [12,18,999,9,27],
                [17,8,9,999,20],
                [34,46,27,20,999]])


prob = cp.Problem(cp.Minimize(cp.sum(cp.sum(cp.multiply(y,x),axis = 1), axis = 0)),
                 [
                    -cp.sum(x,axis = 1)[0] + cp.sum(x,axis = 0)[0] >= 200 - 130,
                    -cp.sum(x,axis = 1)[1] + cp.sum(x,axis = 0)[1] >= 400 - 385,
                    -cp.sum(x,axis = 1)[2] + cp.sum(x,axis = 0)[2] >= 600 - 400,
                    -cp.sum(x,axis = 1)[3] + cp.sum(x,axis = 0)[3] >= 200 - 480,
                    -cp.sum(x,axis = 1)[4] + cp.sum(x,axis = 0)[4] >= 300 - 610,
                    cp.diag(x) == 0,
                    cp.min(x) >= 0
                 ])
prob.solve()

# Print result.
print("\nThe optimal value is", prob.value)
print("A solution x is")
print(x.value)
