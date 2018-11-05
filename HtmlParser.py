from bs4 import BeautifulSoup
import urllib  # 用来拼接url
import re  # 正则表达式模块


class HtmlParser(object):
    def parser(self, page_url, html_cont):
        """
        解析器主函数
        parm page_url:一个url
        parm html_cont:网页内容，格式为字符串
        return: urls, 数据；格式为 set, dict
        """
        if page_url is None or html_cont is None:
            print("page_url is None")
            return

        # 建立bs对象，使用html.parser进行解析
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='urf-8')
        print("soup established")

        # 接下来分别调用两个私有函数返回urls和data
        new_urls = self._get_new_urls(page_url, soup)
        print("new_urls get")

        new_data = self._get_new_data(page_url, soup)
        print("new_data get")

        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        """
        从页面中抽取指向其他词条的链接
        parm page_url: 当前页面url
        parm soup: beautifulsoup对象
        return: 新url的set
        """
        new_urls = set()
        # 根据正则表达式规则对页面内的链接进行筛选，留下想要的链接
        links = soup.find_all('a', href=re.compile(r'/item/.+'))
        for link in links:
            # 每个link都是Tag对象，Tag对象的操作方法与字典相同
            new_url = link['href']
            # 借助urljoin，可以很方便地拼接url
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        """
        提取想要的数据
        parm page_url: 当前页面url
        parm soup: beautifulsoup对象
        return: dict
        """
        # 声明字典
        data = {}
        data['url'] = page_url
        data['title'] = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1').get_text()
        data['summary'] = soup.find('div', class_='lemma-summary').get_text()

        return data
