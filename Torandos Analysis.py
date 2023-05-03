names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville',
 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie',
 'Beulah', 'Camille','Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 
 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 
 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

months = ['October', 'September', 'September', 'November', 'August', 'September',
'September', 'September', 'September', 'September', 'September', 'October',
'September', 'August', 'September', 'September', 'August', 'August', 'September',
'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
'October', 'August', 'September', 'October', 'September', 'September', 'October']

years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938,
 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979,
 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005,
 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

max_sustained_winds = [165, 160, 160, 175, 160, 160, 
 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 
 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 
 175, 175, 165, 180, 175, 160]

areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'],
['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'],
['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'],
['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'],
['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'],
['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'],
['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', 
'306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', 
'10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# Update Recorded Damages
def damage_function(damages_list):
  conversion = {"M": 1000000,
             "B": 1000000000}
  updated_damages = []
  for item in damages_list:
    if item == "Damages not recorded":
        updated_damages.append(item)
    else:
      last_char = item[-1]
      updated_damages.append(float(item[:-1]) * conversion[last_char])
  return updated_damages
new_damage_list = damage_function(damages)

# Creating a Dictionary for the Tornados 
zipper = list(zip(names,months,years,max_sustained_winds,areas_affected,damages,deaths))

def dict_summary(Z):
    dict_container = {}
    for item in Z:
        dict_container[item[0]] = {"Name": item[0],
         "Month":item[1], "Year":item[2],
         "Wind":item[3], "Areas":item[4],
         "Damage":item[5], "Death":item[6]}
    return dict_container

tornado_dict = dict_summary(zipper)

# Organizing by Year
def dict_summary_year(Z):
    dict_container = {}
    for item in Z:
        dict_container[item[2]] = {"Name": item[0],
         "Month":item[1], "Year":item[2],
         "Wind":item[3], "Areas":item[4],
         "Damage":item[5], "Death":item[6]}
    return dict_container
tornado_dict_year = dict_summary_year(zipper)

# Counting Damaged Areas
def count_damaged(areas):
    
    raw_areas = []
    output = {}
    for item in areas:
        for mini_item in item:
            raw_areas.append(mini_item)
    for item in raw_areas:
        output[item] = raw_areas.count(item)
        
    return output

#Most affected area
def most_affected_areas(areas):
    items_list = sorted([(value,key) for key,value in areas.items()],reverse=True)
    values_list = sorted(areas.values,reverse=True)
    output = []
    for i in range(values_list.count(values_list[0])):
        output.append(values_list[i][1])
    return output

# Calculating the Deadliest Hurricane
def max_death(names,deaths):
    location = deaths.index(max(deaths))
    return (names[location], deaths[location])

# Rating Hurricanes by Mortality
def mortality_rating(names, deaths):
    mortality_scale = {0: 0,1: 100,2: 500,3: 1000,4: 10000}
    values = list(mortality_scale.values())
    output = {}
    for death in deaths:
        location = deaths.index(death)    
        if death in values:
            output[names[location]] = values[location]
        else:
            temp_values = values[:]
            temp_values.append(death)
            rank = sorted(temp_values).index(death)
            output[names[location]] = rank
    return output
ratings = mortality_rating(names, deaths)

# Calculating Hurricane Maximum Damage
def max_damage(names, damages):
    #Modifying the damages list so that they are all numbers
    cleaned_damages = [item if type(item) != str else 0 for item in damages]
    location = cleaned_damages.index(max(cleaned_damages))
    return (names[location],max(cleaned_damages)),cleaned_damages
    
Max, clean_damage = max_damage(names,new_damage_list)

# categorize hurricanes in new dictionary with damage severity as key
def damage_rating(names, damages):
    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
    
    values = list(damage_scale.values())
    output = {}
    for damage in damages:
        location = damages.index(damage)    
        temp_values = values[:]
        temp_values.append(damage)
        rank = sorted(temp_values).index(damage)
        output[names[location]] = rank
    return output
