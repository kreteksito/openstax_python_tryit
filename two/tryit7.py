# Prompt for inputs.
hour = int(input("Current hour (0-23)? "))
minute = int(input("Current minute (0-59)? "))
add = int(input("Trip time (in minutes)? "))

# TODO: Calculate the time.
total_min = hour * 60 + minute + add
hour = total_min // 60 % 24
minute = total_min % 60

# Display the results.
print()
print("Arrival hour is", hour)
print("Arrival minute is", minute)