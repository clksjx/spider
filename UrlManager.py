class UrlManager(object):
    def __init__(self):
        # 初始化的时候就生成两个url仓库
        self.new_urls = set()
        self.old_urls = set()

    # 判断新url仓库中是否还有没有爬取的url
    def has_new_url(self):
        return len(self.new_urls)

    # 从new_url仓库获取一个新的url
    def get_new_url(self):
        return self.new_urls.pop()

    # 将一条url添加到new_urls仓库中
    def add_new_url(self, url):
        if url is None:
            return
        # 只需要判断old_urls中没有该链接即可，new_urls在添加的时候会自动去重
        if url not in self.old_urls:
            self.new_urls.add(url)

    # 将多条url添加到new_urls仓库中
    def add_new_urls(self, urls):
        print("start add_new_urls")
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def add_old_url(self, url):
        self.old_urls.add(url)
        print("add old url successfully")

    # 获取已经爬取过的url的数目
    def old_url_size(self):
        return len(self.old_urls)
