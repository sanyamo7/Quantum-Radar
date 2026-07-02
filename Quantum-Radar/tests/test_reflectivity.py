from src.channel.beam_splitter import BeamSplitter

values = [0.01, 0.1, 0.25, 0.5, 0.75, 1.0]

for value in values:

    beam = BeamSplitter(value)

    print("=" * 60)

    print(beam)

    print(beam.matrix())