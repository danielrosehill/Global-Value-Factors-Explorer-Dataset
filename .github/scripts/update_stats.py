import requests
import csv
from datetime import datetime

API_URL = "https://huggingface.co/api/datasets/danielrosehill/ifvi_valuefactors_deriv?expand[]=downloads&expand[]=downloadsAllTime"
response = requests.get(API_URL)
data = response.json()
downloads = data.get('downloads', 0)
today = datetime.now().strftime('%Y-%m-%d')

try:
    with open('daily_downloads.csv', mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
except FileNotFoundError:
    rows = []

with open('daily_downloads.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    if not rows:
        writer.writerow(["Date", "Total Downloads"])
    else:
        writer.writerows(rows)
    writer.writerow([today, downloads])
