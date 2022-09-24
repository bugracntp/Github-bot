from bot import Github
from user_info import username, password

def select_event():
    print("Github bot is running.")
    choice = str(input("""Choice your process
    1- Pull your  repostories
    2- Pull your followers list
    3- Pull your following list
    4- Pull last started posts
    5- Close the bot
    """))
    save = input("Do you want save the datas ? Y/N.")
    
    git_bot = Github(username, password)
    if choice == "1":
        git_bot.get_repos(save= True if save.upper() == "Y" else False)
    elif choice == "2":
        git_bot.get_followers(save= True if save.upper() == "Y" else False)
    elif choice == "3":
        git_bot.get_followings(save= True if save.upper() == "Y" else False)
    elif choice == "4":
        git_bot.get_last_started(save= True if save.upper() == "Y" else False)        

select_event()

