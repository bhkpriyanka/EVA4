from all_imports import *


class Net(nn.Module):
    def __init__(self,dropout_value=0.0):
        super(Net, self).__init__()
        # Input Block
        self.convblock1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=(3, 3), padding=1,bias=False),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.Dropout(0.1)
        ) # output_size = 32

        # CONVOLUTION BLOCK 1
        self.convblock2 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3), padding=1 ,bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(0.15)
        ) # output_size = 32
        '''self.convblock3 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(3, 3), padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU()
            #nn.Dropout(0.01)
        ) # output_size = 2'''
        self.dwsconv1 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(3, 3), padding=1,groups= 64, bias=False),
            nn.Conv2d(in_channels=64,out_channels=128,kernel_size=(1,1)),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Dropout(0.25)
        ) # output_size = 32

        # TRANSITION BLOCK 1
        self.conv1x1_1 = nn.Sequential(
            nn.Conv2d(in_channels=128, out_channels=16, kernel_size=(1, 1), padding=0, bias=False),
        ) # output_size = 32
        self.pool1 = nn.MaxPool2d(2, 2) # output_size = 16

         # CONVOLUTION BLOCK 2
        self.convblock4 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=(3, 3), padding=1, bias=False),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.Dropout(0.1)
        ) # output_size = 16
        self.convblock5 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3), padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(0.15)
        ) # output_size = 16
        '''self.convblock6 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(3, 3), padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU()
            #nn.Dropout(0.01)
        ) # output_size = 2'''
        self.dwsconv2 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=(3, 3), padding=1,groups= 64, bias=False),
            nn.Conv2d(in_channels=64,out_channels=128,kernel_size=(1,1)),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Dropout(0.25)
        ) # output_size = 16


        # TRANSITION BLOCK 2
        self.conv1x1_2 = nn.Sequential(
            nn.Conv2d(in_channels=128, out_channels=16, kernel_size=(1, 1), padding=0, bias=False),
        ) # output_size = 16
        self.pool2 = nn.MaxPool2d(2, 2) # output_size = 8

        # CONVOLUTION BLOCK 3
        self.convblock7 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=(3, 3), padding=1,dilation=1, bias=False),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.Dropout(0.1)
        ) # output_size = 8
        self.convblock8 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3), padding=2,dilation=2, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(0.15)
        ) # output_size = 8
        self.convblock9 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(3, 3), padding=2,dilation=2, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Dropout(0.25)
        ) # output_size = 8


        # TRANSITION BLOCK 3
        self.conv1x1_3 = nn.Sequential(
            nn.Conv2d(in_channels=128, out_channels=32, kernel_size=(1, 1), padding=0, bias=False),
        ) # output_size = 8
        self.pool3 = nn.MaxPool2d(2, 2) # output_size = 4

         # CONVOLUTION BLOCK 4
        self.convblock10 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=(3, 3), padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            #nn.Dropout(0.01)
        ) # output_size = 4

               
        
        # OUTPUT BLOCK
        self.gap = nn.Sequential(
            nn.AvgPool2d(kernel_size=4)
        ) # output_size = 1

        self.fcn = nn.Sequential(
            #nn.Linear(in_features=64, out_features=10, bias=False)
            nn.Conv2d(in_channels=64, out_channels=10, kernel_size=(1, 1), padding=0, bias=False),
            
        ) 

        
    def forward(self, x):
        x = self.convblock1(x)
        x = self.convblock2(x)
        #x = self.convblock3(x)
        x = self.dwsconv1(x)
        x = self.conv1x1_1(x)
        x = self.pool1(x)
        x = self.convblock4(x)
        x = self.convblock5(x)
        #x = self.convblock6(x)
        x = self.dwsconv2(x)
        x = self.conv1x1_2(x)
        x = self.pool2(x)
        x = self.convblock7(x)
        x = self.convblock8(x)
        x = self.convblock9(x)
        x = self.conv1x1_3(x)
        x = self.pool3(x)
        x = self.convblock10(x)
        #x = self.convblock11(x)
        
        x = self.gap(x)  

        x = self.fcn(x)

        x = x.view(-1, 10)
        return F.log_softmax(x, dim=-1)

		

		
def get_model_instance(dp):
	return Net(dropout_value = dp)
