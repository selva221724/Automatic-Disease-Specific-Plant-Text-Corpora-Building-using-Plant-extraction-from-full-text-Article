import json
import nltk
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import checkPlantName as c
from natsort import natsorted
import shutil
from pathlib import Path

import glob
files = glob.glob('/mnt/dash/Alpha_Share/Automation_Team/Tamil/NLP_learning/Plant_names/own_script/ALL/*.txt')
files = natsorted(files)

out = '/mnt/dash/Alpha_Share/Automation_Team/Tamil/NLP_learning/Plant_names/own_script/out'



def split_abstract(files,out):
    diseas = ['diabet','fever','arthriti']
    for i in diseas:
        if not os.path.exists(out+'/'+i):
            os.mkdir(out+'/'+i)
        for j in files:
            try:
                with open(j, encoding='utf-8') as f:
                    text = f.read()
            except:
                try:
                    with open(j, encoding='utf-16') as f:
                        text = f.read()
                except:
                    with open(j, encoding='latin-1') as f:
                        text = f.read()
            if i in text:
                name = Path(j).name
                shutil.copy(j,out+'/'+i+'/'+name)


split_abstract(files,out)

#
#
# data = files[0]
# with open(data, encoding='utf-8') as f:
#     text = f.read()
#
# # ================================ remove stop words ===========================================
#
# stop_words = set(stopwords.words('english'))
#
# word_tokens = word_tokenize(text)
#
# filtered_sentence = [w for w in word_tokens if not w in stop_words]
#
# filtered_sentence = []
# for w in word_tokens:
#     if w not in stop_words:
#         filtered_sentence.append(w)
#
#
# filtered_sentence = [i for i in filtered_sentence if not len(i) == 2]
#
# # ============================= remove int ===============================
#
# f=[]
# for i in filtered_sentence:
#     try:
#         a = int(i)
#     except:
#         f.append(i)
# # ======================================== remove all caps words ======================
# cap = [i for i in f if not i.isupper()]
# # ======================================== get only first caps words ======================
# cap = [i for i in cap if i[0].isupper()]
#
# # ======================================= find any - alpha numerica=======================
#
# cap = [ i for i in cap if i.isalnum()]
#
# # ======================================== remove englihs words =====================
# import enchant
# d = enchant.Dict("en_US")
# cap = [i for i in cap if not d.check(i)]
#
# # ============================= remove if more than two capital letters =======================
#
# sliced =[]
# for i in cap:
#     count=0
#     for j in i:
#         if j.isupper():
#             count+=1
#     if not count <1:
#         sliced.append(i)
#
# cap = sliced
# #  ================================ check if it is a plant name ==================
# cap = [i for i in cap if c.find_plant(i,'')]
# cap = list(set(cap))
#
#
# plant_list =[]
# for i in cap:
#     match_list = [k for k, e in enumerate(filtered_sentence) if e == i]
#     for j in match_list:
#         plant_list.append(filtered_sentence[j]+' '+filtered_sentence[j+1])
