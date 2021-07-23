import random

movies_list = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 'The Shawshank Redemption', 'Pulp Fiction']

# pick a random choice from a list of strings.
movie = random.choice(movies_list)
print(movie)
# Output 'The Shawshank Redemption'


for i in range(2):
    movie = random.choice(movies_list)
    print(movie)
