from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class Github:
    def __init__(self, username, password):
        # this line for open your web browser. if you are useing an other browser find your driver file from :
        # https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
        self.browser = webdriver.Chrome("chromedriver.exe")
        self.username = username
        self.password = password
    # sign in method (take the username and password values and sign in to your account).
    def sign_In(self):
        self.browser.get("https://github.com/login")

        time.sleep(1)
        # Take input boxes from the page.
        username_text = self.browser.find_element(By.XPATH,"//*[@id='login_field']")
        password_text = self.browser.find_element(By.XPATH,"//*[@id='password']")

        # Sending your username and password.
        username_text.send_keys(self.username)
        password_text.send_keys(self.password)

        time.sleep(1)
        # take the submit button and login your account.
        signin_btn = self.browser.find_element(By.XPATH,"//*[@id='login']/div[4]/form/div/input[12]")
        signin_btn.click()

    def get_repos(self, save, name):
        self.sign_In()
        time.sleep(1)
        dropdown = self.browser.find_element(By.XPATH,"/html/body/div[1]/header/div[7]/details")
        dropdown.click()
        time.sleep(1)

        repos_btn = self.browser.find_element(By.XPATH,"/html/body/div[1]/header/div[7]/details/details-menu/a[2]")
        repos_btn.click()
        time.sleep(1)

        # pulling the repostories elements.
        repos = self.browser.find_elements(By.CSS_SELECTOR,"#user-repositories-list > ul > li > div.col-10.col-lg-9.d-inline-block")
        repo_list=[]
        # repos elements convert to a list 
        for repo in repos:
            repo_list.append(repo.text)

        # if there is a next page for elements it will surf and take all of them
        while True:
            # take the button of next and previsous button
            links = self.browser.find_elements(By.CSS_SELECTOR,"#user-repositories-list > div > div > a")
            # checkt the list when there is no button, it will break this loop
            if len(links) == 0:
                break
            # if we have a button it will checkt it and if it is a next button click on it of isn't it will break the loop
            elif len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(2)
                    repos = self.browser.find_elements(By.CSS_SELECTOR,"#user-repositories-list > ul > li > div.col-10.col-lg-9.d-inline-block")
                    for repo in repos:
                        repo_list.append(repo.text)
                else:
                    break
             # if more then one links element it will check text of them , when the elements text equals with next surf on page and pull the elements if isn't equals with next it will pass the next step of loop
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(2)
                        repos = self.browser.find_elements(By.CSS_SELECTOR,"#user-repositories-list > ul > li > div.col-10.col-lg-9.d-inline-block")
                        for repo in repos:
                            repo_list.append(repo.text)
                    else:
                        continue

        # write list of your repostories on the console
        
        self.file_writer(file=name, list = repo_list, save=save)   
                    
        time.sleep(3)
        self.browser.close()
    
    def get_followers(self, save,name):
        self.sign_In()
        time.sleep(1)
        dropdown = self.browser.find_element(By.XPATH,"/html/body/div[1]/header/div[7]/details")
        dropdown.click()
        time.sleep(1)
        profile_btn = self.browser.find_element(By.XPATH,"/html/body/div[1]/header/div[7]/details/details-menu/a[1]")
        profile_btn.click()
        time.sleep(2)

        followers_btn = self.browser.find_element(By.XPATH,"/html/body/div[5]/main/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/div[3]/div/a[1]")
        followers_btn.click()
        time.sleep(1)
        
        # pulling the followers elements.
        followers = self.browser.find_elements(By.CSS_SELECTOR,"body > div.application-main > main > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.Layout-main > div:nth-child(2) > div > div")
        follower_list=[]

        # followers elements convert to a list 
        for follower in followers:
            follower_list.append(follower.text)

        # if there is a next page for elements it will surf and take all of them
        while True:
            # take the button of next and previsous button
            links = self.browser.find_elements(By.CSS_SELECTOR,"body > div.application-main > main > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.Layout-main > div:nth-child(2) > div > div.paginate-container > div > a")
            # checkt the list when there is no button, it will break this loop
            if len(links) == 0:
                break
            # if we have a button it will checkt it and if it is a next button click on it of isn't it will break the loop
            elif len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(2)
                    followers = self.browser.find_elements(By.CSS_SELECTOR,"body > div.application-main > main > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.Layout-main > div:nth-child(2) > div > div")
                    for follower in followers:
                        follower_list.append(follower.text)
                else:
                    break
            # if more then one links element it will check text of them , when the elements text equals with next surf on page and pull the elements if isn't equals with next it will pass the next step of loop
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(2)
                        followers = self.browser.find_elements(By.CSS_SELECTOR,"body > div.application-main > main > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.Layout-main > div:nth-child(2) > div > div")
                        for follower in followers:
                            follower_list.append(follower.text)
                    else:
                        continue
        # write list of your repostories on the console                
        
        self.file_writer(file=name, list = follower_list, save=save)   
                    
        time.sleep(3)
        self.browser.close()

    def get_followings(self, save,name):
        self.sign_In()
        time.sleep(1)
        dropdown = self.browser.find_element(By.XPATH,"/html/body/div[1]/header/div[7]/details")
        dropdown.click()
        time.sleep(1)
        profile_btn = self.browser.find_element(By.XPATH,"/html/body/div[1]/header/div[7]/details/details-menu/a[1]")
        profile_btn.click()
        time.sleep(2)

        following_btn = self.browser.find_element(By.XPATH,"/html/body/div[5]/main/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/div[3]/div/a[2]")
        following_btn.click()
        time.sleep(1)

        # pulling the following elements.
        followings = self.browser.find_elements(By.CSS_SELECTOR,"body > div.application-main > main > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.Layout-main > div:nth-child(2) > div > div")
        following_list=[]

        # following elements convert to a list 
        for following in followings:
            following_list.append(following.text)

        # if there is a next page for elements it will surf and take all of them
        while True:
            # take the button of next and previsous button
            links = self.browser.find_elements(By.CSS_SELECTOR,"body > div.application-main > main > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.Layout-main > div:nth-child(2) > div > div.paginate-container > div > a")
            # checkt the list when there is no button, it will break this loop
            if len(links) == 0:
                break
             # if we have a button it will checkt it and if it is a next button click on it of isn't it will break the loop
            elif len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(2)
                    followings = self.browser.find_elements(By.CSS_SELECTOR,"body > div.application-main > main > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.Layout-main > div:nth-child(2) > div > div")
                    for following in followings:
                        following_list.append(following.text)
                else:
                    break
            # if more then one links element it will check text of them , when the elements text equals with next surf on page and pull the elements if isn't equals with next it will pass the next step of loop
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(2)
                        followings = self.browser.find_elements(By.CSS_SELECTOR,"body > div.application-main > main > div.container-xl.px-3.px-md-4.px-lg-5 > div > div.Layout-main > div:nth-child(2) > div > div")
                        for followings in followings:
                            following_list.append(following.text)
                    else:
                        continue

        self.file_writer(file=name, list = following_list, save=save)       
            
        time.sleep(3)
        self.browser.close()

    def get_last_started(self,save,name):

        self.sign_In()
        time.sleep(1)
        dropdown = self.browser.find_element(By.XPATH,"/html/body/div[1]/header/div[7]/details")
        dropdown.click()
        time.sleep(1)

        profile_btn = self.browser.find_element(By.XPATH,"/html/body/div[1]/header/div[7]/details/details-menu/a[1]")
        profile_btn.click()
        time.sleep(1)

        started_btn = self.browser.find_element(By.XPATH,"/html/body/div[5]/main/div[1]/div/div/div[2]/div/nav/a[5]")
        started_btn.click()
        time.sleep(1)
        # pulling the started elements.
        starteds = self.browser.find_elements(By.CSS_SELECTOR,"#user-starred-repos > div > div > div.col-12.d-block")
        started_list=[]

        # started elements convert to a list 
        for started in starteds:
            started_list.append(started.text)

        # if there is a next page for elements it will surf and take all of them
        while True:
            # take the button of next and previsous button
            links = self.browser.find_elements(By.CSS_SELECTOR,"#user-starred-repos > div > div > div.paginate-container > div > a")
            # checkt the list when there is no button, it will break this loop
            if len(links) == 0:
                break
             # if we have a button it will checkt it and if it is a next button click on it of isn't it will break the loop
            elif len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(2)
                    starteds = self.browser.find_elements(By.CSS_SELECTOR,"#user-starred-repos > div > div > div.col-12.d-block")
                    for started in starteds:
                        started_list.append(started.text)
                else:
                    break
             # if more then one links element it will check text of them , when the elements text equals with next surf on page and pull the elements if isn't equals with next it will pass the next step of loop
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(2)
                        starteds = self.browser.find_elements(By.CSS_SELECTOR,"#user-starred-repos > div > div > div.col-12.d-block")
                        for started in starteds:
                            started_list.append(started.text)
                    else:
                        continue

        self.file_writer(file=name, list = started_list, save=save)       

        time.sleep(3)
        self.browser.close()

    def file_writer(self, file, list, save):
        for l in list:
            print(l,"\n")
            # if save is True it will save your datas as a txt file
        if save:
            with open (f"data/{file}.txt","w",encoding = "UTF-8") as file:
                for l in list:
                    file.write(l+"\n")
                    file.write("\n")
