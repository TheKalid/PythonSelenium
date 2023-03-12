class WelcomePage:
    #Define web elements using conventional name: typeObject_nameObject_idenfiedBy = "id,name,xpath. etc"
    button_login_xpath = "//header/div[@id='navbar']/div[@id='nav-flyout-anchor']/div[13]/div[2]/a[1]/span[1]"

    def __init__(self,driver):
        self.driver=driver

    def openLogin(self):
        self.driver.find_element("xpath", self.button_login_xpath).click()

    
#find_element_by_link_text
