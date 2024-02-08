# importing libraries
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import html


import requests
from bs4 import BeautifulSoup

def scrape_analytics_insight():
    url = "https://www.analyticsinsight.net/category/latest-news/"
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        article_data = []
        # Find all articles
        articles = soup.find_all('article', class_='post')

        for article in articles:
            # Extract title and link
            title_tag = article.find('h2', class_='entry-title')
            if title_tag:
                title = title_tag.text.strip()
                link = title_tag.a['href'] if title_tag.a else None

                # Extract image source link
                image_tag = article.find('img')
                img_link = image_tag['src'] if image_tag else None

                article_data.append({'article_title': title, 'Link': link, 'Image': img_link})
    
        return article_data

    else:
        print(f"Error: {response.status_code}")
        return None
# -----------------------------------------


def scrape_mit_news():
    url = "https://news.mit.edu/topic/artificial-intelligence2?type=1"
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        doc = BeautifulSoup(response.text, 'html.parser')

        # Extract the relevant information for all articles
        article_data = []
        article_elements = doc.find_all('div', {'class': 'page-term--views--list-item'})

        for article_element in article_elements:
            img_link = 'https://news.mit.edu' + article_element.find('img')['data-src']
            if img_link is None:
                continue
            
            title = article_element.find('h3', class_='term-page--news-article--item--title').a.span.text.strip()
            link = 'https://news.mit.edu/' + article_element.find('h3', class_='term-page--news-article--item--title').a['href']
            description = article_element.find('p', class_='term-page--news-article--item--dek').span.text.strip()
            date = article_element.find('p', class_='term-page--news-article--item--publication-date').time['datetime']

            article_data.append({'article_title': title, 'Link': link, 'Image': img_link, 'Description': description})
        
        return article_data

    else:
        print(f"Error: {response.status_code}")
        return None
# ----------------------

def scrape_wired_news():
    url = "https://www.wired.co.uk/topic/artificial-intelligence"
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        doc = BeautifulSoup(response.text, 'html.parser')

        # Extract the relevant information for all articles
        article_data = []
        article_elements = doc.find_all('div', {'class': 'SummaryItemWrapper-iwvBff cKnNyU summary-item summary-item--has-border summary-item--article summary-item--no-icon summary-item--text-align-left summary-item--layout-placement-side-by-side-desktop-only summary-item--layout-position-image-left summary-item--layout-proportions-33-66 summary-item--side-by-side-align-center summary-item--side-by-side-image-right-mobile-false summary-item--standard SummaryItemWrapper-iGxRII bMTfcI summary-list__item'})

        for article_element in article_elements:
            # IMAGE
            img_tag = article_element.find('img', class_='ResponsiveImageContainer-eybHBd')
            if img_tag is None:
                continue
            else:
                img_link = img_tag['src']

            # TEXT
            title = article_element.find('a', class_="SummaryItemHedLink-civMjp ejgyuy summary-item-tracking__hed-link summary-item__hed-link").h3.text
            link = "https://www.wired.co.uk" + article_element.find('a', class_="SummaryItemHedLink-civMjp ejgyuy summary-item-tracking__hed-link summary-item__hed-link")['href']

            article_data.append({'article_title': title, 'Link': link, 'Image': img_link})
        
        return article_data

    else:
        print(f"Error: {response.status_code}")
        return None
# -------------------------


def scrape_extremetech_news():
    url = "https://www.extremetech.com/tag/artificial-intelligence"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the HTML content using lxml
        doc = html.fromstring(response.content)

        # Extract the relevant information for all articles
        article_data = []
        article_elements = doc.xpath('//div[contains(@class, "item flex mt-4")]')

        for article_element in article_elements:
            # IMAGE
            img_tag = article_element.find('.//img[@class="w-full"]')
            if img_tag is None:
                continue
            else:
                img_link = img_tag.attrib.get('src', '')

            # TEXT
            title = article_element.xpath('.//a[contains(@class, "w-full block hover:text-brand-orange text-base leading-tight font-medium sm:text-xl sm:leading-normal text-gray-700")]/text()')
            title = ' '.join(title).strip()

            description = article_element.xpath('.//div[@class="hidden md:block w-full text-gray-600 mt-2"]/text()')
            description = ' '.join(description).strip()

            link = "https://www.extremetech.com" + article_element.xpath('.//a[contains(@class, "w-full block hover:text-brand-orange text-base leading-tight font-medium sm:text-xl sm:leading-normal text-gray-700")]/@href')[0]

            article_data.append({'article_title': title, 'Link': link, 'Image': img_link, 'Description': description})
        
        return article_data

    else:
        print(f"Error: {response.status_code}")
        return None

# --------------------


def scrape_venturebeat_news():
    url = "https://venturebeat.com/"
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        doc = BeautifulSoup(response.text, 'html.parser')

        # Extract the relevant information for all articles
        article_data = {}
        article_elements = doc.find_all('article', {'class': 'ArticleListing'})

        for article_element in article_elements:
            # IMAGE
            img_tag = article_element.find('img', class_='ArticleListing__image wp-post-image')
            if img_tag is None:
                continue
            else:
                img_link = img_tag['src']

            # TEXT
            title = article_element.find('h2', class_="ArticleListing__title").a.text
            link = article_element.find('a', class_="ArticleListing__title-link")['href']

            article_data.append({'article_title': title, 'Link': link, 'Image': img_link})
        
        return article_data

    else:
        print(f"Error: {response.status_code}")
        return None

#-------------------

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_huggingface_papers():
    url = "https://huggingface.co/papers"
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Initialize lists to store data
        # data = {'Title': [], 'Paper_Link': [], 'Image': []}
        data = []

        # Find all article elements
        articles = soup.find_all('article', class_="flex flex-col overflow-hidden rounded-xl border")

        # Iterate over each article
        for article in articles:
            # Extract image source if available
            img_tag = article.find('img')
            image = img_tag.get('src') if img_tag else None

            # Extract title text
            title = article.find('h3').text.strip()

            # Extract link
            link = "https://huggingface.co" + article.find('a').get('href')

            # Append data to lists
            # data['Image'].append(image)
            # data['Title'].append(title)
            # data['Paper_Link'].append(link)
            data.append({'article_title': title, 'Link': link, 'Image': image})

        # Create a DataFrame from the collected data
        
        return data

    else:
        print(f"Error: {response.status_code}")
        return None
# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# def combine_data_simple(*data_list):
#     combined_data = {'article_title': [], 'Link': [], 'Image': []}

#     for data in data_list:
#         if data:
#             for entry in data:
#                 combined_data['article_title'].append(entry['article_title'])
#                 combined_data['Link'].append(entry['Link'])
#                 combined_data['Image'].append(entry['Image'])

#     df_combined = pd.DataFrame(combined_data)
#     return df_combined

# data_analytics_vidhya = scrape_analytics_insight()
data_wired = scrape_wired_news()
# data_venturebeat = scrape_venturebeat_news()
data_mitnews = scrape_mit_news()
data_extremetech = scrape_extremetech_news()
data_huggingface = scrape_huggingface_papers()

# # print("Vidhya : ", data_analytics_vidhya)
# print('--------------------------------------------------------/n')
# print("wired : ",data_wired)
# print('--------------------------------------------------------/n')
# # print("venture : ",data_venturebeat)
# print('--------------------------------------------------------/n')
# print("mit : ",data_mitnews)
# print('--------------------------------------------------------/n')
# print("huggingface : ",data_huggingface)
# print('--------------------------------------------------------/n')
# print("extremetech : ",data_extremetech)