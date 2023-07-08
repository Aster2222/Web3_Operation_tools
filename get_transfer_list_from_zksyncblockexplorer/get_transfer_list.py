import requests
import pandas as pd
import argparse
import csv
import time
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('target_address', type=str, help='target address')
parser.add_argument('pages', type=int, help='Number of pages')
args = parser.parse_args()

def get_data(target_address, page):
    url = f"https://block-explorer-api.mainnet.zksync.io/address/{target_address}/transfers?pageSize=10&page={page}"
    response = requests.get(url)
    data = response.json()
    
    rows = []
    for item in data['items']:
        timestamp = datetime.fromisoformat(item['timestamp'].replace('Z', '+00:00'))
        formatted_timestamp = timestamp.strftime('%Y/%m/%d %H:%M:%S')
        rows.append((item['from'], item['to'], formatted_timestamp, item['amount']))

    return rows

with open('trasfer_history_list.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['from', 'to', 'timestamp', 'amount']) 

    for page in range(1, args.pages + 1):
        time.sleep(1)
        rows = get_data(args.target_address, page)
        writer.writerows(rows)
