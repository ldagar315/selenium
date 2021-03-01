from selenium.webdriver import Safari
# importing os module to making folders 
# your PC
import os
driver = Safari()
#taking input from user for the problem they want to scrape 
problem = int(input("please enter the problem you want to scrape:"))
#creating the folder name with problem
os.mkdir("/Users/lakshaydagar/Downloads/%s" %(problem))
# navigating to the codeforces site 
driver.get("https://codeforces.com/contest/%s" % (problem))
# finding the name of variable of part of problem
taga = driver.find_elements_by_tag_name("a")
#runnig a loop through all the parts in problem
for i in range(27, len(taga)-9, 4):
    driver.get("https://codeforces.com/contest/%s" % (problem))
    taga = driver.find_elements_by_tag_name("a")
    # converting the part of problem to a string 
    op = taga[i].get_attribute("innerHTML")
    o = op[29] # mapping is done such that the 29th element in page 
               # source is first part of problem and folllwoing part follow
               # a 4 no. differance 
    try:
        # navigating to specific problem page 
        driver.get("https://codeforces.com/contest/%s/problem/%s"%(problem,o))
        # creating a sprate folder for the part of the problem 
        os.mkdir("/Users/lakshaydagar/Downloads/%s/%s"%(problem,o))
        # maximizing the window so that screenshot can be taken 
        driver.set_window_size(1500, 1080)
        # saving the screenshot in the problem folder created earlier
        driver.save_screenshot("/Users/lakshaydagar/Downloads/%s/%s/problem%s.png"%(problem,o,o))
        # now finding the input and output elements by tag name pre 
        inpu = driver.find_elements_by_tag_name("pre")
        # running a loop to get all the inputs and output boxes printed out
        for m in range (0,len(inpu),2):
            filein = 1
            # first creating a folder by their name 
            os.mkdir("/Users/lakshaydagar/Downloads/%s/%s/input%s"%(problem,o,filein))
            # now writing all the input in a text file
            with open('/Users/lakshaydagar/Downloads/%s/%s/input%s/input%s.text'%(problem,o,filein,filein), 'w') as f:
                f.write(inpu[m].text)
            filein += 1    
             # running a loop for output as same as input   
        for n in range (1,len(inpu),2):
            fileout = 1 
            os.mkdir("/Users/lakshaydagar/Downloads/%s/%s/output%s"%(problem,o,fileout))
            with open("/Users/lakshaydagar/Downloads/%s/%s/output%s/output%s.text"%(problem,o,fileout,fileout), 'w') as g:
                g.write(inpu[n].text)
            fileout += 1     

    except:
        continue
# quit the browser window when all work is done         
driver.quit()
