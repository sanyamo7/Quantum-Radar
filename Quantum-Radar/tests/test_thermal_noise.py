from src.channel.thermal_noise import ThermalNoise

noise = ThermalNoise(
    dimension=2,
    mean_photons=0.2
)

rho = noise.state()

print("\nThermal Density Matrix\n")
print(rho)