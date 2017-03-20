# coding=utf-8
from selenium import webdriver
from bs4 import BeautifulSoup

class gotscores:
    school_dict = {}
    def __init__(self):
        driver = webdriver.PhantomJS(executable_path='C:\Program Files (x86)\Python35-32\Lib\site-packages/phantomjs')
        for page_num in range(1,12):
            url = "http://gkcx.eol.cn/soudaxue/querySpecialtyScore.html?recomschoolflag=211%E5%B7%A5%E7%A8%8B&recomyear=2014&argprovince=%E6%B2%B3%E5%8D%97&argluqutype=%E7%90%86%E7%A7%91&scoreSign=3&argkeyword=%E8%AE%A1%E7%AE%97%E6%9C%BA&page="+str(page_num)
            driver.get(url)
            print("Got url num %s."%page_num)
            #print(driver.current_url)
            soup = BeautifulSoup(driver.page_source,"lxml")
            #print(soup.text)
            table = soup.find("table",{"id":"queryschoolad"})
            trs = table.tbody.findAll("tr")
            #print(len(trs))
            #schools = []
            for tr in trs:
                tds = tr.findAll("td")
                if(len(tds)==0):
                    continue
                school_name = tds[0].attrs["title"]
                #schools.append(school_name)
                score = tds[6].string
                self.school_dict[school_name] = score
            print("Page num%s solved."%page_num)

        print("Crawling finished.")

    def save2file(self):
        file = open('C:\Study\schools.txt','w+')
        for k,v in  self.school_dict.items():
            file.write(k)
            file.write('\t')
            file.write(v)
            file.write('\n')
        print("File saveing finish.")
        file.close()

if __name__ == '__main__':
    gotscore = gotscores()
    gotscore.save2file()