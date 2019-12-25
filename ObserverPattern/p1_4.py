#%%
import time
from abc import ABCMeta, abstractclassmethod
#from ObserverPattern import p1_2
from p1_2 import Observer, Observable


# %%
class Account(Observable):
    """define user account"""
    def __init__(self):
        super().__init__()
        self._latestIp = {}       # set this attribute as a dictionary
        self._latestRegion = {}

    def login(self, name, ip, time):
        region = self._getRegion(ip)
        if self._isLongDistance(name, region):
            self.notifyObservers({"name":name, "ip":ip,"region":region, "time":time})
        self._latestRegion[name] = region  # verify if change region befor reset region
        self._latestIp[name] = ip     # set element in this dictionary as { name:ip }
        

    def _getRegion(self, ip):
          # call ip address service
         ipRegions = {
              "101.47.18.9":"china hungzhu",
              "67.218.147.69":"USA LA"
         }
         region = ipRegions.get(ip)
         return "" if region is None else region

    def _isLongDistance(self, name, region):
        # call geographical service
        latestRegion = self._latestRegion.get(name)
        return latestRegion is not None and latestRegion != region




# %%
class SmsSender(Observer):
    def update(self, observable, object):
         print("SMS send"+object["name"]+object["region"]+object["ip"]+
               time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"]))
            )
        
class MailSender(Observer):
    def update(self, observable, object):
         print("MAIL send"+object["name"]+object["region"]+object["ip"]+
               time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"]))
            )


# %%
def testLogin():
    accout = Account()
    accout.addObserver(SmsSender())
    accout.addObserver(MailSender())
    accout.login("Tony","101.47.18.9",time.time())
    accout.login("Tony","67.218.147.69",time.time())

# %%
testLogin()

# %%
