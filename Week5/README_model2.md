**TARGET:**  
1.Reduce no.of overall parameters by tweaking layers & channel sizes.Finalize and fix the model skeleton.  
2.Play with batch size

**RESULTS:**  
*#params:*  10876  
*best train acc:*  99.16  
*best test acc:*  99.05

**ANALYSIS:**    
1.With reduction in number of params and no other change, a drop in accuracy was observed which was expected.  
2.Tried batch sizes of 64,100,128,256 and lower batch size of 64 improved and gave relatively better accuracies for this model.  

  Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 12, 26, 26]             108
              ReLU-2           [-1, 12, 26, 26]               0
            Conv2d-3           [-1, 16, 24, 24]           1,728
              ReLU-4           [-1, 16, 24, 24]               0
            Conv2d-5           [-1, 10, 24, 24]             160
         MaxPool2d-6           [-1, 10, 12, 12]               0
            Conv2d-7           [-1, 16, 10, 10]           1,440
              ReLU-8           [-1, 16, 10, 10]               0
            Conv2d-9             [-1, 20, 8, 8]           2,880
             ReLU-10             [-1, 20, 8, 8]               0
           Conv2d-11             [-1, 24, 6, 6]           4,320
             ReLU-12             [-1, 24, 6, 6]               0
        AvgPool2d-13             [-1, 24, 1, 1]               0
           Conv2d-14             [-1, 10, 1, 1]             240
================================================================  
Total params: 10,876
Trainable params: 10,876  

**LOGS**  
  0%|          | 0/938 [00:00<?, ?it/s]EPOCH: 1
Loss=0.4026837944984436 Batch_id=937 Accuracy=48.96: 100%|██████████| 938/938 [00:18<00:00, 49.58it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.1868, Accuracy: 9414/10000 (94.14%)

EPOCH: 2
Loss=0.053772732615470886 Batch_id=937 Accuracy=95.30: 100%|██████████| 938/938 [00:19<00:00, 49.00it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.1078, Accuracy: 9659/10000 (96.59%)

EPOCH: 3
Loss=0.014410972595214844 Batch_id=937 Accuracy=97.13: 100%|██████████| 938/938 [00:19<00:00, 49.18it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0752, Accuracy: 9772/10000 (97.72%)

EPOCH: 4
Loss=0.10268621146678925 Batch_id=937 Accuracy=97.80: 100%|██████████| 938/938 [00:19<00:00, 49.26it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0665, Accuracy: 9789/10000 (97.89%)

EPOCH: 5
Loss=0.01346561312675476 Batch_id=937 Accuracy=98.10: 100%|██████████| 938/938 [00:18<00:00, 54.46it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0603, Accuracy: 9806/10000 (98.06%)

EPOCH: 6
Loss=0.05644223093986511 Batch_id=937 Accuracy=98.39: 100%|██████████| 938/938 [00:18<00:00, 49.84it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0553, Accuracy: 9829/10000 (98.29%)

EPOCH: 7
Loss=0.008385300636291504 Batch_id=937 Accuracy=98.54: 100%|██████████| 938/938 [00:18<00:00, 50.57it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0439, Accuracy: 9861/10000 (98.61%)

EPOCH: 8
Loss=0.022823259234428406 Batch_id=937 Accuracy=98.65: 100%|██████████| 938/938 [00:18<00:00, 50.63it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0431, Accuracy: 9869/10000 (98.69%)

EPOCH: 9
Loss=0.0019380450248718262 Batch_id=937 Accuracy=98.85: 100%|██████████| 938/938 [00:18<00:00, 50.20it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0430, Accuracy: 9856/10000 (98.56%)

EPOCH: 10
Loss=0.010888278484344482 Batch_id=937 Accuracy=98.85: 100%|██████████| 938/938 [00:18<00:00, 50.41it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0391, Accuracy: 9873/10000 (98.73%)

EPOCH: 11
Loss=0.011479660868644714 Batch_id=937 Accuracy=99.04: 100%|██████████| 938/938 [00:18<00:00, 49.98it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0332, Accuracy: 9886/10000 (98.86%)

EPOCH: 12
Loss=0.08564302325248718 Batch_id=937 Accuracy=98.98: 100%|██████████| 938/938 [00:18<00:00, 51.66it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0551, Accuracy: 9828/10000 (98.28%)

EPOCH: 13
Loss=0.0018100440502166748 Batch_id=937 Accuracy=99.08: 100%|██████████| 938/938 [00:18<00:00, 50.86it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0334, Accuracy: 9895/10000 (98.95%)

EPOCH: 14
Loss=0.03090299665927887 Batch_id=937 Accuracy=99.16: 100%|██████████| 938/938 [00:18<00:00, 57.46it/s]
  0%|          | 0/938 [00:00<?, ?it/s]
Test set: Average loss: 0.0300, Accuracy: 9898/10000 (98.98%)

EPOCH: 15
Loss=0.007993310689926147 Batch_id=937 Accuracy=99.15: 100%|██████████| 938/938 [00:18<00:00, 51.54it/s]

Test set: Average loss: 0.0293, Accuracy: 9905/10000 (99.05%)
