import unittest
from commonality import testReport
h=testReport.TestReportRunner()
class ppprson(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def testgetPerson(self):
        print("Person")

    def testd(self):
        print(1)

    def teste(self):
        print(3)
    def testp(self):
        print(2)

if __name__=="__main__":
    #该类下的全部用例
    # suite=unittest.makeSuite(ppprson)
    #选择某些用例执行
    suite=unittest.TestSuite()
    suite.addTest(ppprson("teste"))
    suite.addTest(ppprson("testp"))
    # runner=unittest.TextTestRunner()
    # runner.run(suite)
    #测试报告
    h.getReport("123","试一试看","看走不走",suite)
