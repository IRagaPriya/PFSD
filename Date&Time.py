#date and time
import time;
import datetime;
print(time.time())
print(time.asctime())
print(time.asctime(time.localtime(time.time())))
datetime_object=datetime.datetime.now()
print(datetime_object)
print("Year:",datetime_object.year)
print("Month:",datetime_object.month)
print("Hour:",datetime_object.hour)
print("Minute:",datetime_object.minute)
print("Day:",datetime_object.day)

#calendar
import calendar;
s=calendar.prcal(2022)
print(s)

#classes in python-ex for namespaces
count=5                       #global variable
def some_method():
 global count                 #global keyword to call global variable
 count=count+1
 local=10                     #local variable
 print(count)
 print(local)
some_method()


#declaring class and objects
class FruitBasket:
    "deepak"
    #constructor
    def __init__ (self,fruits,total):
        self.fruit_list=fruits
        self.total=total
    def show_total(self):
        print("total",self.total)
    def show_basket(self):
        print("cart",self.fruit_list)
    def show_bill(self):
        self.show_total()
        self.show_basket()
        print(FruitBasket.__doc__)
my_basket=FruitBasket(["apple","mango","orange"],50)
my_basket.show_bill()


#constructor

class KLU:
    def __init__(self,name,id):      #parameterized constructor
        self.id=id
        self.name=name
    def display(self):
        print("ID:%d\n Names:%s"%(self.id,self.name))

obg1=KLU("Deepak",101)
obg2= KLU("Ramya", 101)
obg1.display()
obg2.display()