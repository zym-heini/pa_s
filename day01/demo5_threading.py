#coding=utf8
#引入模块
import requests
import Queue #url资源数据的核心保存模块
import threading

#多线程访问共享数据
lock = threading.Lock()

#创建一个保存url地址的队列
url_queue = Queue.Queue()

#添加所有需要爬取的地址

for pageno in range(0,15):
    url_queue.put("https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&ie=utf-8&pn=" + str(pageno*50))

#打印所有需要爬取的队列中的url地址

print url_queue.queue

def spider(urlqueue):
    #开始爬取，队列中还有未操作的url是程序不会停
    while urlqueue.qsize>0:
        #给可能出现数据访问冲突的代码块加锁
        if lock.acquire():
            #获取url地址
            url = urlqueue.get()
            print("剩余数据：%s；线程%s开始对%s进行爬取" % (urlqueue.qsize(), threading.currentThread().name, url))
            header = {
                "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.7 Safari/537.36"
            }
            response = requests.get(url,headers = header)
            filname = url[-20:] + ".html"

            with open("daystext/%s"%filname,"w")as f:
                f.write(response.text.encode("utf-8"))

            print "对%s目标地址爬取完成"%url
            #执行完成 解锁数据
            lock.release()


#程序入口  指定多线程
if __name__ == '__main__':
    #声明一个变量，保存多个线程
    threads = []

    #声明一个变量 控制多少个线程

    thread_name = 3

    #创建线程对象

    for ct in range(0,thread_name):
        #创建线程对象
        current_thread = threading.Thread(target = spider,args = (url_queue,))
        current_thread.start()
        #将线程保存在队列中
        threads.append(current_thread)
        #让所有的线程join,就是让主线程等待所有子线程运行结束再退出
    for i in threads:
        i.join()

    print("程序执行结束......")
