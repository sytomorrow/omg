import HTMLTestRunner

class TestReportRunner(object):
    def getReport(self, fileName,ti,desc,suite):
        #定义报告存放路径
        fp = open("D:/PyProjects/report/" + fileName + ".html", "wb")
        # 定义测试报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=ti,description=desc)
        # 运行测试
        runner.run(suite)   #调用suite函数，将测试用例名称传入函数中
        fp.close()  # 关闭文件对象把数据写进磁盘,关闭文件流，不关的话生成的报告是空的