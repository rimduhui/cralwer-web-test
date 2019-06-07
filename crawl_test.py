from selenium import webdriver

def get_titles():
    driver = webdriver.Chrome("chromedriver")
    driver.get("http://www.naver.com")
    driver.find_element_by_xpath('//*[@id="query"]').send_keys("화장품")
    driver.find_element_by_xpath('//*[@id="search_btn"]/span[2]').click()
    titles = driver.find_elements_by_css_selector('a.lnk_tit')
    print(titles[0].text, len(titles))

    res = ''
    for title in titles:
        print(title.text)
        res = res + title.text + ', '

    driver.close()

    return res