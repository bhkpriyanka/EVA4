        Layer (type)               Output Shape         Param #

            Conv2d-1           [-1, 32, 32, 32]             864
       BatchNorm2d-2           [-1, 32, 32, 32]              64
              ReLU-3           [-1, 32, 32, 32]               0
            Conv2d-4           [-1, 64, 32, 32]          18,432
       BatchNorm2d-5           [-1, 64, 32, 32]             128
              ReLU-6           [-1, 64, 32, 32]               0
            Conv2d-7          [-1, 128, 32, 32]          73,728
       BatchNorm2d-8          [-1, 128, 32, 32]             256
              ReLU-9          [-1, 128, 32, 32]               0
           Conv2d-10           [-1, 16, 32, 32]           2,048
        MaxPool2d-11           [-1, 16, 16, 16]               0
           Conv2d-12           [-1, 32, 16, 16]           4,608
      BatchNorm2d-13           [-1, 32, 16, 16]              64
             ReLU-14           [-1, 32, 16, 16]               0
           Conv2d-15           [-1, 64, 16, 16]          18,432
      BatchNorm2d-16           [-1, 64, 16, 16]             128
             ReLU-17           [-1, 64, 16, 16]               0
           Conv2d-18          [-1, 128, 16, 16]          73,728
      BatchNorm2d-19          [-1, 128, 16, 16]             256
             ReLU-20          [-1, 128, 16, 16]               0
           Conv2d-21           [-1, 16, 16, 16]           2,048
        MaxPool2d-22             [-1, 16, 8, 8]               0
           Conv2d-23             [-1, 32, 8, 8]           4,608
      BatchNorm2d-24             [-1, 32, 8, 8]              64
             ReLU-25             [-1, 32, 8, 8]               0
           Conv2d-26             [-1, 64, 8, 8]          18,432
      BatchNorm2d-27             [-1, 64, 8, 8]             128
             ReLU-28             [-1, 64, 8, 8]               0
           Conv2d-29            [-1, 128, 8, 8]          73,728
      BatchNorm2d-30            [-1, 128, 8, 8]             256
             ReLU-31            [-1, 128, 8, 8]               0
           Conv2d-32             [-1, 32, 8, 8]           4,096
        MaxPool2d-33             [-1, 32, 4, 4]               0
           Conv2d-34             [-1, 64, 4, 4]          18,432
      BatchNorm2d-35             [-1, 64, 4, 4]             128
             ReLU-36             [-1, 64, 4, 4]               0
        AvgPool2d-37             [-1, 64, 1, 1]               0
           Conv2d-38             [-1, 10, 1, 1]             640

Total params: 315,296
Trainable params: 315,296
Non-trainable params: 0

  
  0%|          | 0/782 [00:00<?, ?it/s]EPOCH: 1
Loss=1.0726819038391113 Batch_id=781 Accuracy=43.41: 100%|██████████| 782/782 [00:20<00:00, 38.51it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 1.2584, Accuracy: 5468/10000 (54.68%)


EPOCH: 2
Loss=1.2036470174789429 Batch_id=781 Accuracy=62.17: 100%|██████████| 782/782 [00:20<00:00, 38.97it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 1.0305, Accuracy: 6345/10000 (63.45%)


EPOCH: 3
Loss=0.7386047840118408 Batch_id=781 Accuracy=70.20: 100%|██████████| 782/782 [00:19<00:00, 39.30it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.8538, Accuracy: 7037/10000 (70.37%)


EPOCH: 4
Loss=0.41830167174339294 Batch_id=781 Accuracy=75.18: 100%|██████████| 782/782 [00:19<00:00, 39.18it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.7679, Accuracy: 7385/10000 (73.85%)


EPOCH: 5
Loss=0.44068247079849243 Batch_id=781 Accuracy=77.80: 100%|██████████| 782/782 [00:20<00:00, 38.56it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.7357, Accuracy: 7471/10000 (74.71%)


EPOCH: 6
Loss=1.0068883895874023 Batch_id=781 Accuracy=80.25: 100%|██████████| 782/782 [00:19<00:00, 39.21it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.7208, Accuracy: 7618/10000 (76.18%)


EPOCH: 7
Loss=0.8716267347335815 Batch_id=781 Accuracy=82.02: 100%|██████████| 782/782 [00:20<00:00, 38.83it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6735, Accuracy: 7742/10000 (77.42%)


EPOCH: 8
Loss=0.37572893500328064 Batch_id=781 Accuracy=83.74: 100%|██████████| 782/782 [00:20<00:00, 40.55it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.7314, Accuracy: 7620/10000 (76.20%)


EPOCH: 9
Loss=0.395250141620636 Batch_id=781 Accuracy=84.91: 100%|██████████| 782/782 [00:20<00:00, 41.85it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6288, Accuracy: 7959/10000 (79.59%)


EPOCH: 10
Loss=0.3686211407184601 Batch_id=781 Accuracy=86.15: 100%|██████████| 782/782 [00:19<00:00, 39.18it/s]

Test set: Average loss: 0.6063, Accuracy: 8063/10000 (80.63%)

