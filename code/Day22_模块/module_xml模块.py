"""
xml 文本格式：
<标签名>                                                     ——》最外层，根
    <标签名 属性名=' '>                                       ——》内一层，节点
        <标签名 属性名=''> test </标签名>      # 非自闭和标签，有test
        <标签名 属性名=''> test </标签名>
        <标签名 属性名='' 属性名1=''> test </标签名>
        <标签名 属性名=''/>                   #自闭合标签，无test
        <标签名 属性名='' 属性名1=''/>
    </标签名>
</标签名>
标签名必须有，属性名可有可无，test可有可无
标签名：tag     属性名：attribute       内容：test  不可以是有标签
"""
# python 对 xml 文件的操作
import xml.etree.ElementTree as Tree
tree = Tree.parse('xml_data')       # 导入 xml 文件
root = tree.getroot()               # 获得文件的最外层标签
print(root.tag)                     # 查看标签名
# 得到的是对象，可以进行 for 循环遍历
print(root.iter('year'))            # 全文搜索 year
print(root.find('country'))         # 在根的字节点找，只找一个标签为 country 的全部信息
print(root.find('country').attrib)
print(root.findall('country'))      # 在根的字节点找，找所有标签为 country 的全部信息
# 遍历全文
for item in root:
    # 查看根的下一级的标签名，属性名，属性对应的 key 取值
    print(item.tag, item.attrib, item.attrib['name'])
    for j in item:
        # 查看标签名，属性名，内容 ————》 <>test<>
        print(j.tag, j.attrib, j.text)
# 只遍历 year 节点
for node in root.iter('year'):
    print(node.tag, node.text)
"""
对 xml 文件的 修改 删除
"""
# 修改：针对节点的内容和属性进行操作
for node in root.iter('year'):
    new = int(node.text) + 1
    node.text = str(new)            # 对 test 进行操作
    node.set('update', 'yes')       # 对属性进行操作，加了一个名字
    node.set('version', '1.0')      # 加第二个属性名

tree.write('new_xml.xml')           # 必须要有，它改的内容写到一个文件中，可以是新文件，也可是原文件
# 删除：对子节点来说--》不能跨越节点操作
for country in root.findall('country'):
    rank = int(country.find('rank').text)    # 找到 rank 的内容化为整型
    if rank > 50:
        root.remove(country)                 # 删掉符合条件的 country 节点

tree.write('new_xml.xml')
# # 在 country 下添加新的节点 year2
# for country in root.findall('country'):
#     for year in country.findall('years'):
#         if int(year.text) > 2000:
#             year2 = Tree.Element('year2')
#             year2.attrib = {'update': 'yes'}
#             year2.text = '1'
#             country.append(year2)
#
# tree.write('new_xml.xml')

""" 
怎么删year ？
"""
# for country in root.findall('country'):
#     for year in country.findall('years'):
#         country.remove(year)
#
# tree.write('new_xml.xml')


"""
用 python 语言自己创建 xml 文件
"""
import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
age = ET.SubElement(name, "age", attrib={"checked": "no"})    # 没有内容所以是自闭和标签
sex = ET.SubElement(name, "sex")  # 有内容是自闭和标签
sex.text = '33'
name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
age = ET.SubElement(name2, "age")
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("b.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式