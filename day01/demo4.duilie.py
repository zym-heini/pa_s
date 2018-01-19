#coding=utf8
import Queue

#队列的特点：线程安全的

q1 = Queue.Queue()

#添加数据
q1.put("a")
q1.put("b")
q1.put("c")
q1.put("d")

#打印展示队列中的数据
print q1.queue
print q1.get()
print q1.get()
print q1.get()
print q1.queue
print"###################################"

#栈队列
q2 = Queue.LifoQueue()

q2.put("1")
q2.put("2")
q2.put("3")
q2.put("4")
q2.put("5")
print q2.queue,q2.qsize()
print q2.get()
print q2.get()
print q2.get()
print q2.get()
print q2.queue,q2.qsize()
