class LoginPage():
    #Define web elements using conventional name: typeObject_nameObject_idenfiedBy = "id,name,xpath. etc"
    title_swaglabs_xpath = "//body/div[@id='root']/div[1]/div[1]"
    input_username_css = "#user-name"
    input_password_id = "password"
    button_login_name = "login-button"


    def __init__(self,driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element("css selector", self.input_username_css).click()
        self.driver.find_element("css selector", self.input_username_css).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element("id", self.input_password_id).click()
        self.driver.find_element("id", self.input_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element("name", self.button_login_name).click()


"""
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")
"""