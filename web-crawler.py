# ------------------------------------------------------------
#
#                   START OF THE WEB CRAWLER
# 
# ------------------------------------------------------------
# ------------------------------------------------------------
#
#       Author  : Uma Mageswari Rajendiran
#       Date    : September 27, 2020
#       Title   : Coronavirus News Article Web Crawler
# 
# ------------------------------------------------------------

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#News source for user generated texts
nytimes_query_url = "https://www.nytimes.com/search?query=coronavirus"
ustoday_query_url = "https://www.usatoday.com/search/?q=coronavirus"
time_query_url = "https://time.com/search/?q=coronavirus"
yahoo_query_url = "https://news.search.yahoo.com/search?p=coronavirus&fr=uh3_news_vert_gs&fr2=p%3Anews%2Cm%3Asb"
science_query_url = "https://www.sciencenews.org/?s=coronavirus"
newyorker_query_url = "https://www.newyorker.com/search/q/coronavirus"
latimes_query_url = "https://www.latimes.com/search?q=coronavirus"
newscientist_query_url = "https://www.newscientist.com/search/?q=coronavirus"
sciamerican_query_url = "https://www.scientificamerican.com/search/?q=coronavirus"
scinews_query_url = "https://www.sciencenewsforstudents.org/?s=coronavirus"
week_query_url = "https://theweek.com/search/coronavirus"
dogonews_query_url = "https://www.dogonews.com/search/coronavirus"
onion_query_url = "https://www.theonion.com/search?blogId=1636079510&q=coronavirus"
natrev_query_url = "https://www.nationalreview.com/?s=coronavirus"
livesci_query_url = "https://www.livescience.com/search?searchTerm=coronavirus"

#List of all article urls
nytimes_article_urls = [] 
ustoday_article_urls = []
time_article_urls = []
yahoo_article_urls = []
science_article_urls = []
newyorker_article_urls = []
latimes_article_urls = []
newscientist_article_urls = []
sciamerican_article_urls = []
scinews_article_urls = []
week_article_urls = []
dogonews_article_urls = []
onion_article_urls = []
natrev_article_urls = []
livesci_article_urls = []

#File of extracted urls
url_list = open("url_list.txt", "a")

#Initializing the url counter
url_count = 1;

#URL Extraction Code Below

