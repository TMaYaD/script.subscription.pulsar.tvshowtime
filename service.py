# coding: utf-8
from tools import *
import xbmcaddon
import update_subscriptions from main
from time import time
from time import asctime
from time import localtime
from time import strftime
from time import gmtime

if settings.value['service'] == 'true':
    sleep(int(settings.value['delayTime']))  # get the delay to allow pulsar starts
    every = 28800  # seconds
    previous_time = time()
    settings.log("Persistent Update Service starting...")
    update_subscriptions(True)
    while (not xbmc.abortRequested) and settings.value["persistent"] == 'true':
        if time() >= previous_time + every:  # verification
            previous_time = time()
            update_subscriptions(True)
            settings.log('Update List at %s' % asctime(localtime(previous_time)))
            settings.log('Next Update in %s' % strftime("%H:%M:%S", gmtime(every)))
        sleep(every/60)

del settings
del browser
