from bs4 import BeautifulSoup
from selenium import webdriver

# 웹 드라이버 import
# 페이지 html 코드 받기
driver = webdriver.Chrome("./chromedriver")
driver.get("https://gall.dcinside.com/mgallery/board/lists?id=jusik")

# 받은 코드 html로 변환
soup = BeautifulSoup(driver.page_source, "html.parser")

result_list = []

# html 코드 중 게시글의 제목만 받기
for i in soup.select("#container > section.left_content > article:nth-child(3) > div.gall_listwrap.list > table > tbody > tr"):
    print(i.find("td", class_="gall_tit ub-word").text)
    result_list.append(i.find("td", class_="gall_tit ub-word").text[1:].split('\n')[0])

print("result_list")
print(result_list)

#웹 드라이버 종료
driver.close()


