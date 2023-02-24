from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
#con estas opts desabilithamos el js del perfil que nos encontramo de google
opts.add_argument("user-agent=whatever you want")
opts.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
chrome = webdriver.Chrome('chromedriver',chrome_options=opts)

driver = webdriver.Chrome(chrome_options=opts)
agent = driver.execute_script("return navigator.userAgent")
print(agent)