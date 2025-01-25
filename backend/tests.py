import requests

url = 'https://solana-mainnet.gateway.tatum.io/'
headers = {
  'accept': 'application/json',
  'content-type': 'application/json',
  'x-api-key': 't-677d28e76120e827ba1ef48b-2513dd38168e4184941d82ea'
}
body = {
  'jsonrpc': '2.0',
  'method': 'getVersion',
  'id': 1
}

response = requests.post(url, headers=headers, json=body)
print(response.text)