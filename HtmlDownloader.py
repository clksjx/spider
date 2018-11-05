import requests


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
            print("url is None")
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        headers = {'User-Agent': user_agent}
        print("start requests")
        r = requests.get(url, headers=headers)
        # 判断响应状态
        if r.status_code == 200:
            r.encoding = 'utf-8'
            print("该页面下载成功！{}".format(url))
            return r.text
        else:
            print("该页面下载失败！{}".format(url))
        return None
