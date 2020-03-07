        Layer (type)               Output Shape         Param #

            Conv2d-1           [-1, 32, 32, 32]             864
       BatchNorm2d-2           [-1, 32, 32, 32]              64
              ReLU-3           [-1, 32, 32, 32]               0
            Conv2d-4           [-1, 64, 32, 32]          18,432
       BatchNorm2d-5           [-1, 64, 32, 32]             128
              ReLU-6           [-1, 64, 32, 32]               0
            Conv2d-7           [-1, 64, 32, 32]             576
            Conv2d-8          [-1, 128, 32, 32]           8,320
       BatchNorm2d-9          [-1, 128, 32, 32]             256
             ReLU-10          [-1, 128, 32, 32]               0
           Conv2d-11           [-1, 16, 32, 32]           2,048
        MaxPool2d-12           [-1, 16, 16, 16]               0
           Conv2d-13           [-1, 32, 16, 16]           4,608
      BatchNorm2d-14           [-1, 32, 16, 16]              64
             ReLU-15           [-1, 32, 16, 16]               0
           Conv2d-16           [-1, 64, 16, 16]          18,432
      BatchNorm2d-17           [-1, 64, 16, 16]             128
             ReLU-18           [-1, 64, 16, 16]               0
           Conv2d-19           [-1, 64, 16, 16]             576
           Conv2d-20          [-1, 128, 16, 16]           8,320
      BatchNorm2d-21          [-1, 128, 16, 16]             256
             ReLU-22          [-1, 128, 16, 16]               0
           Conv2d-23           [-1, 16, 16, 16]           2,048
        MaxPool2d-24             [-1, 16, 8, 8]               0
           Conv2d-25             [-1, 32, 8, 8]           4,608
      BatchNorm2d-26             [-1, 32, 8, 8]              64
             ReLU-27             [-1, 32, 8, 8]               0
           Conv2d-28             [-1, 64, 8, 8]          18,432
      BatchNorm2d-29             [-1, 64, 8, 8]             128
             ReLU-30             [-1, 64, 8, 8]               0
           Conv2d-31            [-1, 128, 8, 8]          73,728
      BatchNorm2d-32            [-1, 128, 8, 8]             256
             ReLU-33            [-1, 128, 8, 8]               0
           Conv2d-34             [-1, 32, 8, 8]           4,096
        MaxPool2d-35             [-1, 32, 4, 4]               0
           Conv2d-36             [-1, 64, 4, 4]          18,432
      BatchNorm2d-37             [-1, 64, 4, 4]             128
             ReLU-38             [-1, 64, 4, 4]               0
        AvgPool2d-39             [-1, 64, 1, 1]               0
           Conv2d-40             [-1, 10, 1, 1]             640
Total params: 185,632
Trainable params: 185,632
Non-trainable params: 0  

  0%|          | 0/782 [00:00<?, ?it/s]EPOCH: 1
Loss=1.1849955320358276 Batch_id=781 Accuracy=46.98: 100%|██████████| 782/782 [00:17<00:00, 43.45it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 1.2889, Accuracy: 5289/10000 (52.89%)


EPOCH: 2
Loss=1.0963808298110962 Batch_id=781 Accuracy=64.09: 100%|██████████| 782/782 [00:17<00:00, 43.58it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 1.0879, Accuracy: 6162/10000 (61.62%)


EPOCH: 3
Loss=1.2025140523910522 Batch_id=781 Accuracy=70.83: 100%|██████████| 782/782 [00:18<00:00, 43.22it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.8337, Accuracy: 7060/10000 (70.60%)


EPOCH: 4
Loss=0.8731542825698853 Batch_id=781 Accuracy=75.02: 100%|██████████| 782/782 [00:18<00:00, 43.08it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.9346, Accuracy: 6890/10000 (68.90%)


EPOCH: 5
Loss=0.5995721817016602 Batch_id=781 Accuracy=77.51: 100%|██████████| 782/782 [00:18<00:00, 43.44it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.7185, Accuracy: 7609/10000 (76.09%)


EPOCH: 6
Loss=0.404413104057312 Batch_id=781 Accuracy=79.98: 100%|██████████| 782/782 [00:18<00:00, 42.61it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6336, Accuracy: 7842/10000 (78.42%)


EPOCH: 7
Loss=0.4452131390571594 Batch_id=781 Accuracy=81.92: 100%|██████████| 782/782 [00:19<00:00, 44.01it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6158, Accuracy: 7888/10000 (78.88%)


EPOCH: 8
Loss=0.8388016819953918 Batch_id=781 Accuracy=83.32: 100%|██████████| 782/782 [00:19<00:00, 40.47it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6580, Accuracy: 7812/10000 (78.12%)


EPOCH: 9
Loss=0.47719094157218933 Batch_id=781 Accuracy=84.59: 100%|██████████| 782/782 [00:19<00:00, 40.86it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6113, Accuracy: 8000/10000 (80.00%)


EPOCH: 10
Loss=1.6173546314239502 Batch_id=781 Accuracy=85.81: 100%|██████████| 782/782 [00:19<00:00, 41.08it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.7731, Accuracy: 7571/10000 (75.71%)


EPOCH: 11
Loss=0.5175689458847046 Batch_id=781 Accuracy=86.87: 100%|██████████| 782/782 [00:19<00:00, 40.46it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.5834, Accuracy: 8050/10000 (80.50%)


EPOCH: 12
Loss=0.6328138113021851 Batch_id=781 Accuracy=87.94: 100%|██████████| 782/782 [00:19<00:00, 40.93it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6742, Accuracy: 7906/10000 (79.06%)


EPOCH: 13
Loss=0.4218151271343231 Batch_id=781 Accuracy=88.60: 100%|██████████| 782/782 [00:18<00:00, 41.30it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6579, Accuracy: 7984/10000 (79.84%)


EPOCH: 14
Loss=0.3095846474170685 Batch_id=781 Accuracy=89.58: 100%|██████████| 782/782 [00:19<00:00, 40.67it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6093, Accuracy: 8079/10000 (80.79%)


EPOCH: 15
Loss=0.8277952075004578 Batch_id=781 Accuracy=90.32: 100%|██████████| 782/782 [00:18<00:00, 41.56it/s]

Test set: Average loss: 0.6978, Accuracy: 7948/10000 (79.48%)


