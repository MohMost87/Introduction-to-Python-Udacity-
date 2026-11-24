user_engaged = True
idle_cycles = 0

while user_engaged:
    print("Plugin active: monitoring current tab...")
    idle_cycles += 1

    # Simulate user going idle after 3 checks
    if idle_cycles >= 3:
        user_engaged = False

print("Plugin sleeping to conserve resources.")