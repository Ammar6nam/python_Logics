fruits = {
  'red': ['apple', 'cherry', 'strawberry'],
  'orange':['orange', 'mango', 'peach'],
  'yellow': ['banana', 'lemon']
}
fruits['green'] = ['watermelon']
fruits.update({'green': ['watermelon']})
fruits.pop('yellow')
for color, colored_fruits in fruits.items():
  print(color + ' fruits:')
for fruit in colored_fruits:
    print('- ' + fruit)