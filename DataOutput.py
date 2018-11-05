import xlsxwriter


class DataOutput(object):
    def __init__(self):
        self.data_set = []  # 可以将数据暂存在这个列表里

    # 每个循环调用一次此函数，暂存数据
    def store_data(self, data):
        if data is None:
            print("data is None")
            return
        self.data_set.append(data)

    # 全部页面爬取结束后调用此函数，写入文件
    def output_excel(self):
        # 创建一个excel表格
        workbook = xlsxwriter.Workbook('data' + '.xlsx')
        # 为创建的excel表格添加一个工作表
        worksheet = workbook.add_worksheet()

        # 将data中的三个数据写成表格的一行
        row = 0
        for data in self.data_set:
            worksheet.write(row, 0, data["url"])
            worksheet.write(row, 1, data["title"])
            worksheet.write(row, 2, data["summary"])
            row += 1

        workbook.close()
        self.data_set = []  # 清空表格，释放内存
