import requests


class Token1:
  def __init__(self):
    self.url = "https://digital.etihad.com/rubie-Fease-no-sall-be-intome-Deat-seemselfe-Mot"
    self.payload : str = None
    self.headers = {
      'accept': 'application/plain; charset=utf-8',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'text/plain; charset=utf-8',
      'origin': 'https://digital.etihad.com',
      'priority': 'u=1, i',
      'referer': 'https://digital.etihad.com/book/cart-new/upsell/0/upsell',
      'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }

  def get_x_d_token(self):
    with open('p_token.txt', 'r') as f:
      lines = f.readlines()
    
    response = requests.request("POST", self.url, headers=self.headers, data=lines[0], timeout=30)
    # print(response.__dict__)
    token = response.json().get('token',"")
    # print(token)
    return token.strip()

  def save_x_d_token(self):
    token = self.get_x_d_token()
    with open('x_d_token.txt', 'w') as f:
      f.writelines(token)

# if __name__ == "__main__":
#   obj = Token1()
#   obj.save_x_d_token()