import requests
import csv
from datetime import datetime
import os
from pathlib import Path

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

API_URL = "https://huggingface.co/api/datasets/danielrosehill/ifvi_valuefactors_deriv?expand[]=downloads&expand[]=downloadsAllTime"
CSV_PATH = REPO_ROOT / 'daily_downloads.csv'
README_PATH = REPO_ROOT / 'README.md'

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
    
    return rows[1:] + [[today, downloads]]

def generate_mermaid_chart(data):
    mermaid_syntax = '''```
graph TD
    subgraph Download Statistics
'''
    seen_dates = set()
    for date, downloads in data[-7:]:
        if date not in seen_dates:
            mermaid_syntax += f'    {date}["{date}: {downloads} downloads"]\n'
            seen_dates.add(date)
    
    mermaid_syntax += '    end\n```'
    return mermaid_syntax

def update_readme(mermaid_chart):
    with open(README_PATH, 'r') as file:
        content = file.read()
    
    start_marker = "## Download Statistics"
    if start_marker not in content:
        content += f"\n\n{start_marker}\n\n{mermaid_chart}\n"
    else:
        parts = content.split(start_marker)
        next_section = parts[1].find("##")
        if next_section == -1:
            parts[1] = f"\n\n{mermaid_chart}\n"
        else:
            parts[1] = f"\n\n{mermaid_chart}\n" + parts[1][next_section:]
        content = start_marker.join(parts)
    
    with open(README_PATH, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    data = update_csv()
    mermaid_chart = generate_mermaid_chart(data)
    update_readme(mermaid_chart)
