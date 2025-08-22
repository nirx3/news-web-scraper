import requests
from datetime import timedelta,datetime,timezone
from bs4 import BeautifulSoup

# main function
def web_scraper():
    total_result=0
    # BBC 
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
                            if "days" in date_.text or "day" in date_.text:
                                that_date = datetime.now() - timedelta(days=days_ago)
                                actual_date=that_date.strftime("%d %b %Y")
                            elif "hours" in date_.text or "hour" in date_.text:
                                actual_date=datetime.now()
                        news_section={
                            "No":index,
                            "Date": actual_date ,
                            "Title":title.text,
                            "Description":description.text
                        }
                        bbc_news_info.append(news_section)
            else:
                print("Error occured")
                break
            count+=9
        match=0
        for info in bbc_news_info:
            if (datetime.now()-datetime.strptime(info["Date"],"%d %b %Y")).days <= 7:
                match+=1
        nonlocal total_result
        total_result += match
            
        print(f"\n[✓] BBC: {match} articles found")

    #techcrunch
    def techcrunch_scraper():
        techcrunch_info=[]
        count = 1
        for pg_no in range(1,4,1):
            base_url=f"https://techcrunch.com/page/{pg_no}/"
            params={
                "s": ask_category,
            }
            headers={
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
            }
            response=requests.get(base_url,params=params,headers=headers)
            if response.status_code == 200:
                soup=BeautifulSoup(response.text,"html.parser")
                titles=soup.find_all("h3", class_="loop-card__title")
                dates=soup.find_all("time" , class_="loop-card__meta-item loop-card__time wp-block-tc23-post-time-ago") 
                for no,title,date_ in zip(list(range(count ,count+30,1)),titles,dates):
                    news_section={
                        "No": no,
                        "Title" : title.text,
                        "Date" : date_.get("datetime")
                    }
                    techcrunch_info.append(news_section)
            else:
                print("error")
                break
            count+=30

        match=0
        for info in techcrunch_info:
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            _current_date=datetime.strptime(current_date,"%Y-%m-%d %H:%M:%S")
            proper_timezone=timezone(timedelta(hours=5,minutes=45))
            published_date=datetime.fromisoformat(info["Date"])
            _published_date=(published_date.astimezone(proper_timezone)).strftime("%Y-%m-%d %H:%M:%S")
            if (_current_date - datetime.strptime(_published_date,"%Y-%m-%d %H:%M:%S")).days <=7:
                match+=1
        nonlocal total_result
        total_result+=match
        print(f"[✓] Techcrunch: {match} articles found")
        
    #calling web_scrapers
    bbc_scraper()
    techcrunch_scraper()
    print(f"\nTotal relevant articles:{total_result}")


print("Selected Source:BBC, Techcrunch")
ask_category=input("Keyword filter: ").strip().capitalize()
print("\nFetching articles for last 7 days....")
web_scraper()