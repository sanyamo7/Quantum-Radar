from src.channel.beam_splitter import BeamSplitter

beam = BeamSplitter(0.2)

print(beam)

print()

print("Beam Splitter Matrix\n")

print(beam.matrix())