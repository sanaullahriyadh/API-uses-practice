import requests
job_board_url = 'https://www.arbeitnow.com/api/job-board-api'
res = requests.get(job_board_url)
job_details = res.json()
data = job_details.get('data')[0].get('title')
print(data)