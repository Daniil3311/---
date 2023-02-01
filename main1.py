from pprint import pprint
import re
import csv
import os
import datetime

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def function1(contacts_list):
 i=0
 while i<8:
  i += 1
  x = 0
  c = (contacts_list[i][0].split())
  if len(c)==1:
      c.append(contacts_list[i][1])
      c.append(contacts_list[i][2])
  #print(c)
  if i == 3:
   c = (contacts_list[i][1].split())
   c.insert(0, contacts_list[3][0])
  while x<3:
     if len(c)==2:
         if x==2:
             break
     #print()
     contacts_list[i][x]=c[x]
     x += 1

function1(contacts_list)


newlist = []
def function2(newlist):
 for x in range(9):
    innerlist = []
    for y in []:
        innerlist.append(y)
    newlist.append(innerlist)

function2(newlist)


def function3(newlist,contacts_list):
 t=0
 l2=0
 lists=[]
 while l2<8:
  l2 += 1
  t += 1
  for x,value in enumerate(contacts_list):
     if contacts_list[l2][0] in value:
         newlist[t].append(x)

function3(newlist,contacts_list)


def function4(newlist,contacts_list):
 l1=0
 p1=0
 while l1 < 8:
  l1 += 1
  if len(newlist[l1]) > 1:
   l3 = newlist[l1][1]
   if contacts_list[l1][0] in contacts_list[l1]:
      p1=0
      while p1 < 6:
       p1 += 1
       if contacts_list[l1][p1] == '':
            contacts_list[l1][p1]=contacts_list[l3][p1]

function4(newlist,contacts_list)


def removing_duplicate_elements():
    for x in newlist:
       if newlist.count(x) > 1:
          newlist.remove(x)
    l4=7
    while l4>1:
        l4-=1
        if len(newlist[l4])>1:
           l5=newlist[l4][1]
           contacts_list.pop(l5)
removing_duplicate_elements()
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)

pattern = r'(\+7|8)(\s*\(*)(\d{3})(\s*\)*|\s)(\s*|-*)(\d{3})(\-*|\s*)(\d{2})(\-*|\s*)(\d{2})(\s*)(\()?(\w{3})?(\.|s?)(\s?\d*)\)'
res = re.sub(pattern, r"+7(\3)\6-\8-\10 \13.\15", str(contacts_list))
print(newlist)
print(res)
