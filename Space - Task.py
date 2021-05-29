import time                                                                 #the code might run into an error while running, 
from selenium import webdriver                                              #like its not able to locate something.
from selenium.webdriver import ActionChains                                 #It's a bug, try to re-run the code.
from selenium.webdriver.chrome.options import Options as selOptions                       
from selenium.webdriver.common.keys import Keys                             #I did not use OOP since I am not
                                                                            #familiar with Pytest,Allure...                                                                           
                                                                            #One more thing, the given email
                                                                            #got registered after some tests, so
                                                                            #I have put an unregistered one - random333@email.net
                                                                            #which as I said is not registered and after you run the code, 
                                                                            #it will get registered






#                                      SetUp
options = selOptions()
options.add_argument("no-sandbox")            #Did not manage to set the window size to the given resolution since 'quick view'
options.add_argument("window-size=1792,1120") #button would only show up while hovering the cursor up to a certain resolution.

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe", options=options) #My chromedriver location
driver.get("http://automationpractice.com/index.php")
action = ActionChains(driver)



def fooling_around():
    #the following script finds the specified item, hovers the cursor on it, so we are able to
    #click the 'quick view' button. P.s it took me a while.
    time.sleep(2)
    
    
    target = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div[1]/ul[1]/li[3]/div/div[2]/h5/a")
    action.move_to_element(target).perform()
    driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div[1]/ul[1]/li[3]/div/div[1]/div/a[2]").click()
    
    
    #the following script clicks 'minus','plus' and 'close' buttons, as mentioned
    #driver.find_element_by_xpath("/html/body/div/div/div[3]/form/div/div[2]/p[1]/a[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/a").click() 
    
    
def purchasing():
    #Clicking 'More' button  
    target = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div[1]/ul[1]/li[3]/div/div[2]/h5/a")
    action.move_to_element(target).perform()
    driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div[1]/ul[1]/li[3]/div/div[2]/div[2]/a[2]/span").click()
    time.sleep(1)
    #increasing quantity by 1
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/div/div[4]/form/div/div[2]/p[1]/a[2]/span/i').click()

    #adding to cart
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/div/div[4]/form/div/div[3]/div/p/button/span').click()
    time.sleep(2)
    
    #proceeding to checkout
    driver.find_element_by_xpath('/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a').click()
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]').click()

    #entering email 
    email_input = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/div[1]/form/div/div[2]/input")
    email_input.send_keys("random333@email.net", Keys.RETURN)
    time.sleep(3)
    #selecting 'Mr.'
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[1]/div[1]/label').click()
    
    #entering First name
    first_name = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[2]/input")
    first_name.send_keys('Jhon')
    
    time.sleep(1)
    
    #entering Last name
    last_name = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[3]/input")
    last_name.send_keys('Doe')
    
    time.sleep(1)

    #entering password
    password = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[5]/input")
    password.send_keys('paroli')

    #CHOOSING DATE OF BIRTH
    #Day:
    day_select = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[6]/div/div[1]/div/select').click()
    day = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[6]/div/div[1]/div/select/option[4]').click()
    #Month:
    month_select = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[6]/div/div[3]/div/select').click()   
    month = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[6]/div/div[2]/div/select/option[6]').click()
    #Year:
    year_select = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[6]/div/div[3]/div/select').click()
    year = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[6]/div/div[3]/div/select/option[50]').click()

    #ENTERING ADDRESS
    #Main address field
    address_input = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[2]/p[4]/input')
    address_input.send_keys('115 Lower Jersey RD')

    #City
    city = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[2]/p[6]/input')
    city.send_keys('Jersey')

    #State
    state_select = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[2]/p[7]/div/select').click()
    state = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[2]/p[7]/div/select/option[12]').click()

    #Entering Zip code
    zip_input = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[2]/p[8]/input')
    zip_input.send_keys('30014')

    #Entering Home phone number
    home_phone_input = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[2]/p[12]/input')
    home_phone_input.send_keys('+17706091425')


    #Clicking the 'Register' button
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div[4]/button').click()

    #Clicking 'Proceed to checkout' and checking the terms box
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/form/p/button').click()
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/div/p[2]/div').click()
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/form/p/button').click()

    #Clicking 'pay by bank wire'
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div/div[3]/div[1]/div/p/a').click()

    #Clicking 'I confirm my order'
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/form/p/button').click()


fooling_around()
time.sleep(2)
purchasing()     

