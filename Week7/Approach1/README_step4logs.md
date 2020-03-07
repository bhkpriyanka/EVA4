        Layer (type)               Output Shape         Param #

            Conv2d-1           [-1, 32, 32, 32]             864
       BatchNorm2d-2           [-1, 32, 32, 32]              64
              ReLU-3           [-1, 32, 32, 32]               0
           Dropout-4           [-1, 32, 32, 32]               0
            Conv2d-5           [-1, 64, 32, 32]          18,432
       BatchNorm2d-6           [-1, 64, 32, 32]             128
              ReLU-7           [-1, 64, 32, 32]               0
           Dropout-8           [-1, 64, 32, 32]               0
            Conv2d-9           [-1, 64, 32, 32]             576
           Conv2d-10          [-1, 128, 32, 32]           8,320
      BatchNorm2d-11          [-1, 128, 32, 32]             256
             ReLU-12          [-1, 128, 32, 32]               0
          Dropout-13          [-1, 128, 32, 32]               0
           Conv2d-14           [-1, 16, 32, 32]           2,048
        MaxPool2d-15           [-1, 16, 16, 16]               0
           Conv2d-16           [-1, 32, 16, 16]           4,608
      BatchNorm2d-17           [-1, 32, 16, 16]              64
             ReLU-18           [-1, 32, 16, 16]               0
          Dropout-19           [-1, 32, 16, 16]               0
           Conv2d-20           [-1, 64, 16, 16]          18,432
      BatchNorm2d-21           [-1, 64, 16, 16]             128
             ReLU-22           [-1, 64, 16, 16]               0
          Dropout-23           [-1, 64, 16, 16]               0
           Conv2d-24           [-1, 64, 16, 16]             576
           Conv2d-25          [-1, 128, 16, 16]           8,320
      BatchNorm2d-26          [-1, 128, 16, 16]             256
             ReLU-27          [-1, 128, 16, 16]               0
          Dropout-28          [-1, 128, 16, 16]               0
           Conv2d-29           [-1, 16, 16, 16]           2,048
        MaxPool2d-30             [-1, 16, 8, 8]               0
           Conv2d-31             [-1, 32, 8, 8]           4,608
      BatchNorm2d-32             [-1, 32, 8, 8]              64
             ReLU-33             [-1, 32, 8, 8]               0
          Dropout-34             [-1, 32, 8, 8]               0
           Conv2d-35             [-1, 64, 8, 8]          18,432
      BatchNorm2d-36             [-1, 64, 8, 8]             128
             ReLU-37             [-1, 64, 8, 8]               0
          Dropout-38             [-1, 64, 8, 8]               0
           Conv2d-39            [-1, 128, 8, 8]          73,728
      BatchNorm2d-40            [-1, 128, 8, 8]             256
             ReLU-41            [-1, 128, 8, 8]               0
          Dropout-42            [-1, 128, 8, 8]               0
           Conv2d-43             [-1, 32, 8, 8]           4,096
        MaxPool2d-44             [-1, 32, 4, 4]               0
           Conv2d-45             [-1, 64, 4, 4]          18,432
      BatchNorm2d-46             [-1, 64, 4, 4]             128
             ReLU-47             [-1, 64, 4, 4]               0
        AvgPool2d-48             [-1, 64, 1, 1]               0
           Conv2d-49             [-1, 10, 1, 1]             640

Total params: 185,632
Trainable params: 185,632
Non-trainable params: 0

  0%|          | 0/782 [00:00<?, ?it/s]EPOCH: 1
