import os
import requests

token = os.environ.get("ACMOJ_TOKEN")
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "ACMOJ-Python-Client/2.2"
}
data = {"language": "git", "code": "https://github.com/ojbench/oj-eval-gemini-cli-026-20260407202449"}
response = requests.post("https://acm.sjtu.edu.cn/OnlineJudge/api/v1/problem/2020/submit", headers=headers, data=data)
print(response.status_code)
print(response.text)
