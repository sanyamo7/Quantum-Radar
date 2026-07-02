from src.radar.target import Target

targets = [

    Target(10,0.9),

    Target(100,0.9),

    Target(1000,0.9),

    Target(5000,0.9)

]

for t in targets:

    print("="*60)

    print(t)