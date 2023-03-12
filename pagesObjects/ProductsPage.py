class ProductsPage():
    title_products_xpath = "//span[contains(text(),'Products')]"    
    product_backpack_button_name = "add-to-cart-sauce-labs-backpack"
    product_bikelight_button_name = "add-to-cart-sauce-labs-bike-light"
    product_boldshirt_button_name = "add-to-cart-sauce-labs-bolt-t-shirt"
    product_flaeece_button_name = "add-to-cart-sauce-labs-fleece-jacket"
    product_onesie_button_name = "add-to-cart-sauce-labs-onesie"
    product_tshirt_button_name = "add-to-cart-test.allthethings()-t-shirt-(red)"
    icon_car_button_id = "shopping_cart_container"

    def __init__(self,driver):
        self.driver = driver

    def get_products_title(self):
        title_products = self.driver.find_element("xpath",self.title_products_xpath).text
        return title_products
        
    def open_car(self):
        self.driver.find_element("id", self.icon_car_button_id).click()

    def add_a_product(self):
        self.driver.find_element("name", self.product_boldshirt_button_name).click()

