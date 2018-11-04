pythoimport requests
from bs4 import BeautifulSoup
from database import cur
from time import sleep

base_url = "https://www.getphysicianjobs.com"
sample_url = "https://www.getphysicianjobs.com/employers/search-resumes-results.php?p={page_num}&kw=Physicians&city=New%20York&province=&state=New%20York&country=219&sm=and&submit=Search"
page_num = 1
cookie  = { "as": "true",
            "mname": "hr%40glhstaffing.com",
            "mpass": "millionaire2020",
            "PHPSESSID": "fecbab3a947be9610db4a4384ef23888",
            "_ga": "GA1.2.899379915.1541344436",
            "_gid": "GA1.2.1579575363.1541344436",
            "_fbp": "fb.1.1541344435757.1185368540",
            "_dc_gtm_UA-75029810-1": "1",
            "Refs": "DirectTraffic"}


resume_link_list = []
last_page = False

def populate_resume_link_list():
    r = requests.get(sample_url.format(page_num=page_num), cookies=cookie)
    soup = BeautifulSoup(r.text, features="lxml")
    # print(soup)

    candidate_rows = soup.findAll("td", {"class": "nowrap"})
    print("Candidate rows..." ,candidate_rows)
    for i in candidate_rows:
        try:
            link = i.a['href']
            id = link.split("=")
            print("id num", id[1])

            cur.execute("INSERT into physicians VALUES ('{}', '{}')".format(i.a['href'], id[1]))
        except:
            continue




populate_resume_link_list()
page_num += 1

while (last_page == False):
    try:
        if (requests.get(sample_url.format(page_num=page_num), cookies=cookie) == requests.get(sample_url.format(page_num=page_num - 1), cookies=cookie)):
            last_page = True
    except:
        sleep(60)
        if (requests.get(sample_url.format(page_num=page_num), cookies=cookie) == requests.get(sample_url.format(page_num=page_num - 1), cookies=cookie)):
            last_page = True

    try:
        populate_resume_link_list()

    except:
        sleep(60)

    page_num += 1
    print("next!")
