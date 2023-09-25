import requests
from send_email import send_email
api_key="f419370ad13e4c408db3bd891c5de31f"
url="https://newsapi.org/v2/everything?" \
    "q=tesla&from=2023-08-25&" \
    "sortBy=publishedAt&apiKey=f419370ad13e4c408db3bd891c5de31f"
request=requests.get(url)
content=request.json()
body=""
for article in content["articles"]:
    if article["title"] is not None:
        body=body+article["title"]+"\n"+article["description"]+2*"\n"
body=body.encode("utf-8")
send_email(body)