Loss=1.1861604452133179 Batch_id=781 Accuracy=42.10: 100%|██████████| 782/782 [00:27<00:00, 28.25it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 1.2919, Accuracy: 5198/10000 (51.98%)


EPOCH: 2
Loss=1.001328706741333 Batch_id=781 Accuracy=58.76: 100%|██████████| 782/782 [00:27<00:00, 28.30it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 1.1048, Accuracy: 6006/10000 (60.06%)


EPOCH: 3
Loss=1.0589420795440674 Batch_id=781 Accuracy=65.47: 100%|██████████| 782/782 [00:26<00:00, 29.07it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.9028, Accuracy: 6845/10000 (68.45%)


EPOCH: 4
Loss=0.9190222024917603 Batch_id=781 Accuracy=69.57: 100%|██████████| 782/782 [00:27<00:00, 28.45it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.8508, Accuracy: 7034/10000 (70.34%)


EPOCH: 5
Loss=0.892803430557251 Batch_id=781 Accuracy=72.17: 100%|██████████| 782/782 [00:26<00:00, 29.05it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.7700, Accuracy: 7327/10000 (73.27%)


EPOCH: 6
Loss=0.4105657637119293 Batch_id=781 Accuracy=74.12: 100%|██████████| 782/782 [00:26<00:00, 29.65it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.7803, Accuracy: 7212/10000 (72.12%)


EPOCH: 7
Loss=0.7347368001937866 Batch_id=781 Accuracy=75.73: 100%|██████████| 782/782 [00:26<00:00, 29.57it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6627, Accuracy: 7666/10000 (76.66%)


EPOCH: 8
Loss=0.8855469226837158 Batch_id=781 Accuracy=77.31: 100%|██████████| 782/782 [00:25<00:00, 30.34it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6393, Accuracy: 7774/10000 (77.74%)


EPOCH: 9
Loss=0.3541273772716522 Batch_id=781 Accuracy=78.11: 100%|██████████| 782/782 [00:26<00:00, 29.58it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6392, Accuracy: 7787/10000 (77.87%)


EPOCH: 10
Loss=1.7536847591400146 Batch_id=781 Accuracy=78.74: 100%|██████████| 782/782 [00:26<00:00, 29.63it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6706, Accuracy: 7737/10000 (77.37%)


EPOCH: 11
Loss=0.5356900095939636 Batch_id=781 Accuracy=79.48: 100%|██████████| 782/782 [00:26<00:00, 31.26it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.5800, Accuracy: 7983/10000 (79.83%)


EPOCH: 12
Loss=0.4610078036785126 Batch_id=781 Accuracy=80.31: 100%|██████████| 782/782 [00:26<00:00, 29.46it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.5735, Accuracy: 8067/10000 (80.67%)


EPOCH: 13
Loss=0.4945637285709381 Batch_id=781 Accuracy=81.11: 100%|██████████| 782/782 [00:26<00:00, 29.29it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.5734, Accuracy: 8049/10000 (80.49%)


EPOCH: 14
Loss=0.5537509918212891 Batch_id=781 Accuracy=81.50: 100%|██████████| 782/782 [00:26<00:00, 30.55it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.5468, Accuracy: 8134/10000 (81.34%)


EPOCH: 15
Loss=0.6712223291397095 Batch_id=781 Accuracy=81.98: 100%|██████████| 782/782 [00:26<00:00, 31.88it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.5591, Accuracy: 8076/10000 (80.76%)


EPOCH: 16
Loss=0.6152092814445496 Batch_id=781 Accuracy=81.83: 100%|██████████| 782/782 [00:26<00:00, 29.08it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.5602, Accuracy: 8135/10000 (81.35%)


EPOCH: 17
Loss=0.5589620471000671 Batch_id=781 Accuracy=82.74: 100%|██████████| 782/782 [00:26<00:00, 29.28it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.5223, Accuracy: 8218/10000 (82.18%)


EPOCH: 18
Loss=0.43986088037490845 Batch_id=781 Accuracy=83.15: 100%|██████████| 782/782 [00:26<00:00, 29.98it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.5653, Accuracy: 8117/10000 (81.17%)


EPOCH: 19
Loss=0.33764076232910156 Batch_id=781 Accuracy=83.46: 100%|██████████| 782/782 [00:26<00:00, 29.67it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.5646, Accuracy: 8127/10000 (81.27%)


EPOCH: 20
Loss=0.5380005836486816 Batch_id=781 Accuracy=83.73: 100%|██████████| 782/782 [00:26<00:00, 29.85it/s]

Test set: Average loss: 0.5175, Accuracy: 8241/10000 (82.41%)


