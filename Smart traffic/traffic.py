import time, random

lanes = ["North", "South", "East", "West"]

def traffic_density():
    return {lane: random.randint(0, 100) for lane in lanes}

def emergency_vehicle():
    return random.choice(lanes) if random.random() < 0.1 else None

def green_time(density):
    return 5 + 25 * density / 100  # 5 to 30 seconds

while True:
    densities = traffic_density()
    print("Traffic densities:", densities)

    emergency = emergency_vehicle()
    if emergency:
        print(f"Emergency vehicle on {emergency}. Green for 20s.")
        time.sleep(20)
    else:
        max_lane = max(densities, key=densities.get)
        t = green_time(densities[max_lane])
        print(f"Green light to {max_lane} for {t:.1f}s.")
        time.sleep(t)

    print("All RED for 2s.\n")
    time.sleep(2)
