from Classes.ClassUtility import *
from Classes.Class30nama import Class30nama

url = str("file://" + get_root_path() + "30nama.html")

# service = Service()
# #initialize web driver
# with webdriver.Firefox(service=service,options=firefox_options) as driver:
#     #navigate to the url
#     driver.get("file://" + get_root_path() + "blog.html")
#     #find element by css selector
#     myDiv = driver.find_element(By.CSS_SELECTOR, 'div.post-title')
#     print(myDiv.get_attribute("outerHTML"))
#
#     mydiv2 = driver.find_element(By.CLASS_NAME, 'post-title')
#     print(mydiv2.text)

myWebDriver = MyWebDriver(url=url)

class30nama = Class30nama()

soup = myWebDriver.get_soup()

found = soup.select("div>h2.title")

if found:
    print(found[0].text)

# mydiv2 = driver.find_element(By.CLASS_NAME, 'post-title')
# print(mydiv2.text)

myWebDriver.close()

# driver = Html.get_driver_for_subscene(url)
# driver = Html.get_driver_for_subscene("https://complex-life.blog.ir/")


# button = driver.find_element(By.CLASS_NAME, "post-title")
#
# print(button)
