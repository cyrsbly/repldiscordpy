import os
import logging

try:
    import requests
except ModuleNotFoundError:
    os.system('pip3 install requests')
    import requests

try:
    from flask import Flask
except ModuleNotFoundError:
    os.system('pip3 install flask')
    from flask import Flask

from threading import Thread

# ==============================================
# SETUP

app = Flask('discordbot')

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# ==============================================
# KEEP ALIVE

@app.route('/')
def main():
    try:
        project_name = open('README.md').readlines()[0].strip().lstrip('# ')
    except:
        project_name = 'Discord Bot'

    return f'<h3>Running {project_name} on {globals()["web_ip"]}:{globals()["web_port"]}</h3>'

def web():
    port = globals()['web_port']
    app.run(host='0.0.0.0', port=port)

def keep_alive(port=8080):
    ip = requests.get('http://ip.42.pl/raw').text
    globals()['web_ip'] = ip
    globals()['web_port'] = port
    print(f'Running on: {ip}:{port}')
    
    server = Thread(target=web)
    server.start()

# ==============================================
# OTHER

# def code_autostart():
#     bot_file = ''

#     if os.path.isfile('src/bot.py'):
#         bot_file = 'src/bot.py'
#     else:
#         bot_file = 'src/main.py'

#     open(bot_file, 'w').write('')

def run():
    keep_alive()

# this seems unnecessary, but anyways..
if __name__ == '__main__':
    run()
else:
    run()