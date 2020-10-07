import cvxpy as cp
import numpy as np

A = np.array([
    [1,1,1,0,0],
    [0,0,0,1,1],
    [1,0,1,0,1],
    [1,1,1,1,0],
    [0,1,0,1,1]
])

pi = np.array([[0.8,0.3,0.4,0.7,0.6]])
q = np.array([[8,5,7,8,5]])

x = cp.Variable((5,1))
y = cp.Variable(1)
a = cp.sum(cp.multiply(A,x))
b = cp.sum(cp.multiply(x,pi.T))

prob = cp.Problem(
    cp.Maximize(y),
    [
        y <= a - b,
        x <= q,
        cp.min(x) >= 0
    ]
)

prob.solve()

# Print result.
print("\nThe optimal value is", prob.value)
print("A solution x is")
print(x.value)
print("A solution y is")
print(y.value)