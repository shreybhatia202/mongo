from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd


executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

def scrape():
    data = {}
    output = marsNews()
    data["mars_news"] = output[0]
    data["mars_paragraph"] = output[1]
    data["mars_image"] = marsImage()
    data["mars_weather"] = marsWeather()
    data["mars_facts"] = marsFacts()
    data["mars_hemisphere"] = marsHemisphere()
    return data


# News_Mars
def marsNews():
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("div", class_="list_text")
    news_title = article.find("div", class_="content_title").text
    news_p = article.find("div", class_ ="article_teaser_body").text
    output = [news_title, news_p]
    return output


def marsImage():
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    image = soup.find("img", class_="thumb")["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + image
    return featured_image_url


def marsWeather():
    weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    mars_twitter = soup.find_all("p", class_="TweetTextSize")
    mars_weather = mars_twitter[0].text
    return mars_weather

def marsFacts():
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    mars_data = pd.read_html(facts_url)
    mars_data = pd.DataFrame(mars_data[0])
    mars_facts = mars_data.to_html(header = False, index = False)
    return mars_facts


def marsHemisphere():
    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    mars_hemisphere = []

    products = soup.find("div", class_ = "result-list" )
    hemispheres = products.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image_link)
        html = browser.html
        soup=BeautifulSoup(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        mars_hemisphere.append({"title": title, "img_url": image_url})
    return mars_hemisphere


























































#     url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
#     browser.visit(url)

#     html = browser.html
#     soup = BeautifulSoup(html, "html.parser")
#     lists  = soup.find_all("li", class_="slide")
#     for item in lists:
#         headlines.append(item.find("div", class_="content_title").find("a").text)

#     print(len(headlines))   

    
    
#     return browser

# # executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
# # browser = Browser("chrome", **executable_path, headless=False)
# # url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
# # browser.visit(url)
# marsHTML = scrape()