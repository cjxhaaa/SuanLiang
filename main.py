from data_getter import DataGetter

D = DataGetter()
D_name = D.get_name()
D_number = D.get_number()

class DuichengWindow():
    def __init__(self):
        self.L1_name = D_name[0]
        self.L2_name = D_name[1]
        self.L3_name = D_name[2]
        self.L4_name = D_name[3]
        self.L5_name = D_name[4]
        self.L = D_number[0]
        self.W = D_number[1]
        self.G = D_number[2]
        self.num1 = D_number[3]
        self.num2 = D_number[4]
        self.L_a = D_number[5]
        self.L_b = self.L-2*self.G-self.L_a
        self.W_a1 = (self.W-2*self.G)//self.num1
        self.W_a2 = (self.W-2*self.G)//self.num2

    def SumWindow(self):

        if self.num2 == 1:
            L1 = 2 * ((self.L - self.G * 2) + (self.W - self.G * 2))
            print('窗框{}:{}'.format(self.L1_name,L1))
            L2 = self.num1 * (2 * (self.L_a + self.W_a1))
            print('窗扇{}:{}'.format(self.L2_name,L2))
            L3 = L2 + 2 * ((self.W - 2 * self.G) + self.L_b)
            print('压线{}:{}'.format(self.L3_name,L3))
            L4 = self.W-2*self.G+self.L_a*(self.num1-1)
            print('中挺{}:{}'.format(self.L4_name,L4))
        elif self.num2 > 1:
            L1 = 2 * ((self.L - self.G * 2)*self.num2 + (self.W - self.G * 2))
            print('窗框{}:{}'.format(self.L1_name,L1))
            L2 = self.num1 * (2 * (self.L_a + self.W_a1))
            print('窗扇{}:{}'.format(self.L2_name,L2))
            L3 = L2 + 2 * ((self.W - 2 * self.G) + self.L_b*self.num2)
            print('压线{}:{}'.format(self.L3_name,L3))
            L4 = self.W-2*self.G+self.L_a*(self.num1-self.num2)
            print('中挺{}:{}'.format(self.L4_name,L4))
            L5 = (self.L-2*self.G)*(self.num2-1)
            print('加强型中挺{}:{}'.format(self.L5_name,L5))






#
#
# if __name__ == '__main__':
#     # L = 1800
#     # W = 1200
#     # G = 20
#     # num1 = 2
#     # num2 = 1
#     # L_a = 830
#     L = 1800
#     W = 2400
#     G = 20
#     num1 = 6
#     num2 = 3
#     L_a = 830
#     win = DuichengWindow(L,W,G,num1,num2,L_a)
#     win.SumWindow()



