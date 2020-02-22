TARGET:
1.create end-to-end setup and fully functional basic code skeleton.
2.Normalize dataset,define data transformations after visualizing data shape and distribution.
3.Create dataloaders and set test and train loops

RESULTS:
#params: 89664
best train acc: 99.21
best test acc: 99.15

ANALYSIS:
1.Model is quiet heavy in terms of no. of parameters.
2.The gap between train accuracy and the test accuracy is high most of the times i.e., model is overfitting.
  
 Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 16, 26, 26]             144
              ReLU-2           [-1, 16, 26, 26]               0
            Conv2d-3           [-1, 32, 24, 24]           4,608
              ReLU-4           [-1, 32, 24, 24]               0
            Conv2d-5           [-1, 10, 24, 24]             320
         MaxPool2d-6           [-1, 10, 12, 12]               0
            Conv2d-7           [-1, 20, 10, 10]           1,800
              ReLU-8           [-1, 20, 10, 10]               0
            Conv2d-9             [-1, 32, 8, 8]           5,760
             ReLU-10             [-1, 32, 8, 8]               0
           Conv2d-11             [-1, 64, 6, 6]          18,432
             ReLU-12             [-1, 64, 6, 6]               0
           Conv2d-13            [-1, 100, 6, 6]          57,600
             ReLU-14            [-1, 100, 6, 6]               0
        AvgPool2d-15            [-1, 100, 1, 1]               0
           Conv2d-16             [-1, 10, 1, 1]           1,000
================================================================  
Total params: 89,664
Trainable params: 89,664
Non-trainable params: 0

**LOGS**  
  0%|          | 0/469 [00:00<?, ?it/s]EPOCH: 0
Loss=2.302467107772827 Batch_id=468 Accuracy=10.99: 100%|██████████| 469/469 [00:09<00:00, 47.02it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 2.3021, Accuracy: 974/10000 (9.74%)

EPOCH: 1
Loss=2.2995870113372803 Batch_id=468 Accuracy=11.70: 100%|██████████| 469/469 [00:09<00:00, 48.26it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 2.2984, Accuracy: 1282/10000 (12.82%)

EPOCH: 2
Loss=0.275231271982193 Batch_id=468 Accuracy=48.78: 100%|██████████| 469/469 [00:09<00:00, 48.45it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.3014, Accuracy: 9072/10000 (90.72%)

EPOCH: 3
Loss=0.09147423505783081 Batch_id=468 Accuracy=94.61: 100%|██████████| 469/469 [00:09<00:00, 47.23it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.1105, Accuracy: 9658/10000 (96.58%)

EPOCH: 4
Loss=0.07779335975646973 Batch_id=468 Accuracy=96.98: 100%|██████████| 469/469 [00:10<00:00, 45.58it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0794, Accuracy: 9746/10000 (97.46%)

EPOCH: 5
Loss=0.05202610790729523 Batch_id=468 Accuracy=97.61: 100%|██████████| 469/469 [00:09<00:00, 48.51it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0472, Accuracy: 9854/10000 (98.54%)

EPOCH: 6
Loss=0.022567197680473328 Batch_id=468 Accuracy=98.13: 100%|██████████| 469/469 [00:09<00:00, 47.94it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0418, Accuracy: 9860/10000 (98.60%)

EPOCH: 7
Loss=0.028238752856850624 Batch_id=468 Accuracy=98.48: 100%|██████████| 469/469 [00:09<00:00, 47.08it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0358, Accuracy: 9882/10000 (98.82%)

EPOCH: 8
Loss=0.015676042065024376 Batch_id=468 Accuracy=98.61: 100%|██████████| 469/469 [00:09<00:00, 47.38it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0364, Accuracy: 9895/10000 (98.95%)

EPOCH: 9
Loss=0.08387544006109238 Batch_id=468 Accuracy=98.80: 100%|██████████| 469/469 [00:10<00:00, 45.08it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0293, Accuracy: 9910/10000 (99.10%)

EPOCH: 10
Loss=0.0073745050467550755 Batch_id=468 Accuracy=98.93: 100%|██████████| 469/469 [00:09<00:00, 47.91it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0310, Accuracy: 9906/10000 (99.06%)

EPOCH: 11
Loss=0.012476627714931965 Batch_id=468 Accuracy=99.07: 100%|██████████| 469/469 [00:09<00:00, 48.40it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0355, Accuracy: 9884/10000 (98.84%)

EPOCH: 12
Loss=0.04786286875605583 Batch_id=468 Accuracy=99.09: 100%|██████████| 469/469 [00:09<00:00, 48.68it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0337, Accuracy: 9898/10000 (98.98%)

EPOCH: 13
Loss=0.0064407289028167725 Batch_id=468 Accuracy=99.19: 100%|██████████| 469/469 [00:09<00:00, 48.16it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0306, Accuracy: 9905/10000 (99.05%)

EPOCH: 14
Loss=0.01571367122232914 Batch_id=468 Accuracy=99.21: 100%|██████████| 469/469 [00:10<00:00, 46.42it/s]

Test set: Average loss: 0.0265, Accuracy: 9915/10000 (99.15%)
