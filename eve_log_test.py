import codecs
import os
import sys
import time
import traceback
import win32con
import win32evtlog
import win32evtlogutil
import winerror

def readEventLog(server, log_type):
    '''
    Reads the log_type (e.g., "Application" or "System") Windows events from the
    specified server.
    '''
    begin_sec = time.time()
    begin_time = time.strftime('%H:%M:%S  ', time.localtime(begin_sec))

    seconds_per_hour = 60 * 60
    how_many_seconds_back_to_search = seconds_per_hour * 1

    gathered_events = []

    try:
        log_handle = win32evtlog.OpenEventLog(server, log_type)

        total = win32evtlog.GetNumberOfEventLogRecords(log_handle)
        print("Scanning through {} events on {} in {}".format(total, server, log_type))

        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

        event_count = 0
        events = 1
        while events:
            events = win32evtlog.ReadEventLog(log_handle, flags, 0)
            seconds = begin_sec
            for event in events:
                the_time = event.TimeGenerated.Format()
                seconds =1
                if seconds < begin_sec - how_many_seconds_back_to_search: break
 
                if event.EventType == win32con.EVENTLOG_ERROR_TYPE:
                    event_count += 1
                    gathered_events.append(event)
            if seconds < begin_sec - how_many_seconds_back_to_search: break  # get out of while loop as well

        win32evtlog.CloseEventLog(log_handle)
    except:
        try:
            print(traceback.print_exc(sys.exc_info()))
        except:
            print('Exception while printing traceback')
 
    return gathered_events






server = None  # None = local machine
log_type = ["System", "Application", "Security"]
# Pseudo-code for reading Windows Events
log_handle = win32evtlog.OpenEventLog(server, "System")
f=True
while f:
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | \
            win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = win32evtlog.ReadEventLog(log_handle,flags,1)
    # Loop through returned list and do your work
    print("-------------------------------------------------------")
    for i in events:
        print(i.EventID,i.EventType)
    f=False
win32evtlog.CloseEventLog(log_handle)




'''
-------------------------------------------------------
1073748864 4
1073748864 4
1014 2
10016 1
16 4
1073748864 4
1073748864 4
16 4
10016 1
'''