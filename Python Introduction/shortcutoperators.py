# 1. Accumulating points across rounds
total_score = 0
round_points = [15, 25, 10]

for points in round_points:
    total_score += points

print(f"Final score: {total_score}")  # Final score: 50

# 2. Counting down remaining retries
retries_left = 3
while retries_left > 0:
    print(f"Attempting connection... ({retries_left} retries left)")
    retries_left -= 1

for points in range(3, 0, -1):
    print(f"Retrying... ({points} retries left)")