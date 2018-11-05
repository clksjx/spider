import DataOutput
import HtmlDownloader
import HtmlParser
import UrlManager


class SpiderMan(object):
    def __init__(self):
        # 调度器内包含其它四个元件，在初始化调度器的时候也要建立四个元件对象的实例
        self.manager = UrlManager.UrlManager()
        self.downloader = HtmlDownloader.HtmlDownloader()
        self.parser = HtmlParser.HtmlParser()
        self.output = DataOutput.DataOutput()

    def spider(self, origin_url, url_numbers):
        # 添加初始url
        self.manager.add_new_url(origin_url)

        # 下面进入主循环，爬取页面总数小于numbers
        num = 0
        while (self.manager.has_new_url() and self.manager.old_url_size() < url_numbers):
            num = num + 1
            print("正在处理第{}个链接".format(num))

            # 从新url仓库中获取url
            current_url = self.manager.get_new_url()

            # 调用html下载器下载页面
            html = self.downloader.download(current_url)

            # 调用解析器解析页面，返回新的url和data
            new_urls, data = self.parser.parser(current_url, html)
            for url in new_urls:
                self.manager.add_new_url(url)

            # 将已经爬取过的这个url添加至老url仓库中
            self.manager.add_old_url(current_url)

            # 将返回的数据存储至文件
            self.output.store_data(data)
            print("store data successfully")

            print("第{}个链接已经抓取完成".format(self.manager.old_url_size()))
            print("")

        # 爬取循环结束的时候将存储的数据输出至文件
        self.output.output_excel()
