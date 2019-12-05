import sys
import os
from github import Github

path = "/Users/thanoschourlias/Documents/codingprojects/"

username = "Athanasioschourlias" 
password = "thanaras123" 

def create():
    folderName = str(input("Give the name of the project folder and repo: "))
    # folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))
    user = Github(username, password).get_user()
    repo = user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()



# print("EIMAI LIGO PRIN TO ERROORRRRRRR KANE KATI")


# browser = webdriver.Chrome(executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

# print("DEN STAMATAW EKEI PAW KAI PIO KATW")
# browser.get("https://github.com/login") 


# path = ("/Users/thanoschourlias/Documents/codingprojects/")

# def create():

    
#     folderName = str(sys.argv[1])
#     os.makedirs(path + folderName)
#     python_button = browser.find_elements_by_xpath("//input[@name='login']")[0]
#     python_button.click()
    
    
# if __name__ == "__main__":
#     create()
#     #passs