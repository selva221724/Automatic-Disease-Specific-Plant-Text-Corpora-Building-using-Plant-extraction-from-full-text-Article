from matplotlib import pyplot as plt


# ============================ abstracts sepration based on disaes =================

langs = ['Diabetes', 'Fever', 'Arthritis','Cancer']
students = [186,59,37,256]
plt.bar(langs,students)
plt.ylabel('Number of Abstracts')
plt.xlabel('Disease')
plt.show()


# ============================ abstracts sepration based on disaes =================
#
langs = ['Diabetes', 'Fever', 'Arthritis','Cancer']
students = [55,5,5,4]
plt.bar(langs,students)
plt.ylabel('Number of Abstracts')
plt.xlabel('Disease')
plt.show()




# ================================== diseas absed calssification =======================================================
import numpy as np
import matplotlib.pyplot as plt

N = 4
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

yvals = [186,48,36,256]
rects1 = ax.bar(ind, yvals, width, color='g')
zvals = [188,50,37,267]
rects2 = ax.bar(ind+width, zvals, width, color='b')


ax.set_ylabel('Number of Abstracts')
ax.set_xlabel('Disease')
ax.set_xticks(ind+width/2)
ax.set_xticklabels( ['Diabetes', 'Fever', 'Arthritis','Cancer'])
ax.legend( (rects1[0], rects2[0]), ('Automated', 'Manual') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
plt.title('Disease based Classification')
plt.show()



# ================================== manual vs automatics plants count diease wise =================================
import numpy as np
import matplotlib.pyplot as plt

N = 4
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

yvals = [445,127,31,169]
rects1 = ax.bar(ind, yvals, width, color='g')
zvals = [387,93,27,220]
rects2 = ax.bar(ind+width, zvals, width, color='b')


ax.set_ylabel('Number of Plant Names Detected')
ax.set_xlabel('Disease')
ax.set_xticks(ind+width/2)
ax.set_xticklabels( ['Diabetes', 'Fever', 'Arthritis','Cancer'])
ax.legend( (rects1[0], rects2[0]), ('Automated', 'Manual') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
plt.title('Plant Name Extraction')
plt.show()



# ================================== Totoal number of plants automatics vs manual =================================
langs = ['Automated', 'Manual']
students = [772,727]
plt.bar(langs,students)
plt.bar(langs,[0,727])
plt.ylabel('Number of Plants Extracted')
plt.xlabel('Method')
plt.title('Totoal Number of Plants Extracted in Entire Abstracts')
plt.show()




# ================================== manual vs automatics plants count in individual abstracts =================================
import numpy as np
import matplotlib.pyplot as plt

N = 10
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

yvals = [4,11,2,2,1,20,8,16,24,9]
rects1 = ax.bar(ind, yvals, width, color='g')
zvals = [3,13,1,3,1,17,8,17,24,6]
rects2 = ax.bar(ind+width, zvals, width, color='b')


ax.set_ylabel('Number of Plant Names Detected')
ax.set_xlabel('Individual Abstracts')
ax.set_xticks(ind+width/2)
ax.set_xticklabels([str(i) for i in range(1,len(yvals)+1)])
ax.legend( (rects1[0], rects2[0]), ('Automated', 'Manual') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
plt.title('Plant Name Extraction on Individual Abstracts')
plt.show()



