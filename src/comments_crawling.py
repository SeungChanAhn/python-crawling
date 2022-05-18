from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#주소, 이후에 동적으로 할 것
url = 'https://n.news.naver.com/mnews/ranking/article/comment/056/0011268381?sid=001'
 
#웹 드라이버
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)
 
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

# 더보기 클릭
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

driver.quit()