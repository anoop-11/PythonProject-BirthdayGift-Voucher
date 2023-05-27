#!/usr/bin/env python
# coding: utf-8

# ## Challenge : Birthday Gift Voucher

# In[78]:


emp_details={"John Lee":"12-12-1976",
             "Tim Brooks":"11-04-1980",
             "Alice Cook":"07-1-1978",
             "Joshua John":"05-02-1991",
             "Alisa Matt":"03-04-1990"}

def christmas_greeting(name):
    print('''\n Dear {},
        Wishing you a very Happy Birthday! On behalf of your Birthday
        and the Upcomming Christmas Season, We offer you a gift
        '''.format(name))
          
def veterans_greeting(name):
    print('''\n Dear {},
        Wishing you a very Happy Birthday! On behalf of your Birthday
        and the Upcomming Veterans Season, We offer you a gift
        '''.format(name))

def Independence_greeting(name):
    print('''\n Dear {},
        Wishing you a very Happy Birthday! On behalf of your Birthday
        and the Upcomming Independence Season, We offer you a gift
        '''.format(name))
    
def birthday_greeting(name):
    print('''\n Dear {},
        Wishing you a very Happy Birthday! On behalf of your Birthday,
        We offer you a gift
        '''.format(name))

    
christmas_voucher = 150
veterans_voucher = 100
Independence_voucher = 50
birtnday_voucher = 100


list1 = list(emp_details.keys())
list2 = list(emp_details.values())
#print(list1)

list3 = []
for i in list2:
    a=i.split('-')
    b= int(a[0])
    list3.append(b)
#print(list3)

print("-------------------------------Greetings-------------------------------")

for j in range(0,len(list3)):
    if list3[j] == 12:
        voucher = christmas_voucher+birtnday_voucher
        christmas_greeting(list1[j])
        print("%10s %18s %18s"%("Voucher(In'$') =","Christmas_Voucher(In'$') +","Birthday_Voucher(In'$')"))
        print("%10d %18d %25d\n"%(voucher,christmas_voucher,birtnday_voucher))
        print("-------------------------------Greetings-------------------------------")
    elif list3[j] == 11:
        voucher = veterans_voucher+birtnday_voucher
        veterans_greeting(list1[j]) 
        print("%10s %18s %18s"%("Voucher(In'$') =","Veterans_Voucher(In'$') +","Birthday_Voucher(In'$')"))
        print("%10d %18d %25d\n"%(voucher,veterans_voucher,birtnday_voucher))
        print("-------------------------------Greetings-------------------------------")
    elif list3[j] == 7:
        voucher = Independence_voucher+birtnday_voucher
        Independence_greeting(list1[j])
        print("%10s %18s %18s"%("Voucher(In'$') =","Independence_Voucher(In'$') +" , "Birthday_Voucher(In'$')"))
        print("%10d %18d %25d\n"%(voucher ,Independence_voucher , birtnday_voucher))
        print("-------------------------------Greetings-------------------------------")
    else:
        voucher = birtnday_voucher
        birthday_greeting(list1[j])
        print("%10s"%("Birthday_Voucher(In'$')"))
        print("%10d\n"%(voucher))
        print("-------------------------------Greetings-------------------------------")


# In[ ]:




