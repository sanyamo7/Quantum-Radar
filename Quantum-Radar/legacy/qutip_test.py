from qutip import basis, tensor

# |0>
zero = basis(2, 0)

# |1>
one = basis(2, 1)

print("|0>")
print(zero)

print()

print("|1>")
print(one)

print()

# |00>
state = tensor(zero, zero)

print("|00>")
print(state)