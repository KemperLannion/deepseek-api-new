from DeepSeekAPI import *
if __name__ == "__main__":
    with open("tokens") as f:
        DS_SESSION_ID,AUTHORIZATION_TOKEN = f.read().strip().split('\n')
    print(DeepSeekChatExample(DS_SESSION_ID,AUTHORIZATION_TOKEN,input('Your message:'),DeepSeekChatIOMethods.STREAMDOWN,True,True))
