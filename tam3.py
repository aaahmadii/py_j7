import random


choices = ['hello', 'yello', 'mello', 'hall']


random_list = [random.choice(choices) for _ in range(100)]

print(random_list)
