**#PARAMS:** 19858(without biases)
**ACCURACY:** 99.43 in 15th epoch  
  
**MODEL:**   
        Layer (type)|             Output Shape   |            Param #

            Conv2d-1           [-1, 12, 28, 28]             108
       BatchNorm2d-2           [-1, 12, 28, 28]              24
         Dropout2d-3           [-1, 12, 28, 28]               0
            Conv2d-4           [-1, 16, 28, 28]           1,728
       BatchNorm2d-5           [-1, 16, 28, 28]              32
         Dropout2d-6           [-1, 16, 28, 28]               0
         MaxPool2d-7           [-1, 16, 14, 14]               0
            Conv2d-8           [-1, 24, 14, 14]           3,456
       BatchNorm2d-9           [-1, 24, 14, 14]              48
        Dropout2d-10           [-1, 24, 14, 14]               0
           Conv2d-11           [-1, 24, 14, 14]           5,184
      BatchNorm2d-12           [-1, 24, 14, 14]              48
        Dropout2d-13           [-1, 24, 14, 14]               0
        MaxPool2d-14             [-1, 24, 7, 7]               0
           Conv2d-15             [-1, 40, 5, 5]           8,640
      BatchNorm2d-16             [-1, 40, 5, 5]              80
        Dropout2d-17             [-1, 40, 5, 5]               0
           Conv2d-18             [-1, 10, 5, 5]             400  
           AdaptiveAvgPool3d-19             [-1, 10, 1, 1]               0
           Linear-20                   [-1, 10]             110

Total params: 19,858  
Trainable params: 19,858  
Non-trainable params: 0  


**LOGS**  
0%|          | 0/469 [00:00<?, ?it/s]EPOCH:  1
/usr/local/lib/python3.6/dist-packages/ipykernel_launcher.py:42: UserWarning: Implicit dimension choice for log_softmax has been deprecated. Change the call to include dim=X as an argument.
loss=0.1155146136879921 batch_id=468: 100%|██████████| 469/469 [00:13<00:00, 34.37it/s]
Train set: Average loss: 0.5799, Accuracy: 48787/60000 (81.31%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0867, Accuracy: 9755/10000 (97.55%)

EPOCH:  2
loss=0.05294984579086304 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 39.44it/s]
Train set: Average loss: 0.0935, Accuracy: 58386/60000 (97.31%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0492, Accuracy: 9858/10000 (98.58%)

EPOCH:  3
loss=0.02068663388490677 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 40.44it/s]
Train set: Average loss: 0.0637, Accuracy: 58896/60000 (98.16%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0389, Accuracy: 9875/10000 (98.75%)

EPOCH:  4
loss=0.034088101238012314 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 40.12it/s]
Train set: Average loss: 0.0508, Accuracy: 59093/60000 (98.49%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0302, Accuracy: 9900/10000 (99.00%)

EPOCH:  5
loss=0.10888117551803589 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 41.64it/s]
Train set: Average loss: 0.0432, Accuracy: 59196/60000 (98.66%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0279, Accuracy: 9905/10000 (99.05%)

EPOCH:  6
loss=0.03456881269812584 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 44.35it/s]
Train set: Average loss: 0.0380, Accuracy: 59298/60000 (98.83%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0252, Accuracy: 9910/10000 (99.10%)

EPOCH:  7
loss=0.023910662159323692 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 41.69it/s]
Train set: Average loss: 0.0339, Accuracy: 59361/60000 (98.94%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0258, Accuracy: 9911/10000 (99.11%)

EPOCH:  8
loss=0.08725183457136154 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 40.37it/s]
Train set: Average loss: 0.0306, Accuracy: 59428/60000 (99.05%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0218, Accuracy: 9926/10000 (99.26%)

EPOCH:  9
loss=0.007307961583137512 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 42.61it/s]

Train set: Average loss: 0.0276, Accuracy: 59476/60000 (99.13%)

  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0205, Accuracy: 9928/10000 (99.28%)

EPOCH:  10
loss=0.039330992847681046 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 41.08it/s]
Train set: Average loss: 0.0258, Accuracy: 59501/60000 (99.17%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0210, Accuracy: 9930/10000 (99.30%)

EPOCH:  11
loss=0.006857097148895264 batch_id=468: 100%|██████████| 469/469 [00:10<00:00, 42.93it/s]
Train set: Average loss: 0.0238, Accuracy: 59561/60000 (99.27%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0221, Accuracy: 9931/10000 (99.31%)

EPOCH:  12
loss=0.005914539098739624 batch_id=468: 100%|██████████| 469/469 [00:10<00:00, 42.73it/s]
Train set: Average loss: 0.0228, Accuracy: 59564/60000 (99.27%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0192, Accuracy: 9935/10000 (99.35%)

EPOCH:  13
loss=0.021734774112701416 batch_id=468: 100%|██████████| 469/469 [00:12<00:00, 38.80it/s]
Train set: Average loss: 0.0216, Accuracy: 59582/60000 (99.30%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0203, Accuracy: 9939/10000 (99.39%)

EPOCH:  14
loss=0.010089327581226826 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 39.22it/s]
Train set: Average loss: 0.0200, Accuracy: 59611/60000 (99.35%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0199, Accuracy: 9932/10000 (99.32%)

EPOCH:  15
loss=0.050252314656972885 batch_id=468: 100%|██████████| 469/469 [00:12<00:00, 37.75it/s]
Train set: Average loss: 0.0186, Accuracy: 59630/60000 (99.38%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0181, Accuracy: 9943/10000 (99.43%)

EPOCH:  16
loss=0.00678589940071106 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 39.62it/s]
Train set: Average loss: 0.0195, Accuracy: 59644/60000 (99.41%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0211, Accuracy: 9934/10000 (99.34%)

EPOCH:  17
loss=0.004988759756088257 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 43.85it/s]
Train set: Average loss: 0.0170, Accuracy: 59697/60000 (99.50%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0169, Accuracy: 9945/10000 (99.45%)

EPOCH:  18
loss=0.011392061598598957 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 40.16it/s]
Train set: Average loss: 0.0162, Accuracy: 59684/60000 (99.47%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0204, Accuracy: 9926/10000 (99.26%)

EPOCH:  19
loss=0.022226205095648766 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 41.43it/s]
Train set: Average loss: 0.0156, Accuracy: 59713/60000 (99.52%)


  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0177, Accuracy: 9942/10000 (99.42%)

EPOCH:  20
loss=0.0056805857457220554 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 40.85it/s]
Train set: Average loss: 0.0159, Accuracy: 59692/60000 (99.49%)



Test set: Average loss: 0.0170, Accuracy: 9948/10000 (99.48%)

