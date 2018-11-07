# -*- coding: utf-8 -*-
"""


takes input file and creates two files ADE aligns and no AED aligns 

@author: hraanan
"""
import sys
import queue
import threading
import time

in_file_name=sys.argv[1]

out_file=open(in_file_name[:-4]+'_NO_ADE.txt','w')
ade_file=open(in_file_name[:-4]+'ADE.txt','w')

head='Source\tTarget\tsource cof\tTarget cof\tQl\tTl\tLigand\tEC distance\tRMSD\tAlign CA\tRaw alignment score\tAligned Residues\tLigand center distance\tStructural Distance\n'
out_file.write(head)
ade_file.write(head)

#NAD=['NAD','ADJ','ENP','NAP','NDP','NJP','NZQ','XNP']

in_file=open(in_file_name,'r')   
in_file.readline()

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, q):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.q = q
   def run(self):
      #print ("Starting " + self.name)
      process_data(self.name, self.q)
      #print ("Exiting " + self.name)

def process_data(threadName, q):
   
    while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
        line = q.get()
        queueLock.release()

        try:
            line=line.split('\t')
            if line[0].split('_')[0].split('.')[1]=='ADE' or line[1].split('_')[0].split('.')[1]=='ADE' :
                ade_file.write('\t'.join(line))
            else:
                out_file.write('\t'.join(line))
            
    
        except Exception as e:
             print (line)
             print(e)
             continue

queueLock = threading.Lock()
workQueue = queue.Queue(len(pdb_list))
threads = []
threadID = 1

# Create new threads
t0 = time.time()

for ti in range(50):
   tName='Thread-'+str(ti)
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Fill the queue
queueLock.acquire()
for line in in_file:
   workQueue.put(line)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()

t1 = time.time()

total = t1-t0
print(total)
print ("Exiting Main Thread")


   
out_file.close()
ade_file.close()
print('end')
#'''

