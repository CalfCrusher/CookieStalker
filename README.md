## AJAX cookie stealer + payload generator <img src="https://upload.wikimedia.org/wikipedia/commons/8/8c/Blue_Python_3.6%2B_Shield_Badge.svg" />

**CookieStalker** is just a simple tool that spawn a Flask web server using flask-CORS, generate payload to launch and wait incoming cookies that are sent through **AJAX** that allows us to send a request from the victim's web browser to our cookie stealer **without** refreshing the page and, most importanty, **without** sending additional HTTP traffic to the target server.

The user loads the infected page (reflected or stored injections) and has their cookies stolen silently in the background. The infamous **Sammy Worm** incorporated this technique into its source code.

# Usage:
`$ git clone https://github.com/CalfCrusher/CookieStalker`

`$ cd CookieStalker && pip install -r requirements.txt`

`$ python3 CookieStalker.py`
##

*Please note that i'm not responsible for any damages and illegal use. Don't be a twat!*
