from datetime import datetime
from time import time, ctime

# wake up hours. integers [0-23]
alarms = [12, 0, 22, 9]

def sleepy(alarms):
    now = datetime.now()
    epoch = time()
    for _ in range(16):
        # alarms converted to datetime objects
        dt_alarms = [now.replace(hour=x, minute=0, second=0) for x in alarms]
        # timedeltas (in seconds) between now and wakeup times
        difference = [(x - now).seconds for x in dt_alarms if x != now]
        # in case of single alarm
        closest = 24 * 60 * 60 if not difference else min(difference)  
        epoch += closest
        print('Now {}.\nI will be sleeping {} seconds and wake up on {}\n'.format(
            ctime(epoch - closest), closest, ctime(epoch)))
        now = datetime.fromtimestamp(epoch)

if __name__ == '__main__':
    sleepy(alarms)
