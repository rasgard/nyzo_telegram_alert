from bs4 import BeautifulSoup
import urllib.request 

nyzo_nodes =['https://nyzo.co/status?id=15fa.9f89','https://nyzo.co/status?id=15fa.9f89'] #Nyzo verifier status url
alerts = ''

def bot_sendtext(bot_message):
    bot_token = '' #talk with botfather bot on telegram https://telegram.me/botfather
    your_chatID = ''#talk with https://telegram.me/chatid_echo_bot
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + your_chatID + '&parse_mode=Markdown&text=' + bot_message
    requests.get(send_text)

def alert(message):
    global alerts
    alerts = alerts + message + '\n'
    print('Alert: ' + message)
    return

def make_soup(node):
    nodedata = urllib.request.urlopen(node)
    soupdata = BeautifulSoup(nodedata, "lxml")
    return soupdata

for node in nyzo_nodes:
    soup = make_soup(node)
    status = soup.find('div', {'class':['verifier verifier-active']})
    if status is None:
        alert('Check status of node: ' + node)
    else:
        print('Node in sync: ' + node)

bot_sendtext(alerts)
