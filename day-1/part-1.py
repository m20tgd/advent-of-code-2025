
dial_position = 50
zero_count = 0

# Open file and read line by line
with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        # Get direction and clicks
        [direction, *clicks] = list(line)
        clicks = int(''.join(clicks))
        # Make clicks negative if direction is 'L'
        if direction == 'L':
            clicks = clicks * -1
        # Move dial
        dial_position = (dial_position + clicks) % 100
        # Increment zero count if dial is at 0
        if dial_position == 0:
            zero_count += 1

# Print final results
print(f"Final Dial Position: {dial_position}")
print(f"Number of times dial was at 0: {zero_count}")
