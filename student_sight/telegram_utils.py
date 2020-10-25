import requests


class sight_bot():
    def __init__(self):
        self.token = '1142444922:AAEk7mqkxbXlVC6TNWSCootQznh_rX_DRWA'  ## bot token 
        self.chatID = '967526545'

    def send_message(self, message):
        send_text = 'https://api.telegram.org/bot' + self.token + '/sendMessage?chat_id=' + self.chatID + '&parse_mode=Markdown&text=' + message

        response = requests.get(send_text)

        return response.json()
