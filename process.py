from multiprocessing import Process,Lock

def f(l,m):
    l.acquire()
    print "hello ,world",m
    l.release()

if __name__ == '__main__':
    l = Lock()
    for i in range(10):
        Process(target=f,args=(l,i)).start()