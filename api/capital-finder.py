from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    path = self.path
    url_components = parse.urlsplit(path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)

    if "country" in dic:
      url = "https://restcountries.com/v3.1/name/"
      r = requests.get(url + dic['country'])
      data = r.json()
      message = f"The Capital of {dic['country']} is {data[0]['capital'][0]}"
    elif "capital" in dic:
      url = "https://restcountries.com/v3.1/capital/"
      r = requests.get(url + dic['capital'])
      data = r.json()
      message = f"{dic['capital']} is the Capital of {data[0]['name']['common']}"
    else:
      message = "Define a country or capital please"

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    return
    