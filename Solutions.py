# Dayana Gonzalez Cruz
# CST-307: Principles of Modeling and Simulation
# WF1100A Dr. Citro
# 10-15-2023
# Project 3: Part 2: Solutions.py
# The purpose of this program is to display the homogeneous and nonhomogeneous solutions discerned in Part 1 of this assignment. 

# Import necessary libraries
import matplotlib.pyplot as plt
import math

# Define lists to keep solution points
EQ1Ys = [0]
EQ2Ys = [0]


# Define Homogeneous Solutions
#----------------------------------------
# 1. y'' + 4y = x ; y(0)=y'(0)=0
# yH = C1*cos(2x) + C2*sin(2x)
# => y = 0
# Given intial values, C1 = C2 = 0 =>
# => y = 0
# Display empty, labeled plot

def DisplayEQ1H():
	plt.ylabel('y')
	plt.xlabel('x')
	plt.title("Homogeneous General Solution to 1. y'' + 4y = x ; y(0)=y'(0)=0")
	plt.show()
# 2. y'' + y = 4; y(0)=y'(0)=0
# yH = C1*cos(x) + C2*sin(x)
# Given intial values, C1 = C2 = 0 =>
# => y = 0
# Display empty, labeled plot

def DisplayEQ2H():
	plt.ylabel('y')
	plt.xlabel('x')
	plt.title("Homogeneous General Solution to 2. y'' + y = 4; y(0)=y'(0)=0")
	plt.show()
#----------------------------------------

# Define Nonhomogeneous solutions by Green's for EQ2 and by Undetermined and Variation for EQ1

# Solution is y(x) = (x/4)-(sin(2x)/8) by Variation and Undetermined Coefficients
# Calculates y for 1000 points and stores
def EQ1NH():
	# y(0) already initialized with list, begin step higher
	x = 0.1
	for i in range(1000):
		# Solve for y
		y = (x/4) - ((math.sin(2*x))/8)
		# Store result
		EQ1Ys.append(y)
		# Step size/increment x by 0.1 each time
		x += 0.1

# Displays graph to user
def DisplayEQ1NH():
	plt.plot(EQ1Ys)
	plt.ylabel('y')
	plt.ylabel('x')
	plt.title("Nonhomogeneous General Solution to 1. y'' + 4y = x ; y(0)=y'(0)=0")
	plt.figtext(0.2, 0.7, "General Solution: y(x) = x/4 - sin(2x)/8")
	plt.show()

# Solution is y(t) = 4(1-cos(t)) by Green's Function, Variation, and Undetermined Coefficients
# Calculates y for 1000 points and stores
def EQ2GF():
	# y(0) already initialized with list, begin step higher
	t = 0.1
	for i in range(1000):
		# Solve for y
		y = 4 * (1- math.cos(t))
		EQ2Ys.append(y)
		# Step size/increment t by 0.1 each time
		t += 0.1

def DisplayEQ2GF():
	plt.plot(EQ2Ys)
	plt.ylabel('y')
	plt.xlabel('t')
	plt.figtext(0.5, 0.112, "General Solution: y(t) = 4(1-cos(t))")
	plt.title("Nonhomogeneous General Solution to 2. y'' + y = 4; y(0)=y'(0)=0")
	plt.show()

#----------------------------------------
# Calculate solutions before allowing user to choose
EQ1NH()
EQ2GF()
#----------------------------------------
# Displays program function to user and requests input 

print("This program displays the solutions to nonhomogeneous differential equations 1. y'' + 4y = x and y'' + y = 4 with intial values y(0) = 0, y'(0) = 0.")
print("")
#----------------------------------------

# Loop showing graphs until user exits
# Must close graph before new prompt appears
# Get input from user to display solution
View = int(input("View Solutions: EQ1H[1], EQ2H[2], EQ1NH[3], EQ2GF[4], or exit[0 or other] => "))
while(View != 0):
	if(View == 1):
		DisplayEQ1H()
	elif(View ==2):
		DisplayEQ2H()
	elif (View == 3):
		DisplayEQ1NH()
	elif (View == 4):
		DisplayEQ2GF()
	else:
		print("Exited")
	View = int(input("View Solutions: EQ1H[1], EQ2H[2], EQ1NH[3], EQ2GF[4], or exit[0] => "))
