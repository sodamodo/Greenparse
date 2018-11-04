from database import cur
import requests
from bs4 import BeautifulSoup

base_url = "https://www.getphysicianjobs.com"
resume_index = 0
def parse_resume_page(link):
    cookie  = { "as": "true",
                "mname": "hr%40glhstaffing.com",
                "mpass": "millionaire2020",
                "PHPSESSID": "fecbab3a947be9610db4a4384ef23888",
                "_ga": "GA1.2.899379915.1541344436",
                "_gid": "GA1.2.1579575363.1541344436",
                "_fbp": "fb.1.1541344435757.1185368540",
                "_dc_gtm_UA-75029810-1": "1",
                "Refs": "DirectTraffic"}
    r =  requests.get(base_url + link[0], cookies=cookie)
    soup = BeautifulSoup(r.text)
    tags = ["<div>", "</div>", "<p>", "</p>", "<br/>", "<h3>", "</h3>", '<div class="textContent">']
    resume = soup.findAll("div", {"class": "textContent"})[1]
    resume_string = str(resume)
    for tag in tags:
        resume_string = resume_string.replace(tag, "")
    return resume_string

cur.execute("SELECT * from physicians")
# This is a list of tuples
links = cur.fetchall()
# file_limiter = 0
for link in links:
    # if file_limiter > 60:
    #     break
    file = open(str(link[1]) + ".txt", "w")
    file.write(parse_resume_page(link))
    file.close()
    # file_limiter += 1
    print("file writter!")






# resume_string = str(divs[1])

# print(resume_string)
# no_open_p = no_div.replace("<p>", "")
# no_closed_p = no_open_p.replace("<p>", "")
# no_br = no_closed_p.replace("<p>", "")



# print(str(divs[1].p))
# for replacement in replacements:
#     derawed_string = str(divs[1]).replace(replacement[0], replacement[1])
#     print(derawed_string)

# resume = (divs[1].p).replace("<br>", "")
# print(resume)
