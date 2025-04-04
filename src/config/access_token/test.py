import requests

url = "https://api-des.etihad.com/v1/security/oauth2/token/initialization"

payload = 'client_id=TEAP1EPUAR97S1aWCpEkWe9L3VvhtBIK&client_secret=j9sP1PK9cEJKbL1o&fact=%7B%22keyValuePairs%22%3A%5B%7B%22key%22%3A%22flow%22%2C%22value%22%3A%22REVENUE%22%7D%2C%7B%22key%22%3A%22market%22%2C%22value%22%3A%22IN%22%7D%2C%7B%22key%22%3A%22originCity%22%2C%22value%22%3A%22DEL%22%7D%2C%7B%22key%22%3A%22originCountry%22%2C%22value%22%3A%22IN%22%7D%2C%7B%22key%22%3A%22currencyCode%22%2C%22value%22%3A%22%22%7D%2C%7B%22key%22%3A%22channel%22%2C%22value%22%3A%22DESKTOP%22%7D%5D%7D&grant_type=client_credentials'
headers = {
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded',
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
  'x-d-token': '3:D7LNXFvQuTY+ZVEVvGvGzw==:Tm3RzdNir7SDlpB+AqwyhdALK9ZVBlkN9D2Jarg8qt8WE4wREWVNTS1Lwn1N613vOLxjvAojVmGQaNpk2gyoLh0gee5S4tVI4rvTMvQeXiNo+6uRxWgWD4ivxKrKDE8Xg0mKOyVQVOIaO77fCu1BnjAa4OJZeykxHQNSozXQsG/FMW9gxdZVBb3HeJWZsU+obSHkjP68nWfH8D5eI8Z2hCKob/8bycu/C8dtW2xBjse0RuIZhQYnKjxnVxj4I/8plx9nqQKhIddtSMzY0xBaf1Q/yo6X5eET46B78qf4lpqQmDer0nSIk+A+hU4e7iwc7zOrdDw5Rva0PMVqFw6wenAudxYVwWzSJKXZ6HWhOH0Q6Zr0o6bhuKPZs3NCroXHvZ1ywwC9v+2MZYX4W48QzHa/oyV+4FNLcVC59z1KRUWANjrLDjl8JCevehGh1Cwxh4Y7ElFK749FNQIUpXOHcNko0FHhn0SOiTpQ7z/ibzN8F2JT71duncIEJMgsjLzuC2tlKiL65THjRh5InDP82YX77MvQv55EPC2NSS1ESYuBaN4Ts1fepSyIFnuU4aRzDdakb398ZvwdXJYnmbp9n9246wk1SENZUlW0B056SitDxJy8rk6TGcox8DML62pzPw2PQUHA0LVr8W3GYIM7mqKsMj8cP28nzAN2EniiE/ODqdzCanG6f/Rof2e1diWNj43HpW9n/IK5/OAvKmEIJUBH7pm2oCSabsrvgvT+AMn0UPrfpLVT2xLji97UPzkyG6rRSjbeys06JPrgXSyVxsxkMOonwKMqLpozk0FVLJGtP8dp7EVYvzIZHzh/mqPh/KS1u5H3Iv0Eq+oR2kuhs1YPqfdRRlwA4oe3F3alQzFe5g58JgmteG3bDYSfC0DU/eELTAN/KnqHRydQxVp6fLQ5rY6phgdmvPpKmLku6l8=:jV2RhtTuEea7UAGESrUGgcYhTOIRQ49wMC7HPQuBRWg=',
  #'Cookie': '_abck=E7220A9601B6C2D103E8D2AB1BABB05C~-1~YAAQTGw/F79LB/SVAQAA0JUb9g1i9FrNCW7bBYo66/6HSvM/9ECcELIFuMIQOMDTuGXk/F1Vr3JeOtHXb5oviRLEFG/ZKyb2xNTNhlA6yF4ATGlYdCQ/rBq24kDzWynX+s1ZmRnSWZm+FJ6UcRx8O+iG3zkaiRE8IdAv983GNkRtXbz9raVJtEyugPKFt6Zed1EqUZTtnOToT95EqswGy89Ja3eDNiuhe6+CW0PR43uzYZxHSdE+P28skGBIHBYC2M5dLDy/AoSJJ5c/vPA057r/r8klz41FfbMq80tMVG4kj/xbEDdCP4UUsKSf0XHRXAuQAwvqAojtWXVnOVEYZupFc9Wlr4Sf49KJtP/UgLXUjkz0ZXOn+U8paBzzorzAWjw/Dxr9LShbYi5YjtaXdi/Ugqe4WhSHNt94LLzwB7sZvyvAgQ3hQW0S3oZc0G7lei7ahKJ1Xco3AQjjKQYT0RfRt6VDHewLMFHhP4acM8Sgcjqbed9q0mBU9P15moXa1uhU4rdaRzhYTcrYEAehE9nrf5ORP4Cr8iWuKPOyBEfTS0qt0QOs6bZIiAzkLzVOD5bjtYiNHZ2xchs7rJC07OMDtP0emPG3IpSSp+nJrS8aS+QDA4uQKGWibbb3JAVMWtuklQ3YERRLBcr0aU5TAiyoSX57heMk1JBst4wANmX5bCer8yx26GryHiMiP78rra9T7lU=~0~-1~-1; ak_bmsc=04DEB688370DE1AF6D14F1F6F623BEA6~000000000000000000000000000000~YAAQTGw/FwVZB/SVAQAASioc9hv+3iKb1U3R4pdQraHBiJCkn2AQ1nADfgjZn6vgTz2KF8WF7P8r4lJV1mujh7m4Iv1X7vHHpm8vGVgIIJrMyGF9z1ZG7s4KR77j7oxNn8Vs5gv+lVVrjah6HYup97+OV0n9NVfEvuT3vxXRqC4IX5ayL9rBnLLUzl2UKIKoJCPjXm5QJ73N84/5OLx8jn99tXEtVeoX0x/IpandO3fTNVy3L7SP5VlfaAR99KU4l4tfNQtmwR+Vtd8oQoOU96KvX8OJwjcITCb3Q2iJE4EcN+AjWbS6saW5eUFNmo7M/cpdm/YhNHS2Q8UR5REtP7Mmd8NhLzVyxffwHw==; bm_sz=5F488BBB1B8D4932D241988F8654AF33~YAAQTmw/F1+JlbCVAQAAS6FB9RvYliJM/p2Md8a2XIYpsXXNjW0xaZpkzgbF8xEv0eRo0Z/e2HQVp9tZesm80OHUYXlYLqpCWO7JKbyEBCAvrNA+LywsnkzVphrzAR4jE7PJTw4IokVzfFaS/bjLGy3P2pWlOtXskL3KEcz5FslWcSaj83BSfwXkU92UFOfi7i7DPLGClQjQI0TxYF49z0pU+BfhLtbvSUVqoN4iult6fsJROV5hgxZTV1AISGPO/eF/ojiy2NI321T6NhaBBBoul4YkJ77quyc4M9oJ8fqGZewBU64HJWVXVl6oPQZ68UKd58jv+I4fOGcZz7pNxpAl2MmUVM+m2kez3/6j5A==~4473141~4272177; incap_ses_738_2864801=aQkKb6/ItyhSeq7jXOc9CswU7WcAAAAArQrKd9CXfT1MSLJiT5oFDg==; nlbi_2864801=3T5IXOPMSlJZIuNXI3VJigAAAADKMU8hKQM/lB0AwEIWNbQI; visid_incap_2864801=DqUF1QanR5u5kDCFnLX8piKerWcAAAAAQUIPAAAAAADvPQkyMk4bg7l0rBic2xic'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
