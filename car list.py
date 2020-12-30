#A project done by Dark Murderer
#ig = @darkmurderer_ggwp
#telegram = @darkmurderer_ggwp
#====================================================================

class car:
    def __init__(self,breaks,wheels,roof):
        self.breaks = breaks
        self.wheels = wheels
        self.roof = roof

#====================================================================

class first_class(car):
    def __init__(self,breaks,wheels,roof):
        super().__init__(breaks, wheels, roof)
        self.Accelerator = "type-1"
        self.name = "1"
    

    def printdata1(self):
        print("==============")
        print("name: ",self.name)
        print("breaks: ",self.breaks)
        print("wheels: ",self.wheels)
        print("roof: ",self.roof)
        print("Accelerator: ",self.Accelerator)
        print("==============")

#====================================================================

class second_class(car):
    def __init__(self,breaks,wheels,roof):
        super().__init__(breaks, wheels, roof)
        self.name = "2"
        self.Accelerator = "type-2"
        self.Nitro = 50

    def printdata2(self):
        print("name: ",self.name)
        print("breaks: ",self.breaks)
        print("wheels: ",self.wheels)
        print("roof: ",self.roof)
        print("Accelerator: ",self.Accelerator)
        print("Nitro: ",self.Nitro)
        print("==============")

#====================================================================

class third_class(car):
    def __init__(self,breaks,wheels,roof):
        super().__init__(breaks, wheels, roof)
        self.name = "3"
        self.Accelerator = "type-3"
        self.Nitro = 100
        self.Sunroof = True

    def printdata3(self):
        print("name: ",self.name)
        print("breaks: ",self.breaks)
        print("wheels: ",self.wheels)
        print("roof: ",self.roof)
        print("Accelerator: ",self.Accelerator)
        print("Nitro: ",self.Nitro)
        print("sunroof: ",self.Sunroof)
        print("==============")

#====================================================================

c1 = first_class(True,True,True)
c2 = second_class(True,True,True)
c3 = third_class(True,True,True)

#====================================================================

print("cars list with info:")
c1.printdata1()
c2.printdata2()
c3.printdata3()

#====================================================================