import requests
import time
import fade

text = """


 ███▄ ▄███▓▓█████   ██████   ██████  ▄▄▄        ▄████ ▓█████      ██████ ▓█████  ███▄    █ ▓█████▄ ▓█████  ██▀███  
▓██▒▀█▀ ██▒▓█   ▀ ▒██    ▒ ▒██    ▒ ▒████▄     ██▒ ▀█▒▓█   ▀    ▒██    ▒ ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
▓██    ▓██░▒███   ░ ▓██▄   ░ ▓██▄   ▒██  ▀█▄  ▒██░▄▄▄░▒███      ░ ▓██▄   ▒███   ▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
▒██    ▒██ ▒▓█  ▄   ▒   ██▒  ▒   ██▒░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄      ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
▒██▒   ░██▒░▒████▒▒██████▒▒▒██████▒▒ ▓█   ▓██▒░▒▓███▀▒░▒████▒   ▒██████▒▒░▒████▒▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
░ ▒░   ░  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░  ░      ░ ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░  ▒   ▒▒ ░  ░   ░  ░ ░  ░   ░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
░      ░      ░   ░  ░  ░  ░  ░  ░    ░   ▒   ░ ░   ░    ░      ░  ░  ░     ░      ░   ░ ░  ░ ░  ░    ░     ░░   ░ 
       ░      ░  ░      ░        ░        ░  ░      ░    ░  ░         ░     ░  ░         ░    ░       ░  ░   ░     
                                                                                            ░                      

 """
print(fade.purplepink(text)) 


TOKEN = 'token-self' #Enter Your Token
headers = {
    'Authorization': f'{TOKEN}',
}
response = requests.get('https://discord.com/api/v9/users/@me/relationships', headers=headers)
if response.status_code == 200:
    friends_data = response.json()
    for friend in friends_data:

        #friends
        if friend['type'] == 1:
            friend_id = friend['id']

            dm_response = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers=headers, json={'recipient_id': friend_id})
            if dm_response.status_code == 200:
                channel_id = dm_response.json()['id'] #Enter ID
                friend_username = friend.get('username', 'User not Found')
                
                dm_send_response = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json={'content': f'Message'}) #type here your message
                
                if dm_send_response.status_code == 200:
                    print(f"Sent  {friend_username}")
                else:
                    print(f"Error, You don't have any dm {dm_send_response.status_code}")
            else:
                print(f"Ignore This Error: {dm_response.status_code}")
            
            time.sleep(5)
else:
    print(f"Captcha Error {response.status_code}")
    print(f"Capcap Trouble {response.text}")
            
            time.sleep(5)
else:
    print(f"Captcha Error {response.status_code}")
    print(f"Capcap Trouble {response.text}")
