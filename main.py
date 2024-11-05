import requests
from send_email import send_email

topic = "tesla"
api_key = "27e29348c7584fceae25983b5216d7fb"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-10-05&" \
      "sortBy=publishedAt&" \
      "apiKey=27e29348c7584fceae25983b5216d7fb&" \
      "language=en"

response = requests.get(url)

content = response.json()

body = ""
for article in content["articles"][:20]:
    title = article["title"] if article["title"] is not None else ""
    description = article["description"] if article["description"] is not None else ""

    body += "Subject: Today's News" + title + "\n" + description + "\n" + article["url"] + "\n\n"

body = body.encode("utf-8")
send_email(message=body)
