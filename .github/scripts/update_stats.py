import requests
import csv
from datetime import datetime
import os

API_URL = "https://huggingface.co/api/datasets/danielrosehill/ifvi_valuefactors_deriv?expand[]=downloads&expand[]=downloadsAllTime"

def update_csv():
    response = requests.get(API_URL)
    data = response.json()
    downloads = data.get('downloads', 0)
    today = datetime.now().strftime('%Y-%m-%d')
    
    try:
        with open('daily_downloads.csv', mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
    except FileNotFoundError:
        rows = [["Date", "Total Downloads"]]
    
    with open('daily_downloads.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        writer.writerow([today, downloads])
    
    return rows[1:] + [[today, downloads]]  # Return all data except header

def generate_mermaid_chart(data):
    # Create time series chart
    mermaid_syntax = '''```
graph TD
    subgraph Download Statistics
'''
    for date, downloads in data[-7:]:  # Last 7 days
        mermaid_syntax += f'    {date}["{date}: {downloads} downloads"]\n'
    
    mermaid_syntax += '    end\n```'
    return mermaid_syntax

def update_readme(mermaid_chart):
    with open('README.md', 'r') as file:
        content = file.read()
    
    # Find the section between ## Download Statistics and the next ## or end of file
    start_marker = "## Download Statistics"
    if "## Download Statistics" not in content:
        # Add section if it doesn't exist
        content += f"\n\n{start_marker}\n\n{mermaid_chart}\n"
    else:
        # Replace existing section
        parts = content.split(start_marker)
        next_section = parts[1].find("##")
        if next_section == -1:
            parts[1] = f"\n\n{mermaid_chart}\n"
        else:
            parts[1] = f"\n\n{mermaid_chart}\n" + parts[1][next_section:]
        content = start_marker.join(parts)
    
    with open('README.md', 'w') as file:
        file.write(content)

if __name__ == "__main__":
    data = update_csv()
    mermaid_chart = generate_mermaid_chart(data)
    update_readme(mermaid_chart)
