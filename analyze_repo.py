import subprocess
from datetime import datetime
from collections import Counter
repo_url = "https://github.com/octocat/Hello-World.git"
subprocess.run(["git","clone",repo_url])
print("Repository clone")
repo_name="Hello-World"
git_output = subprocess.run(
    ["git", "log", "--format=%aI %an"],
    cwd=repo_name,
    capture_output=True,
    text=True
).stdout
lines=git_output.splitlines()

author_count=Counter()
monthly=Counter()
dates=[]
for line in lines:
    date,author=line.split(maxsplit=1)
    date_obj = datetime.fromisoformat(date)
    author_count[author]+=1
    dates.append(date_obj)
    month_key=date_obj.strftime("%Y-%m")
    monthly[month_key]+=1
print(author_count.most_common(5))
print("Commits per month (last 12 months):")
for month in sorted(monthly):
    print(month, monthly[month])

dates.sort()
max_gap=0
for i in range(1,len(dates)):
    gap=(dates[i]-dates[i-1])
    if gap.days>max_gap:
        max_gap=gap.days
print("Longest gap : ",max_gap,"days")

total_commits=len(dates)
total_days=(max(dates)-min(dates)).days+1
avg_per_day=total_commits/total_days
print("Average commits per day:", avg_per_day)