import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path
import os

# Get the repository root (works both for local and GitHub Actions)
if 'GITHUB_WORKSPACE' in os.environ:
    REPO_ROOT = Path(os.environ['GITHUB_WORKSPACE'])
else:
    # Find git root when running locally
    current_dir = Path(__file__).resolve().parent
    while current_dir != current_dir.parent:
        if (current_dir / '.git').exists():
            REPO_ROOT = current_dir
            break
        current_dir = current_dir.parent
    else:
        raise RuntimeError("Not in a git repository")

# Define paths relative to repository root
CSV_PATH = REPO_ROOT / 'daily_downloads.csv'
IMAGE_PATH = REPO_ROOT / 'download_statistics.png'
README_PATH = REPO_ROOT / 'README.md'
API_URL = "https://huggingface.co/api/datasets/danielrosehill/ifvi_valuefactors_deriv?expand[]=downloads&expand[]=downloadsAllTime"

def update_csv():
    response = requests.get(API_URL)
    data = response.json()
    downloads = data.get('downloads', 0)
    today = datetime.now().strftime('%Y-%m-%d')
    
    try:
        with open(CSV_PATH, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
    except FileNotFoundError:
        rows = [["Date", "Total Downloads"]]
    
    with open(CSV_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        writer.writerow([today, downloads])

def generate_image():
    data = pd.read_csv(CSV_PATH)
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values('Date')

    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Total Downloads'], marker='o', label='Total Downloads')
    plt.title('Download Statistics Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Downloads')
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(IMAGE_PATH)
    plt.close()

def update_readme():
    with open(README_PATH, 'r') as file:
        content = file.read()
    
    start_marker = "## Download Statistics"
    image_text = f"\n\n![Download Statistics](download_statistics.png)\n"
    
    if start_marker not in content:
        content += f"\n\n{start_marker}{image_text}"
    else:
        parts = content.split(start_marker)
        next_section = parts[1].find("##")
        if next_section == -1:
            parts[1] = image_text
        else:
            parts[1] = image_text + parts[1][next_section:]
        content = start_marker.join(parts)
    
    with open(README_PATH, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    update_csv()
    generate_image()
    update_readme()
