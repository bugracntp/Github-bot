from unicodedata import name
from source_codes.bot import Github
from source_codes.user_info import username, password

"""
This application is a scraping bot for your Github account.
Before the using this application go to user_info.py and enter your account informations 
After then run the __init__.py file. choice your action.
"""
def select_event():
    print("Github bot is running.")
    choice = str(input("""Please choice your action.
    1- Pull your  repostories
    2- Pull your followers list
    3- Pull your following list
    4- Pull last started posts
    5- Close the bot
    """))
    save = input("Do you want save the datas ? Y/N.")
    name = input("Please enter your file name : ") if save.upper() == "Y" else ""
    
    git_bot = Github(username, password)
    if choice == "1":
        git_bot.get_repos(save= True if save.upper() == "Y" else False, name = name)
    elif choice == "2":
        git_bot.get_followers(save= True if save.upper() == "Y" else False, name = name)
    elif choice == "3":
        git_bot.get_followings(save= True if save.upper() == "Y" else False, name = name)
    elif choice == "4":
        git_bot.get_last_started(save= True if save.upper() == "Y" else False, name = name)        

select_event()

