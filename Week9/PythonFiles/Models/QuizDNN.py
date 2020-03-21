from all_imports import *

class Net(nn.Module):
    def __init__(self,dropout_value=0.0):
        super(Net, self).__init__()
        # Input Block(CB1)
        self.convblock1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=64, kernel_size=(3, 3), padding=1,bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(0.1)
        ) # output_size = 32

        # CB2
        self.convblock2 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(3, 3), padding=1 ,bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(0.15)
        ) # output_size = 32

         # CB3
        self.convblock3 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(3, 3), padding=1 ,bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(0.15)
        ) # output_size = 32
      
        # TRANSITION BLOCK 1
        #self.conv1x1_1 = nn.Sequential(
           # nn.Conv2d(in_channels=128, out_channels=16, kernel_size=(1, 1), padding=0, bias=False),
        #) # output_size = 32
        self.pool1 = nn.MaxPool2d(2, 2) # output_size = 16

        # CB4
        self.convblock4 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(3, 3), padding=1,bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(0.1)
        ) # output_size = 16

        # CB5
        self.convblock5 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(3, 3), padding=1 ,bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(0.15)
        ) # output_size = 16

         # CB6
        self.convblock6 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(3, 3), padding=1 ,bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(0.15)
        ) # output_size = 16
      
        # TRANSITION BLOCK 1
        #self.conv1x1_1 = nn.Sequential(
           # nn.Conv2d(in_channels=128, out_channels=16, kernel_size=(1, 1), padding=0, bias=False),
        #) # output_size = 32
        self.pool2 = nn.MaxPool2d(2, 2) # output_size = 8

         # CB7
        self.convblock7 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(3, 3), padding=1,bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(0.1)
        ) # output_size = 32

        # CB8
        self.convblock8 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(3, 3), padding=1 ,bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(0.15)
        ) # output_size = 32

         # CB9
        self.convblock9 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(3, 3), padding=1 ,bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(0.15)
        ) # output_size = 32
      
                      
        
        # OUTPUT BLOCK
        self.gap = nn.Sequential(
            nn.AvgPool2d(kernel_size=8)
        ) # output_size = 1

        self.fcn = nn.Sequential(
            #nn.Linear(in_features=64, out_features=10, bias=False)
            nn.Conv2d(in_channels=64, out_channels=10, kernel_size=(1, 1), padding=0, bias=False),
            
        ) 

        
    def forward(self, x):
        x1=self.convblock1(x)              #32x32x3-->32x32x64
        x2 = self.convblock2(x1)          #32x32x64-->32x32x64
        x3 = self.convblock3(x1+x2)    #32x32x64-->32x32x64
        x4=self.pool1(x1+x2+x3)          #32x32x64-->16x16x64
        x5 = self.convblock4(x4)            #16x16x64-->16x16x64
        x6 = self.convblock5(x4+x5)       #16x16x64-->16x16x64
        x7 = self.convblock6(x4+x5+x6)  #16x16x64-->16x16x64
        x8 = self.pool2(x5+x6+x7)             #16x16x64-->8x8x64
        x9 = self.convblock7(x8)               #8x8x64-->8x8x64
        x10=self.convblock8(x8+x9)         #8x8x64-->8x8x64
        x11=self.convblock9(x8+x9+x10)  #8x8x64-->8x8x64
                
        x12 = self.gap(x11) #64 

        x13 = self.fcn(x12)  #10

        x = x13.view(-1, 10)
        return F.log_softmax(x, dim=-1)

		

		
def get_model_instance(dp):
	return Net(dropout_value = dp)
