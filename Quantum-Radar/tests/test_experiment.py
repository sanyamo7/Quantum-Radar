from src.simulation.experiment import QuantumRadarExperiment

experiment = QuantumRadarExperiment(

    eta=0.85,

    reflectivity=0.2,

    mean_photons=0.1,

    distance=1500

)

result = experiment.run()

print("=" * 60)

print("SIGNAL")

print(result["signal"])

print("=" * 60)

print("IDLER")

print(result["idler"])

print("=" * 60)

print("CHANNEL OUTPUT")

print(result["channel"]["after_loss"])

print("=" * 60)

print("THERMAL STATE")

print(result["channel"]["thermal"])

print("=" * 60)

print("TARGET")

print(result["target"])