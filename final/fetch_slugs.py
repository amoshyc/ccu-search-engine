import json
import time
import random
import urllib.request
from tqdm import tqdm

targets = [
    'https://tasty.co/api/recipes/recent?size=20&from={}&page={}&from_offset=1&__amp_source_origin=https%3A%2F%2Ftasty.co'.format(idx, idx // 20)
    for idx in range(80)
]

slugs = []
for url in tqdm(targets):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read())
    slugs.extend(item['slug'] for item in data['items'])
    time.sleep(random.randint(2, 6))

    slugs = list(slugs)
    with open('slugs.json', 'w') as f:
        json.dump(slugs, f, indent=2, ensure_ascii=False)
