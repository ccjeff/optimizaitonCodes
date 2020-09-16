import cvxpy as cp
import numpy as np

# minimize c^Tx
# having Ax <= b
c = np.array([-7.8, -7.1])
A = np.array([[1/6, 1/4], [1/2, 1/6]])
b = [90,80]

x = cp.Variable(2)

prob = cp.Problem(cp.Minimize(c.T@x),
                 [A @ x <= b, 
                 x >= 0])
prob.solve()

# Print result.
print("\nThe optimal value is", prob.value)
print("A solution x is")
print(x.value)