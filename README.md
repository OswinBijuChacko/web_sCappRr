#🛍️ Amazon Bestsellers Web Scraper
This project is a Python-based tool that automates the process of logging into Amazon and scraping bestseller product data using Selenium WebDriver. It collects product information such as the name, price, rating, image URL, direct product link, and category, and saves the data into a CSV file for easy analysis. The script is designed to work specifically with Amazon India (amazon.in), and it covers multiple product categories like electronics, books, clothing, kitchen, and more.

##📖 How the Script Works
The scraper follows a step-by-step workflow that starts with logging into Amazon. For login, instead of hardcoding credentials, the script reads the username and password from a .env file. This is done using the python-dotenv package, which keeps your sensitive data secure and separate from your code. After a successful login, the script navigates through a predefined list of bestseller category URLs, opening each one in the browser using Selenium.

Within each category page, the script identifies product cards on the page using CSS selectors. It then extracts the relevant product details like the product title, star rating (if available), price, thumbnail image URL, and the hyperlink to the product page. Each product is also tagged with the category it belongs to. All this data is stored in a list of dictionaries, and once scraping is complete, it's exported to a CSV file named amazon_bestsellers.csv.

#🛠️ Installation Guide
🔧 Prerequisites
1.Python 3.x
2.Google Chrome
3.ChromeDriver matching your Chrome version

#📥 Steps
# Clone this repository
git clone https://github.com/OswinBijuChacko/web_sCappRr.git
cd web_sCappRr

# Install dependencies
pip install selenium python-dotenv

# Place chromedriver.exe in the root folder (or add to PATH)
🚀 How to Use
Update .env with your credentials.

Run the scraper:

bash
Copy
Edit
python amazon_scraper.py
Wait for the browser to complete all scraping operations.

View the output in amazon_bestsellers.csv.

💡 Use Cases
Use Case	Description
📊 E-Commerce Research	Track prices, top-rated products, and bestsellers over time.
🧠 Machine Learning	Build recommendation or price prediction models with real data.
🧪 Academic Use	Use in data science or business analytics projects.
📈 Trend Analysis	Monitor product trends across categories monthly.

⚠️ Disclaimers
⚖️ This tool is meant only for educational purposes.

🚫 Amazon’s Terms of Service prohibit automated scraping without permission.

⚠️ Use responsibly. Do not overload servers or scrape too frequently.

📄 License
This project is licensed under the MIT License – you’re free to use and modify it, but use at your own risk.

👤 Author
Oswin Biju Chacko

💼 LinkedIn

📁 GitHub
