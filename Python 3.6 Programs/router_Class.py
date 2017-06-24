class MyRouter(object):
   '''This is a class that describes a router'''
   def __init__(self,routername,model,serialno,ios):
         self.routername=routername
         self.model=model
         self.serialno=serialno
         self.ios=ios
   def print_router(self,manuf_date):
         print("THe router name is:",self.routername)
         print("The router model is:",self.model)
         print("The serial numberis:",self.serialno)
         print("The IOS version is:",self.ios)
         print("The model and date combined",self.model+manuf_date)


router1=MyRouter("R1","2600","123456","12.4")

router2=MyRouter("R2","2700","989762","11.1")

router2.print_router("12/4/2017")

router1.print_router("11/2/2017")

setattr(router1,"ios","10.5")

print(router1.ios)

delattr(router1,"ios")

print(hasattr(router1,"ios"))



