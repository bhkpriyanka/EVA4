**APPROACH 1: all functionality in Single notebook**  

Tried to achieve the targets of assignment step-by-step by improvising code as below:  

**Step1:**  
a)Edited the code to run on GPU  
b)built model with C1-C2-C3-C4-O Architecture with GAP (followed by FCN)  
c)made sure model has RF>44. 
<h4>Initial Receptive Field Calculation</h3>

![Image](https://github.com/bhkpriyanka/EVA4/blob/master/Week7/Approach1/ReceptiveField.png)

<hr> 

#epochs:10  
#parameters:315,296  
highest test accuracy: 80.63%(10th epoch)


**Step2:**  
Reduce #parameters with Depthwise seperable convolutions.  
#epochs:10  
#parameters:185,632  
highest test accuracy: 79.91%(9th epoch)

**Step3:**  
Added dilated convolutions to get better receptive fields with same no.of params  
#epochs:15  
#parameters:185,632  
test accuracy: 80.00% (9th epoch) & 80.79% (14th epoch)

