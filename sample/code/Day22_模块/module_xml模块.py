"""
xml 文本格式：
        <>test</>   非自闭和标签
        </>         自闭和标签
<标签名>                                                     ——》最外层，根
    <标签名 属性名=' '>                                       ——》内一层，节点
        <标签名 属性名=''> test </标签名>      # 非自闭和标签，有test
        <标签名 属性名=''> test </标签名>
        <标签名 属性名='' 属性名1=''> test </标签名>
        <标签名 属性名=''/>                   # 自闭合标签，无test
        <标签名 属性名='' 属性名1=''/>
    </标签名>
</标签名>
标签名必须有，属性名可有可无，test可有可无
标签名：tag     属性名：attribute ：字典格式       内容：test  不可以是有标签
"""
# ——————————————》 查询
# python 对 xml 文件的操作
import xml.etree.ElementTree as Tree
file = Tree.parse('xml_data')       # 导入 xml 文件
root = file.getroot()               # 获得文件的最外层标签
print(root.tag)                     # 查看标签名
# 得到的是对象，可以进行 for 循环遍历
print(root.iter('year'))            # 全文搜索 year
print(root.find('country'))         # 在根的字节点找，只找一个标签为 country 下的的全部信息
print(root.findall('country'))      # 在根的字节点找，找所有标签为 country 的全部信息
print(root.find('country').attrib)  # {'name': 'Liechtenstein'}
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

file.write('new_xml.xml')           # 必须要有，它改的内容写到一个文件中，可以是新文件，也可是原文件
# 删除：对子节点来说--》不能跨越节点操作
"""
remove 删除的节点的 text
"""
# ——————》 root.remove
for country in root.findall('country'):
    rank = int(country.find('rank').text)    # 找到 rank 的内容化为整型
    if rank > 50:
        root.remove(country)                 # 删掉符合条件的 country 节点
file.write('new_xml.xml')
root.remove(root.find('country'))    # 删除第一个country的所有信息
file.write('哈哈2.xml')
# ——————》 删除节点下的节点,删除第一个country 下的year
a = root.find('country')
for i in a:
    if i.tag == 'year':
        a.remove(i)
file.write('xml_data')
# ————————》 追加
# 在 country 下添加新的节点 year2
for country in root.findall('country'):
    for year in country.findall('year'):
        if int(year.text) > 2000:
            year2 = Tree.Element('year2')
            year2.attrib = {'update': 'yes'}
            year2.text = '1'
            country.append(year2)

file.write('new_xml.xml')


"""
用 python 语言自己创建 xml 文件
"""
import xml.etree.ElementTree as xT

root = xT.Element('公司人员')

node = xT.SubElement(root, 'message', attrib={'update': 'yes'})
next_level_node_name = xT.SubElement(node, '洪吉昌', attrib={"enrolled": "yes"})
# 无 text 的是自闭和标签
next_level_node_age = xT.SubElement(node, 'age')
next_level_node_age.text = '18'                     # text 接收的数据类型必须是字符串
# 有 text 的是非自闭和标签
next_level_node_gender = xT.SubElement(node, '性别')
next_level_node_gender.text = 'male'

node1 = xT.SubElement(root, 'message1', attrib={'enrolled': 'no'})
next_level_node1_name = xT.SubElement(node1, '洪淑芳', attrib={'update': 'yes'})
next_level_node1_age = xT.SubElement(node1, 'age')
next_level_node1_age.text = '20'
next_level_node1_gender = xT.SubElement(node1, 'gender')
next_level_node1_gender.text = 'female'

obj = xT.ElementTree(root)      # 生成 xml 文件对象
obj.write('公司人员.xml', encoding='utf8', xml_declaration=True)
# method 默认方法是 xml 还有 hxml 等等
xT.dump(root)                   # 打印生成格式到终端
