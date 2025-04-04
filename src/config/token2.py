import requests
from token1 import Token1
url = "https://api-des.etihad.com/v1/security/oauth2/token/initialization"

x_d_token = Token1().get_x_d_token()

print(x_d_token)
# with open('solutions.txt', 'r') as f:
#     token = f.readlines()

# print(type(token[0]))

payload = 'client_id=TEAP1EPUAR97S1aWCpEkWe9L3VvhtBIK&client_secret=j9sP1PK9cEJKbL1o&fact=%7B%22keyValuePairs%22%3A%5B%7B%22key%22%3A%22flow%22%2C%22value%22%3A%22REVENUE%22%7D%2C%7B%22key%22%3A%22market%22%2C%22value%22%3A%22IN%22%7D%2C%7B%22key%22%3A%22originCity%22%2C%22value%22%3A%22DEL%22%7D%2C%7B%22key%22%3A%22originCountry%22%2C%22value%22%3A%22IN%22%7D%2C%7B%22key%22%3A%22currencyCode%22%2C%22value%22%3A%22%22%7D%2C%7B%22key%22%3A%22channel%22%2C%22value%22%3A%22DESKTOP%22%7D%5D%7D&grant_type=client_credentials'
headers = {
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'origin': 'https://digital.etihad.com',
  'priority': 'u=1, i',
  'referer': 'https://digital.etihad.com/',
  'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
  'x-d-token': x_d_token,
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
