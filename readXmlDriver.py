from xml.dom import minidom


class ReadXmlDriver(object):
    def RXmlText(self,filename, firstnode, secondnode):
        # 获取数据储存路径
        root = minidom.parse('D://PyProjects/xmlFiles/'+filename+".xml")
        # 获取数据所在上级标签
        OneNode = root.getElementsByTagName(firstnode)[0]
        # 获取数据所在标签
        twoNode = OneNode.getElementsByTagName(secondnode)[0].childNodes[0].nodeValue
        return twoNode
