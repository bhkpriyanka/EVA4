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
Loss=1.1668179035186768 Batch_id=781 Accuracy=45.43: 100%|██████████| 782/782 [00:19<00:00, 39.76it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 1.6207, Accuracy: 4501/10000 (45.01%)


EPOCH: 2
Loss=1.200003981590271 Batch_id=781 Accuracy=63.80: 100%|██████████| 782/782 [00:19<00:00, 40.44it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.9326, Accuracy: 6721/10000 (67.21%)


EPOCH: 3
Loss=1.1004375219345093 Batch_id=781 Accuracy=70.34: 100%|██████████| 782/782 [00:19<00:00, 40.37it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.8389, Accuracy: 7088/10000 (70.88%)


EPOCH: 4
Loss=0.7715393304824829 Batch_id=781 Accuracy=74.29: 100%|██████████| 782/782 [00:19<00:00, 40.18it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.8785, Accuracy: 6994/10000 (69.94%)


EPOCH: 5
Loss=0.5159299373626709 Batch_id=781 Accuracy=77.04: 100%|██████████| 782/782 [00:19<00:00, 40.23it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.7840, Accuracy: 7365/10000 (73.65%)


EPOCH: 6
Loss=0.5607975125312805 Batch_id=781 Accuracy=79.04: 100%|██████████| 782/782 [00:19<00:00, 40.16it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.7199, Accuracy: 7466/10000 (74.66%)


EPOCH: 7
Loss=0.39124926924705505 Batch_id=781 Accuracy=80.98: 100%|██████████| 782/782 [00:19<00:00, 40.28it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6559, Accuracy: 7716/10000 (77.16%)


EPOCH: 8
Loss=0.7989146709442139 Batch_id=781 Accuracy=82.26: 100%|██████████| 782/782 [00:19<00:00, 40.48it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.7210, Accuracy: 7569/10000 (75.69%)


EPOCH: 9
Loss=0.44219350814819336 Batch_id=781 Accuracy=83.49: 100%|██████████| 782/782 [00:19<00:00, 40.16it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6009, Accuracy: 7991/10000 (79.91%)


EPOCH: 10
Loss=1.3877177238464355 Batch_id=781 Accuracy=84.61: 100%|██████████| 782/782 [00:19<00:00, 40.49it/s]

Test set: Average loss: 0.6162, Accuracy: 7918/10000 (79.18%)


