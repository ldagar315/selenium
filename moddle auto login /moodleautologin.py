# importing selenium libararies
from selenium.webdriver import Safari
#import selenium libraray to amke keys working through
#automation
from selenium.webdriver.common.keys import Keys
# calling the web driver of safari
driver = Safari()
#taking user id and passowrd input from the user 
# you can hard code this if you want to save
# this file locallly on your computer 
user1 = input("enter your user id for moddle :")
passw1 = input("enter your password :")
# calling the moodle login page 
driver.get("https://moodle.iitd.ac.in/login/index.php")
# finding the user id and password elements on the login page 
user = driver.find_element_by_id("username")
passw = driver.find_element_by_id("password")
# entering the user id and pasword in the form 
user.send_keys(user1)
passw.send_keys(passw1)
# finding the capthca input in the login page 
captcha = driver.find_element_by_id("valuepkg3")
# making a local copy of the login form so that
# captcha can be extracted and solved 
text1= driver.find_element_by_id("login").text
# figuring out which type of capthca is asked 
case1 = text1[326:329] # for add or sub 
case2 = text1[332:335] # for first or second value
def checking_the_type_of_captha(case1,case2):
    if case1 == "add":
        num1 = int(text1[332:334])
        num2 = int(text1[337:339])
        sum = num1+num2
        return sum
    elif case1 == "sub":
        num1 = int(text1[337:339])
        num2 = int(text1[342:344])
        diff = num1-num2
        return diff
    elif case2 == "fir":
        num1 = text1[346:348]
        return num1
    elif case2 == "sec":
        num2 = text1[352:354]
        return num2
# above we have defined a func to solve the captcha        
captcha.send_keys(checking_the_type_of_captha(case1,case2))
# enetring the captcha into the form 
loginbt = driver.find_element_by_id("loginbtn")
# locating the login button
loginbt.send_keys(Keys.RETURN)
# clicking the login button 


