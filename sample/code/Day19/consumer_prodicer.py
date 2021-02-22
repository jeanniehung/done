"""
生产者消费者模型：
单线并发
"""
import time
f_l = ['蒸羊羔', '蒸鹿茸', '蒸熊掌', '烧素鸭', '烧素鹅', '烧鹿尾']


def consumer(name):
    print('【%s】来到牛气大酒店，服务员上菜单' % name)
    while True:
        food = yield
        time.sleep(0.1)
        print('【%s】美味地吃着【%s】' % (name, food))


def producer(food_list):
    c1 = consumer('洪吉昌')
    c1.send(None)
    print(food_list)
    while True:
            choice = input('点单（y）or 退出（q）:').strip()
            if choice.upper() == 'Q':

                break
            if choice.upper() == 'Y':
                while True:
                    for i in range(len(food_list)):
                        print(i, food_list[i])
                    inp_choice = input('请选择你想吃的菜：').strip()
                    if inp_choice.upper() == 'Q':

                        break
                    if not inp_choice or int(inp_choice) > len(food_list):
                        continue
                    time.sleep(0.1)
                    c1.send(food_list[int(inp_choice)])
            if not choice or choice != 'Q' and 'Y':
                print('请快点选择，如需帮助，请叫服务员')
                continue
            break


producer(f_l)