#Extracting urls for search results from nytimes
uClient = uReq(nytimes_query_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")
domain_url = "www.nytimes.com/"
text_sections = page_soup.find("ol", {"data-testid": "search-results"}).find_all("a")

for i in text_sections:
    if "/2020/" in i.get("href"):
        t = domain_url + i.get("href")
        t = t.split('?')[0]
        print(url_count,". ",t)
        text = str(url_count)+". "+t+"\n"
        url_list.write(text)
        url_count+=1
        nytimes_article_urls.append(t)

#Extracting urls for search results from ustoday
uClient = uReq(ustoday_query_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")
domain_url = "www.usatoday.com/"
text_sections = page_soup.find("div", {"class": "gnt_pr"}).find_all("a")

for i in text_sections:
    if "/2020/" in i.get("href"):
        t = domain_url + i.get("href")
        if("//story/" in t):
            print(url_count,". ",t)
            text = str(url_count)+". "+t+"\n"
            url_list.write(text)
            url_count+=1
            ustoday_article_urls.append(t)

#Extracting urls for search results from time
uClient = uReq(time_query_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")
domain_url = "www.time.com/"
text_sections = page_soup.find("div", {"data-tracking-zone": "search-results"}).find_all("a")

for i in text_sections:
    if "coronavirus" in i.get("href"):
        t = i.get("href")
        if t not in time_article_urls:
            if("wyckoff-hospital-brooklyn-coronavirus" not in t):
                time_article_urls.append(t)
                print(url_count,". ",t)
                text = str(url_count)+". "+t+"\n"
                url_list.write(text)
                url_count+=1

#Extracting urls for search results from yahoo
uClient = uReq(yahoo_query_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")
domain_url = "www.news.yahoo.com/"
text_sections = page_soup.find("div", {"id": "web"}).find_all("a")

for i in text_sections:
    if "coronavirus" in i.get("href"):
        t = i.get("href")
        if t not in yahoo_article_urls:
            if("news.yahoo.com" in t):
                yahoo_article_urls.append(t)
                print(url_count,". ",t)
                text = str(url_count)+". "+t+"\n"
                url_list.write(text)
                url_count+=1

#Extracting urls for search results from science
uClient = uReq(science_query_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")
domain_url = "www.sciencenews.org/"
text_sections = page_soup.find("ol", {"class":"list"}).find_all("a")

for i in text_sections:
    if "coronavirus" in i.get("href"):
        t = i.get("href")
        if t not in science_article_urls:
            science_article_urls.append(t)
            print(url_count,". ",t)
            text = str(url_count)+". "+t+"\n"
            url_list.write(text)
            url_count+=1

#Extracting urls for search results from newyorker
uClient = uReq(newyorker_query_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")
domain_url = "https://www.newyorker.com/"
text_sections = page_soup.find("main", {"class":"ElasticSearchPage__content___XqBdi"}).find_all("a")

for i in text_sections:
    if "coronavirus" in i.get("href"):
        t = i.get("href")
        t = domain_url + i.get("href")
        if t not in newyorker_article_urls:
            if("//search/" not in t):
                newyorker_article_urls.append(t)
                print(url_count,". ",t)
                text = str(url_count)+". "+t+"\n"
                url_list.write(text)
                url_count+=1

#Extracting urls for search results from latimes
uClient = uReq(latimes_query_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")
domain_url = "www.latimes.com/"
text_sections = page_soup.find("main", {"class":"search-results-module-main"}).find_all("a")

for i in text_sections:
    if "coronavirus" in i.get("href"):
        t = i.get("href")
        if t not in latimes_article_urls:
            if("/search" not in t):
                latimes_article_urls.append(t)
                print(url_count,". ",t)
                text = str(url_count)+". "+t+"\n"
                url_list.write(text)
                url_count+=1

#Extracting urls for search results from newscientist
uClient = uReq(newscientist_query_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")
domain_url = "https://www.newscientist.com/"
text_sections = page_soup.find("div", {"class":"search-results"}).find_all("a")

for i in text_sections:
    if "coronavirus" in i.get("href"):
        t = i.get("href")
        t = domain_url + t
        if t not in newscientist_article_urls:
            if("//search/" not in t):
                newscientist_article_urls.append(t)
                print(url_count,". ",t)
                text = str(url_count)+". "+t+"\n"
                url_list.write(text)
                url_count+=1

#Extracting urls for search results from sciamerican
uClient = uReq(sciamerican_query_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")
domain_url = "www.scientificamerican.com/"
text_sections = page_soup.find("div", {"class":"grid__col large-up-8-12 section-latest"}).find_all("a")

for i in text_sections:
    if "coronavirus" in i.get("href"):
        t = i.get("href")
        if t not in sciamerican_article_urls:
            sciamerican_article_urls.append(t)
            print(url_count,". ",t)
            text = str(url_count)+". "+t+"\n"
            url_list.write(text)
            url_count+=1

#Extracting urls for search results from scinews
uClient = uReq(scinews_query_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")
domain_url = "www.sciencenewsforstudents.org/"
text_sections = page_soup.find("ol", {"class":"list"}).find_all("a")

for i in text_sections:
    if "coronavirus" in i.get("href"):
        t = i.get("href")
        if t not in scinews_article_urls:
            if("/article/" in t):
                scinews_article_urls.append(t)
                print(url_count,". ",t)
                text = str(url_count)+". "+t+"\n"
                url_list.write(text)
                url_count+=1

#Extracting urls for search results from week
uClient = uReq(week_query_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")
domain_url = "https://www.theweek.com"
text_sections = page_soup.find("div", {"class":"search-results"}).find_all("a")

for i in text_sections:
    if "coronavirus" in i.get("href"):
        t = i.get("href")
        t = domain_url + t
        if t not in week_article_urls:
            week_article_urls.append(t)
            print(url_count,". ",t)
            text = str(url_count)+". "+t+"\n"
            url_list.write(text)
            url_count+=1

#Extracting urls for search results from dogonews
uClient = uReq(dogonews_query_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")
domain_url = "https://www.dogonews.com/"
text_sections = page_soup.find("div", {"id":"news-posts"}).find_all("a")

for i in text_sections:
    if "coronavirus" in i.get("href"):
        t = i.get("href")
        if t not in dogonews_article_urls:
            dogonews_article_urls.append(t)
            print(url_count,". ",t)
            text = str(url_count)+". "+t+"\n"
            url_list.write(text)
            url_count+=1

#Extracting urls for search results from onion
uClient = uReq(onion_query_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")
domain_url = "https://www.theonion.com/"
text_sections = page_soup.find("div", {"class":"sc-1ijd9j3-2 cFvaIP"}).find_all("a")

for i in text_sections:
    if "coronavirus" in i.get("href"):
        t = i.get("href")
        if t not in onion_article_urls:
            if("/how-" not in t):
                onion_article_urls.append(t)
                print(url_count,". ",t)
                text = str(url_count)+". "+t+"\n"
                url_list.write(text)
                url_count+=1

#Extracting urls for search results from natrev
uClient = uReq(natrev_query_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")
domain_url = "https://www.nationalreview.com/"
text_sections = page_soup.find("div", {"class": "post-list post-list--linear post-list--search-results"}).find_all("a")

for i in text_sections:
    if "coronavirus" in i.get("href"):
        t = i.get("href")
        if t not in natrev_article_urls:
            natrev_article_urls.append(t)
            print(url_count,". ",t)
            text = str(url_count)+". "+t+"\n"
            url_list.write(text)
            url_count+=1

#Extracting urls for search results from livesci
uClient = uReq(livesci_query_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")
domain_url = "https://www.livescience.com/"
text_sections = page_soup.find("div", {"class": "listingResults"}).find_all("a")

for i in text_sections:
    if "coronavirus" in i.get("href"):
        t = i.get("href")
        t = domain_url + t
        if t not in livesci_article_urls:
            livesci_article_urls.append(t)
            print(url_count,". ",t)
            text = str(url_count)+". "+t+"\n"
            url_list.write(text)
            url_count+=1

url_list.close()

#Initializing the header and article counters
header_count = 1
article_count = 1


#Article Extraction Code Below

#Extracting articles from each url in the search results of nytimes
for url in nytimes_article_urls:
    url = 'https://'+url
    uClient = uReq(url)
    read_html = uClient.read()
    uClient.close()
    page_soup = soup(read_html, "html.parser")

    headline = page_soup.find("h1", {"itemprop": "headline"})
    text_sections = page_soup.find("article", {"id": "story"}).find_all("p")
    
    article = ""
    for i in text_sections:
        article += i.text

    #Creating a new file for each header
    header = headline.text+"\n"
    header_file_name = "heading_"+str(header_count)+".txt"
    header_file_ptr = open(header_file_name, "a")
    header_file_ptr.write(header)
    header_file_ptr.close()

    #Creating a new file for each article
    article_file_name = "article_"+str(article_count)+".txt"
    article_file_ptr = open(article_file_name, "a")
    article_file_ptr.write(article)
    article_file_ptr.close()

    print("(---------Title----------)")
    print(header)
    print("(---------Article----------)")
    print(article)
    print("(----------End---------)")

    #Incrementing header and article counters
    header_count += 1
    article_count += 1

#Extracting articles from each url in the search results of ustoday
for url in ustoday_article_urls:
    url = 'https://'+url
    uClient = uReq(url)
    read_html = uClient.read()
    uClient.close()
    page_soup = soup(read_html, "html.parser")

    headline = page_soup.find("h1", {"itemprop": "headline"})
    
    text_sections = page_soup.find("div", {"class": "asset-double-wide double-wide p402_premium"}).find_all("p")
    
    article = ""
    for i in text_sections:
        article += i.text

    #Creating a new file for each header
    header = headline.text+"\n"
    header_file_name = "heading_"+str(header_count)+".txt"
    header_file_ptr = open(header_file_name, "a")
    header_file_ptr.write(header)
    header_file_ptr.close()

    #Creating a new file for each article
    article_file_name = "article_"+str(article_count)+".txt"
    article_file_ptr = open(article_file_name, "a")
    article_file_ptr.write(article)
    article_file_ptr.close()

    print("(---------Title----------)")
    print(header)
    print("(---------Article----------)")
    print(article)
    print("(----------End---------)")

    #Incrementing header and article counters
    header_count += 1
    article_count += 1

#Extracting articles from each url in the search results of time
for url in time_article_urls:
    uClient = uReq(url)
    read_html = uClient.read()
    uClient.close()
    page_soup = soup(read_html, "html.parser")

    headline = page_soup.find("h1", {"class": "headline heading-content margin-8-top margin-16-bottom"})
    
    text_sections = page_soup.find("div", {"id": "article-body"}).find_all("p")
    
    article = ""
    for i in text_sections:
        article += i.text

    #Creating a new file for each header
    header = headline.text+"\n"
    header_file_name = "heading_"+str(header_count)+".txt"
    header_file_ptr = open(header_file_name, "a")
    header_file_ptr.write(header)
    header_file_ptr.close()

    #Creating a new file for each article
    article_file_name = "article_"+str(article_count)+".txt"
    article_file_ptr = open(article_file_name, "a")
    article_file_ptr.write(article)
    article_file_ptr.close()

    print("(---------Title----------)")
    print(header)
    print("(---------Article----------)")
    print(article)
    print("(----------End---------)")

    #Incrementing header and article counters
    header_count += 1
    article_count += 1

#Extracting articles from each url in the search results of yahoo
for url in yahoo_article_urls:
    uClient = uReq(url)
    read_html = uClient.read()
    uClient.close()
    page_soup = soup(read_html, "html.parser")

    headline = page_soup.find("h1", {"itemprop": "headline"})
    
    text_sections = page_soup.find("article", {"role":"article"}).find_all("p")
    
    article = ""
    for i in text_sections:
        article += i.text

    #Creating a new file for each header
    header = headline.text+"\n"
    header_file_name = "heading_"+str(header_count)+".txt"
    header_file_ptr = open(header_file_name, "a")
    header_file_ptr.write(header)
    header_file_ptr.close()

    #Creating a new file for each article
    article_file_name = "article_"+str(article_count)+".txt"
    article_file_ptr = open(article_file_name, "a")
    article_file_ptr.write(article)
    article_file_ptr.close()

    print("(---------Title----------)")
    print(header)
    print("(---------Article----------)")
    print(article)
    print("(----------End---------)")

    #Incrementing header and article counters
    header_count += 1
    article_count += 1

#Extracting articles from each url in the search results of science
for url in science_article_urls:
    uClient = uReq(url)
    read_html = uClient.read()
    uClient.close()
    page_soup = soup(read_html, "html.parser")

    headline = page_soup.find("h1", {"class": "header-default__title___2wL7r"})
    
    text_sections = page_soup.find("div", {"class":"single__content___Cm2ty"}).find_all("p")
    
    article = ""
    for i in text_sections:
        article += i.text

    #Creating a new file for each header
    header = headline.text+"\n"
    header_file_name = "heading_"+str(header_count)+".txt"
    header_file_ptr = open(header_file_name, "a")
    header_file_ptr.write(header)
    header_file_ptr.close()

    #Creating a new file for each article
    article_file_name = "article_"+str(article_count)+".txt"
    article_file_ptr = open(article_file_name, "a")
    article_file_ptr.write(article)
    article_file_ptr.close()

    print("(---------Title----------)")
    print(header)
    print("(---------Article----------)")
    print(article)
    print("(----------End---------)")

    #Incrementing header and article counters
    header_count += 1
    article_count += 1

#Extracting articles from each url in the search results of newyorker
for url in newyorker_article_urls:
    uClient = uReq(url)
    read_html = uClient.read()
    uClient.close()
    page_soup = soup(read_html, "html.parser")

    headline = page_soup.find("h1", {"class": "ArticleHeader__hed___GPB7e"})
    
    text_sections = page_soup.find("div", {"id":"articleBody"}).find_all("p")
    
    article = ""
    for i in text_sections:
        article += i.text

    #Creating a new file for each header
    header = headline.text+"\n"
    header_file_name = "heading_"+str(header_count)+".txt"
    header_file_ptr = open(header_file_name, "a")
    header_file_ptr.write(header)
    header_file_ptr.close()

    #Creating a new file for each article
    article_file_name = "article_"+str(article_count)+".txt"
    article_file_ptr = open(article_file_name, "a")
    article_file_ptr.write(article)
    article_file_ptr.close()

    print("(---------Title----------)")
    print(header)
    print("(---------Article----------)")
    print(article)
    print("(----------End---------)")

    #Incrementing header and article counters
    header_count += 1
    article_count += 1

#Extracting articles from each url in the search results of latimes
for url in latimes_article_urls:
    uClient = uReq(url)
    read_html = uClient.read()
    uClient.close()
    page_soup = soup(read_html, "html.parser")

    headline = page_soup.find("h1", {"class": "headline"})
    
    text_sections = page_soup.find("div", {"class":"rich-text-article-body"}).find_all("p")
    
    article = ""
    for i in text_sections:
        article += i.text

    #Creating a new file for each header
    header = headline.text+"\n"
    header_file_name = "heading_"+str(header_count)+".txt"
    header_file_ptr = open(header_file_name, "a")
    header_file_ptr.write(header)
    header_file_ptr.close()

    #Creating a new file for each article
    article_file_name = "article_"+str(article_count)+".txt"
    article_file_ptr = open(article_file_name, "a")
    article_file_ptr.write(article)
    article_file_ptr.close()

    print("(---------Title----------)")
    print(header)
    print("(---------Article----------)")
    print(article)
    print("(----------End---------)")

    #Incrementing header and article counters
    header_count += 1
    article_count += 1

#Extracting articles from each url in the search results of newscientist
for url in newscientist_article_urls:
    uClient = uReq(url)
    read_html = uClient.read()
    uClient.close()
    page_soup = soup(read_html, "html.parser")

    headline = page_soup.find("h1", {"class": "article-title content__title"})
    
    text_sections = page_soup.find("div", {"class":"article-content"}).find_all("p")
    
    article = ""
    for i in text_sections:
        if "Advertisement" not in i.text:
            if "More on these topics:" not in i.text:
                article += i.text

    #Creating a new file for each header
    header = headline.text+"\n"
    header_file_name = "heading_"+str(header_count)+".txt"
    header_file_ptr = open(header_file_name, "a")
    header_file_ptr.write(header)
    header_file_ptr.close()

    #Creating a new file for each article
    article_file_name = "article_"+str(article_count)+".txt"
    article_file_ptr = open(article_file_name, "a")
    article_file_ptr.write(article)
    article_file_ptr.close()

    print("(---------Title----------)")
    print(header)
    print("(---------Article----------)")
    print(article)
    print("(----------End---------)")

    #Incrementing header and article counters
    header_count += 1
    article_count += 1

#Extracting articles from each url in the search results of sciamerican
for url in sciamerican_article_urls:
    uClient = uReq(url)
    read_html = uClient.read()
    uClient.close()
    page_soup = soup(read_html, "html.parser")

    headline = page_soup.find("h1", {"itemprop": "headline"})
    
    text_sections = page_soup.find("div", {"itemprop": "articleBody"}).find_all("p")
    
    article = ""
    for i in text_sections:
        if "Advertisement" not in i.text:
            if "More on these topics:" not in i.text:
                article += i.text

    #Creating a new file for each header
    header = headline.text+"\n"
    header_file_name = "heading_"+str(header_count)+".txt"
    header_file_ptr = open(header_file_name, "a")
    header_file_ptr.write(header)
    header_file_ptr.close()

    #Creating a new file for each article
    article_file_name = "article_"+str(article_count)+".txt"
    article_file_ptr = open(article_file_name, "a")
    article_file_ptr.write(article)
    article_file_ptr.close()

    print("(---------Title----------)")
    print(header)
    print("(---------Article----------)")
    print(article)
    print("(----------End---------)")

    #Incrementing header and article counters
    header_count += 1
    article_count += 1

#Extracting articles from each url in the search results of scinews
for url in scinews_article_urls:
    uClient = uReq(url)
    read_html = uClient.read()
    uClient.close()
    page_soup = soup(read_html, "html.parser")

    headline = page_soup.find("h1", {"class": "header-default__title___2wL7r"})
    
    text_sections = page_soup.find("div", {"class": "single__content___fEQuj"}).find_all("p")
    
    article = ""
    for i in text_sections:
        if "Advertisement" not in i.text:
            if "More on these topics:" not in i.text:
                article += i.text

    #Creating a new file for each header
    header = headline.text+"\n"
    header_file_name = "heading_"+str(header_count)+".txt"
    header_file_ptr = open(header_file_name, "a")
    header_file_ptr.write(header)
    header_file_ptr.close()

    #Creating a new file for each article
    article_file_name = "article_"+str(article_count)+".txt"
    article_file_ptr = open(article_file_name, "a")
    article_file_ptr.write(article)
    article_file_ptr.close()

    print("(---------Title----------)")
    print(header)
    print("(---------Article----------)")
    print(article)
    print("(----------End---------)")

    #Incrementing header and article counters
    header_count += 1
    article_count += 1

#Extracting articles from each url in the search results of week
for url in week_article_urls:
    uClient = uReq(url)
    read_html = uClient.read()
    uClient.close()
    page_soup = soup(read_html, "html.parser")

    headline = page_soup.find("h2", {"class": "sr-headline"})
    
    text_sections = page_soup.find("div", {"class": "sr-body"}).find_all("p")
    
    article = ""
    for i in text_sections:
        if "Advertisement" not in i.text:
            if "More on these topics:" not in i.text:
                article += i.text

    #Creating a new file for each header
    header = headline.text+"\n"
    header_file_name = "heading_"+str(header_count)+".txt"
    header_file_ptr = open(header_file_name, "a")
    header_file_ptr.write(header)
    header_file_ptr.close()

    #Creating a new file for each article
    article_file_name = "article_"+str(article_count)+".txt"
    article_file_ptr = open(article_file_name, "a")
    article_file_ptr.write(article)
    article_file_ptr.close()

    print("(---------Title----------)")
    print(header)
    print("(---------Article----------)")
    print(article)
    print("(----------End---------)")

    #Incrementing header and article counters
    header_count += 1
    article_count += 1

#Extracting articles from each url in the search results of dogonews
for url in dogonews_article_urls:
    uClient = uReq(url)
    read_html = uClient.read()
    uClient.close()
    page_soup = soup(read_html, "html.parser")

    headline = page_soup.find("h1", {"itemprop": "headline"})
    
    text_sections = page_soup.find("div", {"class": "responsive-body"}).find_all("p")
    
    article = ""
    for i in text_sections:
        article += i.text

    #Creating a new file for each header
    header = headline.text+"\n"
    header_file_name = "heading_"+str(header_count)+".txt"
    header_file_ptr = open(header_file_name, "a")
    header_file_ptr.write(header)
    header_file_ptr.close()

    #Creating a new file for each article
    article_file_name = "article_"+str(article_count)+".txt"
    article_file_ptr = open(article_file_name, "a")
    article_file_ptr.write(article)
    article_file_ptr.close()

    print("(---------Title----------)")
    print(header)
    print("(---------Article----------)")
    print(article)
    print("(----------End---------)")

    #Incrementing header and article counters
    header_count += 1
    article_count += 1

#Extracting articles from each url in the search results of onion
for url in onion_article_urls:
    uClient = uReq(url)
    read_html = uClient.read()
    uClient.close()
    page_soup = soup(read_html, "html.parser")

    headline = page_soup.find("h1", {"class": "sc-1efpnfq-0 bzBeT"})
    
    text_sections = page_soup.find("div", {"class": "js_starterpost"}).find_all("p")
    
    article = ""
    for i in text_sections:
        article += i.text

    #Creating a new file for each header
    header = headline.text+"\n"
    header_file_name = "heading_"+str(header_count)+".txt"
    header_file_ptr = open(header_file_name, "a")
    header_file_ptr.write(header)
    header_file_ptr.close()

    #Creating a new file for each article
    article_file_name = "article_"+str(article_count)+".txt"
    article_file_ptr = open(article_file_name, "a")
    article_file_ptr.write(article)
    article_file_ptr.close()

    print("(---------Title----------)")
    print(header)
    print("(---------Article----------)")
    print(article)
    print("(----------End---------)")

    #Incrementing header and article counters
    header_count += 1
    article_count += 1

#Extracting articles from each url in the search results of natrev
for url in natrev_article_urls:
    uClient = uReq(url)
    read_html = uClient.read()
    uClient.close()
    page_soup = soup(read_html, "html.parser")

    headline = page_soup.find("h1", {"class": "article-header__title"})
    
    text_sections = page_soup.find("div", {"class": "article-content"}).find_all("p")
    
    article = ""
    for i in text_sections:
        article += i.text

    #Creating a new file for each header
    header = headline.text+"\n"
    header_file_name = "heading_"+str(header_count)+".txt"
    header_file_ptr = open(header_file_name, "a")
    header_file_ptr.write(header)
    header_file_ptr.close()

    #Creating a new file for each article
    article_file_name = "article_"+str(article_count)+".txt"
    article_file_ptr = open(article_file_name, "a")
    article_file_ptr.write(article)
    article_file_ptr.close()

    print("(---------Title----------)")
    print(header)
    print("(---------Article----------)")
    print(article)
    print("(----------End---------)")

    #Incrementing header and article counters
    header_count += 1
    article_count += 1

#Extracting articles from each url in the search results of livesci
for url in livesci_article_urls:
    uClient = uReq(url)
    read_html = uClient.read()
    uClient.close()
    page_soup = soup(read_html, "html.parser")

    headline = page_soup.find("h1")
    
    text_sections = page_soup.find("div", {"id": "article-body"}).find_all("p")
    
    article = ""
    for i in text_sections:
        article += i.text

    #Creating a new file for each header
    header = headline.text+"\n"
    header_file_name = "heading_"+str(header_count)+".txt"
    header_file_ptr = open(header_file_name, "a")
    header_file_ptr.write(header)
    header_file_ptr.close()

    #Creating a new file for each article
    article_file_name = "article_"+str(article_count)+".txt"
    article_file_ptr = open(article_file_name, "a")
    article_file_ptr.write(article)
    article_file_ptr.close()

    print("(---------Title----------)")
    print(header)
    print("(---------Article----------)")
    print(article)
    print("(----------End---------)")

    #Incrementing header and article counters
    header_count += 1
    article_count += 1

# ------------------------------------------------------------
#
#                   END OF THE WEB CRAWLER
# 
# ------------------------------------------------------------