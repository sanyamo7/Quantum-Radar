from transmitter import RadarTransmitter

tx = RadarTransmitter()

signal = tx.transmit()

print("\nSignal Photon\n")
print(signal)

print("\nStored Idler\n")
print(tx.stored_idler())