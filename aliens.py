# Dictionary

alien_0 = { 'color' : 'green' , 'points' : 5}

print(alien_0['color'])
print(alien_0['points'])

# point earned by the alien_0
new_points = alien_0['points']
print(f'you just earned {new_points} points!')

# positon of the alien

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# get to access value
#if assigned
point_value = alien_0.get('points','no point value is assigned')
print(point_value)
#if not assigned

strength = alien_0.get('strength','no strength is assigned')
print(strength)

#nesting

alien_1 = {'color': 'red' , 'points' : 10}
alien_2 = {'color': 'blue' , 'points' : 8}
alien_3 = {'color': 'yellow' , 'points' : 6}

aliens = [ alien_0, alien_1, alien_2, alien_3 ]

for alien in aliens:
	print(alien)

# make a empty list for aliens

aliens = []
for alien_number in range(30):
	new_alien = {'color' : 'pink', 'points' : 3 , 'speed' : 'slow'}
	aliens.append(new_alien)

# changing the characteristics of the first 3 aliens based on color

for alien in aliens[:3]:
	if alien['color'] == 'pink':
		alien['color'] = 'black'
		alien['points'] = 7
		alien['speed'] = 'fast'
	elif alien['color'] == 'black':
		alien['color'] = 'white'
		alien['points'] = 6
		alien['speed'] = 'medium'
# show the first five aliens

for alien in aliens[:5]:
	print(alien)
print('...')

#show how many aliens have created

print(f"total number of aliens is {len(aliens)}.")