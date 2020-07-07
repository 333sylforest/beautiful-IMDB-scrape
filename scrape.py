import csv
import requests
from bs4 import BeautifulSoup
from time import sleep

with open('/Users/kimberleyellars/github/beautiful-IMDB-scrape/scrape.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')#, quotechar="", quoting=csv.QUOTE_MINIMAL)

    URL = "https://www.imdb.com/search/title/?genres=sci_fi&sort=user_rating,desc&title_type=tv_series,mini_series&num_votes=5000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f85d9bf4-1542-48d1-a7f9-48ac82dd85e7&pf_rd_r=JEEQAKRDH2F2GVHC23BC&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=toptv&ref_=chttvtp_gnr_20"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_ = "lister-list")
    movies = results.find_all(class_ = "lister-item-content")
    for movie in movies:
        sleep(.1)
        rank = movie.find(class_ = "lister-item-index").text.strip()
        name_card= str(movie.find(class_ = "lister-item-header"))
        names= name_card.split('>')
        name_= names[4]
        names2 = name_.split('<')
        name = names2[0]
        #name = movie.find(class_= "lister item header").text
        length = movie.find(class_ = "runtime")
        if length==None:
            length = "?"
        else:
            length = length.text.strip()
        genre = movie.find(class_ = "genre").text.strip()
        rating = movie.find(class_ = "ratings-imdb-rating").text.strip()
        csv_writer.writerow([rank,name,length,genre,rating])
