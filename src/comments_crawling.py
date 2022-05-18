from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#주소, 이후에 동적으로 할 것
url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%99%B8%EA%B3%84%EC%9D%B8&oquery=&tqi=hogeesprvN8ssbu1KOCssssstDw-054309'
 
#웹 드라이버
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)

#네이버 뉴스 클릭
select_news = driver.find_element(by=By.CSS_SELECTOR, value='#sp_nws1 > div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a:nth-child(3)')
select_news.click()
time.sleep(5)

#새로 열린 탭으로 이동 (이동안하면 첫번째 탭에 머물러있음)
driver.switch_to.window(driver.window_handles[1])

#댓글모음으로 이동
move_comments = driver.find_element(by=By.CSS_SELECTOR, value='#comment_count')
move_comments.click()
time.sleep(5)
 
#클린봇 클릭
cleanbot = driver.find_element(by=By.CSS_SELECTOR, value='a.u_cbox_cleanbot_setbutton')
cleanbot.click()
time.sleep(1)
cleanbot_disable = driver.find_element(by=By.XPATH, value="//input[@id='cleanbot_dialog_checkbox_cbox_module']")
cleanbot_disable.click()
time.sleep(1)
cleanbot_confirm = driver.find_element(by=By.CSS_SELECTOR, value='div.u_cbox_layer_cleanbot2_extra > button')
cleanbot_confirm.click()
time.sleep(1)

# 더보기 계속 클릭
while True:
    try:
        btn_more = driver.find_element(by=By.CSS_SELECTOR, value='a.u_cbox_btn_more')
        btn_more.click()
        # time.sleep(1)
    except:
        break
 
#댓글추출 (contents => 댓글 내용 / writeTimes => 댓글 작성 시간)
contents = driver.find_elements(by=By.CSS_SELECTOR, value='span.u_cbox_contents')
writeTimes = driver.find_elements(by=By.CSS_SELECTOR, value='span.u_cbox_date')

cnt = 1;
for content, writeTime in zip(contents, writeTimes):
    print(cnt, content.text, writeTime.text)
    cnt+=1

# 첫번째 뉴스 댓글 크롤링 마치면 현재 탭을 닫고 검색 탭으로 이동
driver.close()
driver.switch_to.window(driver.window_handles[0])

# 두번째 뉴스 클릭 (셀렉터가 많이 달라서 xpath로 시도해볼것..)
select_news = driver.find_element(by=By.CSS_SELECTOR, value='#sp_nws6 > div > div > div.news_info > div.info_group > a:nth-child(3)')
select_news.click()
time.sleep(5)

# 두번째 뉴스 탭으로 이동
driver.switch_to.window(driver.window_handles[1])

#이동 확인 후 크롤링 종료
driver.quit()