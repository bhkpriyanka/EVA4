**TARGET:**  
Tweak learning rate & create a scheduler with appropriate gamma value.

**RESULTS:**  
*#params:*  9596  
*best train acc:* 99.23  
*best test acc:*  99.55

**ANALYSIS:**  
1.Varied learning rates between 0.01-0.06 & gamma bettwen 0.1-0.9 and got good results for lr=0.04 & gamma=0.1.
2.Achieved consistently high test and train accuracies in last few epocs after suitable lr scheduling.  
3.Model continues to underfit but test accuracy is higher than train.  

**CODE**  
from torch.optim.lr_scheduler import StepLR  
model =  Net().to(device)  
optimizer = optim.SGD(model.parameters(), lr=0.04, momentum=0.9)  
scheduler = StepLR(optimizer, step_size=6, gamma=0.1)  
EPOCHS = 15  


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
  
  
**LOGS**  
  0%|          | 0/938 [00:00<?, ?it/s]EPOCH: 1
Loss=0.0292145237326622 Batch_id=937 Accuracy=93.99: 100%|██████████| 938/938 [00:16<00:00, 57.17it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0654, Accuracy: 9800/10000 (98.00%)

EPOCH: 2
Loss=0.04645681381225586 Batch_id=937 Accuracy=98.06: 100%|██████████| 938/938 [00:16<00:00, 57.43it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0354, Accuracy: 9894/10000 (98.94%)

EPOCH: 3
Loss=0.0197087824344635 Batch_id=937 Accuracy=98.48: 100%|██████████| 938/938 [00:16<00:00, 57.71it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0280, Accuracy: 9915/10000 (99.15%)

EPOCH: 4
Loss=0.007489502429962158 Batch_id=937 Accuracy=98.73: 100%|██████████| 938/938 [00:16<00:00, 58.39it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0409, Accuracy: 9862/10000 (98.62%)

EPOCH: 5
Loss=0.017738208174705505 Batch_id=937 Accuracy=98.76: 100%|██████████| 938/938 [00:16<00:00, 58.57it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0235, Accuracy: 9928/10000 (99.28%)

EPOCH: 6
Loss=0.02108222246170044 Batch_id=937 Accuracy=98.84: 100%|██████████| 938/938 [00:15<00:00, 58.69it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0272, Accuracy: 9914/10000 (99.14%)

EPOCH: 7
Loss=0.011117696762084961 Batch_id=937 Accuracy=98.97: 100%|██████████| 938/938 [00:15<00:00, 59.28it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0216, Accuracy: 9936/10000 (99.36%)

EPOCH: 8
Loss=0.10687536746263504 Batch_id=937 Accuracy=99.03: 100%|██████████| 938/938 [00:16<00:00, 56.17it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0254, Accuracy: 9925/10000 (99.25%)

EPOCH: 9
Loss=0.007371127605438232 Batch_id=937 Accuracy=99.03: 100%|██████████| 938/938 [00:15<00:00, 58.85it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0256, Accuracy: 9917/10000 (99.17%)

EPOCH: 10
Loss=0.14045017957687378 Batch_id=937 Accuracy=99.04: 100%|██████████| 938/938 [00:15<00:00, 59.53it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0200, Accuracy: 9939/10000 (99.39%)

EPOCH: 11
Loss=0.0075303614139556885 Batch_id=937 Accuracy=99.16: 100%|██████████| 938/938 [00:16<00:00, 56.90it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0208, Accuracy: 9936/10000 (99.36%)

EPOCH: 12
Loss=0.03480112552642822 Batch_id=937 Accuracy=99.11: 100%|██████████| 938/938 [00:15<00:00, 59.15it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0208, Accuracy: 9932/10000 (99.32%)

EPOCH: 13
Loss=0.0008060634136199951 Batch_id=937 Accuracy=99.16: 100%|██████████| 938/938 [00:16<00:00, 58.10it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0178, Accuracy: 9943/10000 (99.43%)

EPOCH: 14
Loss=0.0008375942707061768 Batch_id=937 Accuracy=99.19: 100%|██████████| 938/938 [00:15<00:00, 59.08it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0204, Accuracy: 9940/10000 (99.40%)

EPOCH: 15
Loss=0.009292632341384888 Batch_id=937 Accuracy=99.23: 100%|██████████| 938/938 [00:16<00:00, 56.64it/s]

Test set: Average loss: 0.0167, Accuracy: 9955/10000 (99.55%)
