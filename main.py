from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# Configure WebDriver
chrome_options = Options()
service = Service('chromedriver.exe') 
driver = webdriver.Chrome(service=service, options=chrome_options)

# Amazon credentials
USERNAME = 'sunshndaisy@gmail.com'
PASSWORD = 'amazon3118'

# URLs to scrape
categories = [
    "electronics", "books", "clothing", "toys", "kitchen", 
    "beauty", "sports", "automotive", "health", "pet-supplies"
]

# Data storage
data = []

# Authenticate on Amazon
def login_to_amazon(username, password):
    driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    try:
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ap_email"))
        )
        email_field.send_keys(username)
        driver.find_element(By.ID, "continue").click()

        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ap_password"))
        )
        password_field.send_keys(password)
        driver.find_element(By.ID, "signInSubmit").click()

        print("Login successful.")
        
    except TimeoutException:
        print("Login failed. Please check credentials or site availability.")
        

def scrape_category(category_url):
    driver.get(category_url)
    time.sleep(5)
    products = driver.find_elements(By.CSS_SELECTOR, '.p13n-gridRow .a-cardui')
    for product in products[:1500]:
        try:
            name = product.find_element(By.CSS_SELECTOR, '._cDEzb_p13n-sc-css-line-clamp-3_g3dy1').text
            rating = product.find_element(By.CSS_SELECTOR, '.a-icon-star-small span').get_attribute('innerHTML')
            price = product.find_element(By.CSS_SELECTOR, '.a-color-price span').text
            image = product.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
            link = product.find_element(By.CSS_SELECTOR, 'a.a-link-normal').get_attribute('href')
            
            data.append({
                'Product Name': name,
                'Rating': rating,
                'Price': price,
                'Image URL': image,
                'Product Link': 'https://www.amazon.in/'+str(link),
                'Category': category_url.split('/')[-2]
            })
        except Exception as e:
            print(f"Error parsing product: {e}")

# Authenticate and scrape all categories
login_to_amazon(USERNAME,PASSWORD)
for category in categories:
    print(f"Scraping Category: {category}")
    category_url = "https://www.amazon.in/gp/bestsellers/"+str(category)+'/'
    scrape_category(category_url)

# Save data to CSV
with open('amazon_bestsellers.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Product Name', 'Rating', 'Price','Image URL', 'Product Link','Category'])
    writer.writeheader()
    writer.writerows(data)

# Close WebDriver
driver.quit()
print("Scraping Complete. Data saved to 'amazon_bestsellers.csv'")
