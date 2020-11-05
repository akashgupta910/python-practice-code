import requests

r = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
print(r.text)
print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":6
# }
# r2 = requests.post(url=url, data=data)