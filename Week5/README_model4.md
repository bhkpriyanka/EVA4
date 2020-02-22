TARGET:
Reduce overfitting by adding dropout & applying suitable data augmentation transforms on training data(rotation in this case).

RESULTS:
#params: 9596
best train acc: 99.16
best test acc: 99.39

ANALYSIS:
1.Model starts to underfit and getting harder to learn from.
2.However test accuracies improved and are more than corresponding train accuracies in most of the epochs.  

Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 12, 26, 26]             108
       BatchNorm2d-2           [-1, 12, 26, 26]              24
              ReLU-3           [-1, 12, 26, 26]               0
           Dropout-4           [-1, 12, 26, 26]               0
            Conv2d-5           [-1, 16, 24, 24]           1,728
       BatchNorm2d-6           [-1, 16, 24, 24]              32
              ReLU-7           [-1, 16, 24, 24]               0
           Dropout-8           [-1, 16, 24, 24]               0
            Conv2d-9           [-1, 10, 24, 24]             160
        MaxPool2d-10           [-1, 10, 12, 12]               0
           Conv2d-11           [-1, 12, 10, 10]           1,080
      BatchNorm2d-12           [-1, 12, 10, 10]              24
             ReLU-13           [-1, 12, 10, 10]               0
          Dropout-14           [-1, 12, 10, 10]               0
           Conv2d-15             [-1, 16, 8, 8]           1,728
      BatchNorm2d-16             [-1, 16, 8, 8]              32
             ReLU-17             [-1, 16, 8, 8]               0
          Dropout-18             [-1, 16, 8, 8]               0
           Conv2d-19             [-1, 30, 6, 6]           4,320
      BatchNorm2d-20             [-1, 30, 6, 6]              60
             ReLU-21             [-1, 30, 6, 6]               0
          Dropout-22             [-1, 30, 6, 6]               0
        AvgPool2d-23             [-1, 30, 1, 1]               0
           Conv2d-24             [-1, 10, 1, 1]             300
================================================================  
Total params: 9,596
Trainable params: 9,596
Non-trainable params: 0  

LOGS:  

  0%|          | 0/938 [00:00<?, ?it/s]EPOCH: 1
Loss=0.09600294381380081 Batch_id=937 Accuracy=90.36: 100%|██████████| 938/938 [00:15<00:00, 59.56it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0677, Accuracy: 9811/10000 (98.11%)

EPOCH: 2
Loss=0.04664812982082367 Batch_id=937 Accuracy=97.76: 100%|██████████| 938/938 [00:15<00:00, 71.14it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0526, Accuracy: 9852/10000 (98.52%)

EPOCH: 3
Loss=0.01513315737247467 Batch_id=937 Accuracy=98.22: 100%|██████████| 938/938 [00:15<00:00, 60.43it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0418, Accuracy: 9870/10000 (98.70%)

EPOCH: 4
Loss=0.007596716284751892 Batch_id=937 Accuracy=98.47: 100%|██████████| 938/938 [00:16<00:00, 58.06it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0347, Accuracy: 9885/10000 (98.85%)

EPOCH: 5
Loss=0.049171000719070435 Batch_id=937 Accuracy=98.59: 100%|██████████| 938/938 [00:15<00:00, 59.82it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0299, Accuracy: 9916/10000 (99.16%)

EPOCH: 6
Loss=0.025804445147514343 Batch_id=937 Accuracy=98.74: 100%|██████████| 938/938 [00:15<00:00, 60.35it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0288, Accuracy: 9909/10000 (99.09%)

EPOCH: 7
Loss=0.03239145874977112 Batch_id=937 Accuracy=98.84: 100%|██████████| 938/938 [00:15<00:00, 58.69it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0308, Accuracy: 9907/10000 (99.07%)

EPOCH: 8
Loss=0.07282637059688568 Batch_id=937 Accuracy=98.84: 100%|██████████| 938/938 [00:15<00:00, 59.37it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0249, Accuracy: 9924/10000 (99.24%)

EPOCH: 9
Loss=0.01158122718334198 Batch_id=937 Accuracy=98.89: 100%|██████████| 938/938 [00:15<00:00, 59.86it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0249, Accuracy: 9926/10000 (99.26%)

EPOCH: 10
Loss=0.13457418978214264 Batch_id=937 Accuracy=99.01: 100%|██████████| 938/938 [00:15<00:00, 59.34it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0237, Accuracy: 9929/10000 (99.29%)

EPOCH: 11
Loss=0.002543926239013672 Batch_id=937 Accuracy=99.02: 100%|██████████| 938/938 [00:16<00:00, 56.60it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0254, Accuracy: 9927/10000 (99.27%)

EPOCH: 12
Loss=0.02374233305454254 Batch_id=937 Accuracy=99.03: 100%|██████████| 938/938 [00:16<00:00, 57.54it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0269, Accuracy: 9915/10000 (99.15%)

EPOCH: 13
Loss=0.00107651948928833 Batch_id=937 Accuracy=99.08: 100%|██████████| 938/938 [00:16<00:00, 58.35it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0218, Accuracy: 9930/10000 (99.30%)

EPOCH: 14
Loss=0.0008146762847900391 Batch_id=937 Accuracy=99.16: 100%|██████████| 938/938 [00:16<00:00, 64.51it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0216, Accuracy: 9922/10000 (99.22%)

EPOCH: 15
Loss=0.05272011458873749 Batch_id=937 Accuracy=99.10: 100%|██████████| 938/938 [00:16<00:00, 55.50it/s]

Test set: Average loss: 0.0201, Accuracy: 9939/10000 (99.39%)
