import requests
from datetime import date,timedelta,datetime
from bs4 import BeautifulSoup


def bbc_scraper():
    count=1
    bbc_news_info=[]
    for pg_no in range(1,7,1):
        bbc_url="https://www.bbc.com/search/"
        params={
            "q":ask_category,
            "page":pg_no
        }
        headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
        }

        response=requests.get(bbc_url,params=params,headers=headers)
        if response.status_code == 200:
            soup=BeautifulSoup(response.text,"html.parser")
            titles=soup.find_all("h2",class_="sc-9d830f2a-3 duBczH")
            descriptions=soup.find_all("div",class_="sc-cdecfb63-3 pGVVH")
            dates=soup.find_all("span",class_="sc-1907e52a-1 iFYhEd")
            for index,title,description,date_ in zip(list(range(count,count+9,1)),titles,descriptions,dates):
                    try:
                        datetime.strptime(date_.text,"%d %b %Y")
                        actual_date=date_.text 
                    except ValueError:
                        days_ago=int(''.join(filter(str.isdigit,date_.text)))
                        that_date = datetime.now() - timedelta(days=days_ago)
                        actual_date=that_date.strftime("%d %b %Y")
                    news_section={
                        "No":index,
                        "date": actual_date ,
                        "title":title.text,
                        "description":description.text
                    }
                    bbc_news_info.append(news_section)

        count+=9
    match=0
    for info in bbc_news_info:
        if (datetime.now()-datetime.strptime(info["date"],"%d %b %Y")).days <= 7:
            match+=1
        
    print(f"[✓] BBC: {match} articles found")


print("Selected Source:BBC")
ask_category=input("Keyword filter: ").strip().capitalize()
print("Fetching articles for last 7 days....")
bbc_scraper()