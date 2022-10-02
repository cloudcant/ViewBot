import threading
import random
import requests
import sys
#this disables error messages btw so dont ask me
class DevNull:
    def write(self, msg):
        pass

sys.stderr = DevNull()

t = 0
threadcount = 0
views = int("1000000")
threads = int("1000")
sendurl = ("https://camo.githubusercontent.com/6598833b36ca89a5ea60b68e7f3d6a1ca827cdf60e330963d876b46f5005cb72/68747470733a2f2f677076632e6172747572696f2e6465762f73796e74686574696363")

def main():
  reqcount = round(views/threads)
  URL = "https://raw.githubusercontent.com/cloudcant/useragents/main/Useragents.txt"
  response = requests.get(URL)
  open("Useragents.txt", "wb").write(response.content)
  lines = open('Useragents.txt').read().splitlines()
  myline = random.choice(lines)

  user_agent = {'User-agent': myline}
  print(f"> Loaded UserAgent On Thread")
  i = 0
  sent = 0

  while i < (views/threads):
    i = i + 1
    sent = sent+1
    reqcount = reqcount
    response = requests.get(sendurl, headers = user_agent)
    print(f"> Thread | Target Requests: {views} | Current Thread Requests: {sent}/{reqcount} ")

if t == 0:
    for i in range(threads):
        threading.Thread(target=main).start()
        threadcount = threadcount+1
        print(f"> Thread loaded | {threadcount}/{threads}")
                
print(f"> {threads} Threads Loaded")