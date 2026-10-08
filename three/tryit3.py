'''wage calculator

'''
start_hour = int(input("Starting hour: "))
start_min = int(input("Starting minute: "))
stop_hour = int(input("Stopping hour: "))
stop_min = int(input("Stopping minute: "))
rate = float(input("Hourly rate: "))
print("---------------------------------------------------")
#show hours input and output
print(f"Worked {start_hour}:{start_min:02d} to {stop_hour}:{stop_min:02d}")
#calculate hours and print total hours korked
start_hour = (start_hour*60) + (start_min)
stop_hour = (stop_hour*60) + (stop_min)
total_hours = ((stop_hour - start_hour) / 60)
print(f"Total hours: {total_hours:.1f}")
#calculate payment and print it
payment = total_hours * rate
print(f"Payment: ${payment:.2f}")