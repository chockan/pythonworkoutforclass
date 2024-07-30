import requests 
from bs4 import BeautifulSoup  #  pip install beautifulsoup4 

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

URL="https://www.amazon.in/s?k=drones&crid=Y84K7634WRKE&sprefix=drones%2Caps%2C273&ref=nb_sb_noss_1"


webp = requests.get(URL, headers=HEADERS)

#print(webp.content)
soup = BeautifulSoup(webp.content, "html.parser")

#print(soup)

links = soup.find_all("a", attrs={"class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})

#print(links)
# a=links[0].get('href')
# print(a)
# print("########################")
# product_list="https://www.amazon.in/" + a
# print(product_list)



links_list = []

# # # Loop for extracting links from Tag Objects
for link in links:
    
    links_list.append(link.get('href'))
    
for link in links_list:
    try:
        new_webpage = requests.get("https://www.amazon.in" + link, headers=HEADERS)
        new_webpage.raise_for_status()  # Raise an exception for HTTP errors
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")
        
        # Check if the title is properly displayed
        title_tag = new_soup.find("span", id="productTitle")
        #print(title_tag)
        if title_tag:
            title = title_tag.get_text().strip()
            print("Title:", title)
            
        
    except requests.exceptions.RequestException as e:
        # Skip printing error messages and continue with the next link
        continue