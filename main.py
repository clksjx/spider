import SpiderMan

# 链接不能含有中文
origin_url = "https://baike.baidu.com/item/%E9%A6%99%E6%B8%AF%E5%A4%A7%E4%BC%9A%E5%A0%82"
total_url_number = 10

if __name__ == '__main__':
    mySpider = SpiderMan.SpiderMan()
    mySpider.spider(origin_url, total_url_number)

