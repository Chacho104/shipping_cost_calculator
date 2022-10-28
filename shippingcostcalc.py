# Say I operate a shipping company with 3 shipping packages
# Ground shipping has a flat rate and a weight dependent fee
# Ground premium shipping has a much higher flat fee, no weight
# dependent charge
# Drone shipping has no flat charge but weight dependent charges
# are quite high

# In this project, I will write a program that asks customers for
# weight of their package, calculates the shipping cost for the 3
# shipping packages, communicates the costs, and tells the customer
# the cheapest shipping package

# First, define the package weight variable and assign it any int

weight = 100

# Next, calculate shipping cost for each package

# Ground Shipping Package
# Flat charge is 20.00
# weight <= 2, 1.50 per pound; 2 < weight <= 6, 3.00 per pound; 
# 6 < weight <= 10, 4.00 per pound; weight > 10, 4.75 per pound

if weight <= 2:
    cost_ground = weight * 1.50 + 20.00
elif 2 < weight <= 6:
    cost_ground = weight * 3.00 + 20.00
elif 6 < weight <= 10:
    cost_ground = weight * 4.00 + 20.00
else:
    cost_ground = weight * 4.75 + 20.00

print("Ground Shippping:", "$", cost_ground)

# Ground Shipping Premium Package
# One time flat charge of $ 125

cost_ground_premium = 125

print("Ground Shipping Premium:", "$", cost_ground_premium)

# Drone Shipping Package
# No flat charge
# weight <= 2, 4.50 per pound; 2 < weight <= 6, 9.00 per pound; 
# 6 < weight <= 10, 12.00 per pound; weight > 10, 14.25 per pound

if weight <= 2:
    cost_drone = weight * 4.50
elif 2 < weight <= 6:
    cost_drone = weight * 9.00
elif 6 < weight <= 10:
    cost_drone = weight * 12.00
else:
    cost_drone = weight * 14.25

print("Drone Shipping:", "$", cost_drone)

# Communicate the cheapest shipping package

if cost_ground < cost_ground_premium and cost_ground < cost_drone:
    print("Ground Shipping is the cheapest for your weight!")
elif cost_ground_premium < cost_ground and cost_ground_premium < cost_drone:
    print("Ground Shipping Premium is the cheapest for your weight!")
else:
    print("Drone Shipping is the cheapest for your weight!")
