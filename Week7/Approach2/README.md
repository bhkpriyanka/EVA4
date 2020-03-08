Group-Pratik Jain, BhKPriyanka, Siddharth Surange, Anjali Chimnani  
  
 **APPROACH2: CODE IS DIVIDED INTO MULTIPLE FUNCTIONAL BLOCKS AND ALL THESE FUNCTIONLITIES ARE IMPORTED INTO MAIN CODE FILE**  

The network has been modified as below:  
1)changed the code such that it uses GPU  
2)changed the architecture to C1C2C3C40 (basically 3 MPs)  
3)total RF must be more than 44  
4)one of the layers must use Depthwise Separable Convolution  
5)one of the layers must use Dilated Convolution  
6)use GAP (compulsory):- add FC after GAP to target #of classes (optional)
7)achieved >80%(84.12%) accuracy, as many epochs as you want. 
8)Total Params to be less than 1M(185,632).

