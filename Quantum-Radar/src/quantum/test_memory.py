from photon_pair import PhotonPair
from quantum_memory import QuantumMemory

pair = PhotonPair()

memory = QuantumMemory()

memory.store(pair.idler())

print("Stored Idler\n")
print(memory.retrieve())

print("\nMemory Empty?")

print(memory.is_empty())

memory.clear()

print("\nAfter Clearing")

print(memory.is_empty())