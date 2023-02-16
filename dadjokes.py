import requests
from random import choice

url="https://icanhazdadjoke.com/search"
search_term = input("Let me tell you a funny joke!!! Give me a topic: ")



res = requests.get(
    url,
    headers={
        "Accept": "application/json",
    },
    params={
        "term": search_term
    }
    
).json()

result = res['results']
random_joke_num = len(result)
random_joke = choice(result)['joke']

if random_joke_num == 0:

    print(f"I don't have any joke about {search_term}. Please try something else \n{random_joke}")
elif random_joke_num == 1:
    print(f"I have {random_joke_num} joke about {search_term}. Here it is: \n{random_joke}")
else:
    print(f"I have {random_joke_num} jokes about {search_term}. Here's one: \n{random_joke}")

