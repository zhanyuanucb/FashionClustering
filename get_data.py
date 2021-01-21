import json
import requests
import os.path as osp
from tqdm import tqdm

with open("./data/product_data.json") as f:
    data = json.load(f)

print(len(data))

seen = set()
for item in tqdm(data):
    url = item["image_url"]
    image_name = url.split("/")[-1]

    response = requests.get(url)
    with open(osp.join("./data", "images", image_name), "wb") as f:
        f.write(response.content)

#import ipdb; ipdb.set_trace()