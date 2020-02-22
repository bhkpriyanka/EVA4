**TARGET:**  
1.Improve model efficiency further by adding batch normalizaton(adds some more params).  
2.Try reducing #parameters. 

**RESULTS:**  
*#params:* 9596  
*best train acc:*  99.40  
*best test acc:*  99.32

**ANALYSIS:**    
1.Seeing a good jump in train & test accuracies.
2.Model overfits.    
  
   Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 12, 26, 26]             108
       BatchNorm2d-2           [-1, 12, 26, 26]              24
              ReLU-3           [-1, 12, 26, 26]               0
            Conv2d-4           [-1, 16, 24, 24]           1,728
       BatchNorm2d-5           [-1, 16, 24, 24]              32
              ReLU-6           [-1, 16, 24, 24]               0
            Conv2d-7           [-1, 10, 24, 24]             160
         MaxPool2d-8           [-1, 10, 12, 12]               0
            Conv2d-9           [-1, 12, 10, 10]           1,080
      BatchNorm2d-10           [-1, 12, 10, 10]              24
             ReLU-11           [-1, 12, 10, 10]               0
           Conv2d-12             [-1, 16, 8, 8]           1,728
      BatchNorm2d-13             [-1, 16, 8, 8]              32
             ReLU-14             [-1, 16, 8, 8]               0
           Conv2d-15             [-1, 30, 6, 6]           4,320
      BatchNorm2d-16             [-1, 30, 6, 6]              60
             ReLU-17             [-1, 30, 6, 6]               0
        AvgPool2d-18             [-1, 30, 1, 1]               0
           Conv2d-19             [-1, 10, 1, 1]             300
================================================================  
Total params: 9,596
Trainable params: 9,596
Non-trainable params: 0  

**LOGS**  
  0%|          | 0/938 [00:00<?, ?it/s]EPOCH: 1
Loss=0.06499607861042023 Batch_id=937 Accuracy=91.37: 100%|██████████| 938/938 [00:14<00:00, 62.60it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0851, Accuracy: 9764/10000 (97.64%)

EPOCH: 2
Loss=0.048287346959114075 Batch_id=937 Accuracy=98.21: 100%|██████████| 938/938 [00:14<00:00, 63.89it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0540, Accuracy: 9843/10000 (98.43%)

EPOCH: 3
Loss=0.04243403673171997 Batch_id=937 Accuracy=98.61: 100%|██████████| 938/938 [00:14<00:00, 62.82it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0378, Accuracy: 9886/10000 (98.86%)

EPOCH: 4
Loss=0.012408420443534851 Batch_id=937 Accuracy=98.78: 100%|██████████| 938/938 [00:14<00:00, 63.83it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0345, Accuracy: 9891/10000 (98.91%)

EPOCH: 5
Loss=0.010346934199333191 Batch_id=937 Accuracy=98.89: 100%|██████████| 938/938 [00:15<00:00, 62.23it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0315, Accuracy: 9910/10000 (99.10%)

EPOCH: 6
Loss=0.034191206097602844 Batch_id=937 Accuracy=99.03: 100%|██████████| 938/938 [00:14<00:00, 64.02it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0295, Accuracy: 9913/10000 (99.13%)

EPOCH: 7
Loss=0.005022421479225159 Batch_id=937 Accuracy=99.08: 100%|██████████| 938/938 [00:15<00:00, 61.08it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0281, Accuracy: 9913/10000 (99.13%)

EPOCH: 8
Loss=0.04757896810770035 Batch_id=937 Accuracy=99.18: 100%|██████████| 938/938 [00:14<00:00, 62.61it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0301, Accuracy: 9902/10000 (99.02%)

EPOCH: 9
Loss=0.008706748485565186 Batch_id=937 Accuracy=99.21: 100%|██████████| 938/938 [00:14<00:00, 69.27it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0330, Accuracy: 9896/10000 (98.96%)

EPOCH: 10
Loss=0.07262811064720154 Batch_id=937 Accuracy=99.28: 100%|██████████| 938/938 [00:15<00:00, 68.24it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0249, Accuracy: 9931/10000 (99.31%)

EPOCH: 11
Loss=0.003836497664451599 Batch_id=937 Accuracy=99.30: 100%|██████████| 938/938 [00:15<00:00, 61.63it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0255, Accuracy: 9926/10000 (99.26%)

EPOCH: 12
Loss=0.002506732940673828 Batch_id=937 Accuracy=99.36: 100%|██████████| 938/938 [00:15<00:00, 60.09it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0291, Accuracy: 9908/10000 (99.08%)

EPOCH: 13
Loss=0.002976462244987488 Batch_id=937 Accuracy=99.38: 100%|██████████| 938/938 [00:15<00:00, 62.06it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0238, Accuracy: 9924/10000 (99.24%)

EPOCH: 14
Loss=0.0004749596118927002 Batch_id=937 Accuracy=99.40: 100%|██████████| 938/938 [00:15<00:00, 60.12it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0246, Accuracy: 9921/10000 (99.21%)

EPOCH: 15
Loss=0.017247065901756287 Batch_id=937 Accuracy=99.40: 100%|██████████| 938/938 [00:15<00:00, 60.95it/s]

Test set: Average loss: 0.0236, Accuracy: 9932/10000 (99.32%)
