from time import sleep
from pagesObjects.LoginPage import LoginPage
from pagesObjects.ProductsPage import ProductsPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_002_add_product_to_car(self,setup):
        self.logger.info("*************** Test_002_add_a_product_to_the_car *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.pp = ProductsPage(self.driver)
        self.pp = self.pp.add_a_product()
        sleep(13)
        self.driver.close()




