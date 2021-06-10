class cartridge:
    def set_InkColor(self,ink):
        self.ink=ink
    def set_MaxPages(self,page):
        self.maxpage=page
    def set_length(self,length):
        self.length=length
    def set_price(self,price):
        self.price=price
    def getInkColor(self):
        if self.ink!=None:
            return self.ink
    def getMaxPages(self):
        if self.maxpage!= None:
            return self.maxpage
    def getLength(self):
        if self.length!=None:
            return self.length
    def getPrice(self):
        if self.price!=None:
            return self.price
