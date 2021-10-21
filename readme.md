
<img src="logo.webp" alt="Bovada Logo" width="25" height="25"> Bovada Activity Scraper 
==========================

Bovada Activity Scraper exports your betting history into a CSV file using python3

## Saving the HTML
1. Go to your Account > Tranactions > All Transaction
2. Select the date interval (such as 31 days)
3. Scroll the table to the bottom until there are no more transactions to load (page load dynamically)
4. Inspect the webpage
5. In the dev tools, copy the <body> block (right click and copy element) and save it to your working directory


## Dependencies
[Python3](https://www.python.org/downloads/)
[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)


## Running the code
```
python3 scraper.py "bovada_html_file.html" "output.csv"
```