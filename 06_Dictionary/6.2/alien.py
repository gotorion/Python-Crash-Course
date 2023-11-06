alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['color'] = 'yellow'
print(alien_0)

alien_0['speed'] = 'medium'
print(alien_0)

del alien_0['points']
print(alien_0)

#print(alien_0['points'])  # error
print(alien_0.get('points'))