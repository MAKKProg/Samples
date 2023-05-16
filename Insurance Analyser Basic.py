#Objective is to find the cost and major contributing factors for this
import csv


### Functions
#function for getting unique values
def unique(iterable):
	output = []
	for item in iterable:
		if item not in output:
			output.append(item)
			print(item)

#averaging
def average(iterable):
	output = sum(iterable)/len(iterable)
	return output

#Helpful numbers to evaluate the criteria
def stat_numb(iterable):
	print("Average:", Avg:= average(iterable))
	print("Minimum:", Min:= min(iterable))
	print("Maximum:", Max:= max(iterable))
	print("Distance from lowest:", low_mean:= Avg - Min)
	print("Distance from highest:", high_mean:= Max - Avg)
	print("Range:", Max - Min)
	if low_mean and high_mean:
		print("Tendency:", str(tendency:=round(low_mean/high_mean*100)) + "%")
	else:
		print("Tendency: There is only one number") 
		#high value means that there are [high values] outliers, low value means there are [low Values] outliers

#this function checks the relation between two variables once a condition is met. 
#Gives 'individual' details, stat_num details, length of the list that has "True" condition is met, and finally the list itself for better insight
def what_ifs(test, target, value):
	store = []
	for i in range(len(test)):
		if eval("test[i] {}".format(value)):
			store.append(target[i])
			print(people_dict[i])
	stat_numb(store)
	print("Number of item: ", len(store))
	print(sorted(store))

### Code Start Here
# 1 opening the File & Parsing the csv
with open('./insurance.csv') as File:
	insurance_csv = csv.DictReader(File)
	savage = []	
	people_dict = {}
	count = 0
	for item in insurance_csv:
		# saving the output as a dictionary of people reference
		people_dict[count] = item
		count += 1
		for key in item:
			# creating list variables for all different keys
			if not(key in globals()):
				savage.append(key)
				exec("{} = []".format(key))
			eval("{}.append(item[key])".format(key))


#Modifying values to be numerical (if applicable) for easier calculations later on
age = [int(item) for item in age]
bmi = [float(item) for item in bmi]
children = [int(child) for child in children]
charges = [float(charge) for charge in charges] 
smoker_v2 = [1 if item == 'yes' else 0 for item in smoker] # [1] means smoker, [0] means non-smoker 
sex_v2 = [0 if item == 'female' else 1 for item in sex] # [1] means male, [0] means female

#Exploring
stat_numb(bmi)
print("\n______________")
what_ifs(charges, bmi, ">40000")
print("\n______________")
what_ifs(charges, children, "> 60000")