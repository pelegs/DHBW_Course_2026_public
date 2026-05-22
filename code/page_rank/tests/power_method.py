import numpy as np

N = 5
A = np.random.randint(-9, 10, size=(N, N))
A = A @ A.T
v = np.random.rand(5)
eval = v @ A @ v
eval_new = 100

itr, max_itrs = 0, 10000
while abs(eval - eval_new) > 1e-10 and itr < max_itrs:
    eval = eval_new
    v = A @ v
    v = v / np.linalg.norm(v)
    eval_new = v @ A @ v
    itr += 1

if itr == max_itrs:
    print(
        " ------ Couldn't converge, take values with a grain of salt ¯\\_(ツ)_/¯ ------"
    )
print(f"Largest eigenvalue: {eval:0.2f}")
print(f"Largest eigenvector: {v}")
print(f"Num iterations: {itr}")

print("-----------------------------------------------------")
print("Using NumPy's linalg.eig() function:")
vals, vecs = np.linalg.eigh(A)
print(f"Largest eigenvalue: {vals[-1]:0.2f}")
print(f"Largest eigenvector: {vecs[-1]}")
print("-----------------------------------------------------")
for vec in vecs:
    print(vec / np.linalg.norm(vec))
