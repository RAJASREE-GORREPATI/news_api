import requests
from send_email import send_email
topic="tesla"
api_key="f419370ad13e4c408db3bd891c5de31f"
url="https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "sortBy=publishedAt&" \
    "apiKey=f419370ad13e4c408db3bd891c5de31f&" \
    "language=en"
request=requests.get(url)
content=request.json()
body = "Subject: Today's news" + "\n"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body= body + article["title"] + "\n" \
              + article["description"]\
              + "\n" + article["url"] + 2*"\n"
body=body.encode("utf-8")
send_email(message=body)