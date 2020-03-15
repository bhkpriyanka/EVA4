**Assignment:**   
1.Go through this repository: https://github.com/kuangliu/pytorch-cifar  
2.Extract the ResNet18 model from this repository and add it to your API/repo.  
3.Use your data loader, model loading, train, and test code to train ResNet18 on Cifar10   
4.Your Target is 85% accuracy. No limit on the number of epochs. Use default ResNet18 code (so params are fixed).  
  
**SOLUTION SUMMARY:**  
 
 **FINAL ACCURACY:88.09%**  
 **LOGS:** 
   
   0%|          | 0/782 [00:00<?, ?it/s]EPOCH: 1
Loss=2.150298833847046 Batch_id=781 Accuracy=28.17: 100%|██████████| 782/782 [00:34<00:00, 22.47it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0248, Accuracy: 4140/10000 (41.40%)


EPOCH: 2
Loss=1.5966774225234985 Batch_id=781 Accuracy=46.03: 100%|██████████| 782/782 [00:34<00:00, 22.41it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0211, Accuracy: 5097/10000 (50.97%)


EPOCH: 3
Loss=1.4073090553283691 Batch_id=781 Accuracy=55.32: 100%|██████████| 782/782 [00:34<00:00, 22.53it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0181, Accuracy: 5788/10000 (57.88%)


EPOCH: 4
Loss=1.2261829376220703 Batch_id=781 Accuracy=63.33: 100%|██████████| 782/782 [00:34<00:00, 22.49it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0144, Accuracy: 6782/10000 (67.82%)


EPOCH: 5
Loss=0.6967671513557434 Batch_id=781 Accuracy=68.18: 100%|██████████| 782/782 [00:34<00:00, 22.40it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0122, Accuracy: 7254/10000 (72.54%)


EPOCH: 6
Loss=1.7448810338974 Batch_id=781 Accuracy=72.15: 100%|██████████| 782/782 [00:34<00:00, 22.46it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0117, Accuracy: 7410/10000 (74.10%)


EPOCH: 7
Loss=0.39297041296958923 Batch_id=781 Accuracy=75.31: 100%|██████████| 782/782 [00:34<00:00, 22.44it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0100, Accuracy: 7804/10000 (78.04%)


EPOCH: 8
Loss=1.373530387878418 Batch_id=781 Accuracy=77.70: 100%|██████████| 782/782 [00:34<00:00, 22.41it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0091, Accuracy: 8012/10000 (80.12%)


EPOCH: 9
Loss=0.6257967948913574 Batch_id=781 Accuracy=79.88: 100%|██████████| 782/782 [00:34<00:00, 22.54it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0083, Accuracy: 8187/10000 (81.87%)


EPOCH: 10
Loss=0.48776760697364807 Batch_id=781 Accuracy=81.61: 100%|██████████| 782/782 [00:35<00:00, 23.80it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0084, Accuracy: 8146/10000 (81.46%)


EPOCH: 11
Loss=0.3905644416809082 Batch_id=781 Accuracy=85.36: 100%|██████████| 782/782 [00:34<00:00, 22.52it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0066, Accuracy: 8585/10000 (85.85%)


EPOCH: 12
Loss=0.501103401184082 Batch_id=781 Accuracy=86.25: 100%|██████████| 782/782 [00:34<00:00, 22.47it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0063, Accuracy: 8636/10000 (86.36%)


EPOCH: 13
Loss=0.3487904369831085 Batch_id=781 Accuracy=86.74: 100%|██████████| 782/782 [00:34<00:00, 22.47it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0063, Accuracy: 8672/10000 (86.72%)


EPOCH: 14
Loss=0.5686886310577393 Batch_id=781 Accuracy=87.03: 100%|██████████| 782/782 [00:34<00:00, 22.41it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0062, Accuracy: 8694/10000 (86.94%)


EPOCH: 15
Loss=0.40081724524497986 Batch_id=781 Accuracy=87.44: 100%|██████████| 782/782 [00:34<00:00, 22.37it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0061, Accuracy: 8711/10000 (87.11%)


EPOCH: 16
Loss=0.12237614393234253 Batch_id=781 Accuracy=87.55: 100%|██████████| 782/782 [00:34<00:00, 22.36it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0060, Accuracy: 8741/10000 (87.41%)


EPOCH: 17
Loss=0.4604853093624115 Batch_id=781 Accuracy=87.99: 100%|██████████| 782/782 [00:34<00:00, 22.51it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0060, Accuracy: 8727/10000 (87.27%)


EPOCH: 18
Loss=0.22890082001686096 Batch_id=781 Accuracy=88.09: 100%|██████████| 782/782 [00:34<00:00, 22.53it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0059, Accuracy: 8744/10000 (87.44%)


EPOCH: 19
Loss=0.6904873251914978 Batch_id=781 Accuracy=88.31: 100%|██████████| 782/782 [00:34<00:00, 22.38it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0060, Accuracy: 8735/10000 (87.35%)


EPOCH: 20
Loss=0.09879089891910553 Batch_id=781 Accuracy=88.67: 100%|██████████| 782/782 [00:34<00:00, 22.43it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0059, Accuracy: 8762/10000 (87.62%)


EPOCH: 21
Loss=0.1954169124364853 Batch_id=781 Accuracy=89.28: 100%|██████████| 782/782 [00:34<00:00, 22.47it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0057, Accuracy: 8786/10000 (87.86%)


EPOCH: 22
Loss=0.10236484557390213 Batch_id=781 Accuracy=89.53: 100%|██████████| 782/782 [00:35<00:00, 22.34it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0057, Accuracy: 8780/10000 (87.80%)


EPOCH: 23
Loss=0.3209694027900696 Batch_id=781 Accuracy=89.37: 100%|██████████| 782/782 [00:34<00:00, 22.48it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0057, Accuracy: 8777/10000 (87.77%)


EPOCH: 24
Loss=0.29714351892471313 Batch_id=781 Accuracy=89.36: 100%|██████████| 782/782 [00:34<00:00, 22.49it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0057, Accuracy: 8797/10000 (87.97%)


EPOCH: 25
Loss=0.2669198215007782 Batch_id=781 Accuracy=89.50: 100%|██████████| 782/782 [00:34<00:00, 22.66it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0058, Accuracy: 8776/10000 (87.76%)


EPOCH: 26
Loss=0.09272219240665436 Batch_id=781 Accuracy=89.51: 100%|██████████| 782/782 [00:34<00:00, 22.54it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0057, Accuracy: 8792/10000 (87.92%)


EPOCH: 27
Loss=0.21923089027404785 Batch_id=781 Accuracy=89.58: 100%|██████████| 782/782 [00:34<00:00, 22.39it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0056, Accuracy: 8809/10000 (88.09%)


EPOCH: 28
Loss=0.0818018689751625 Batch_id=781 Accuracy=89.60: 100%|██████████| 782/782 [00:34<00:00, 22.44it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0057, Accuracy: 8789/10000 (87.89%)


EPOCH: 29
Loss=0.12163016945123672 Batch_id=781 Accuracy=89.53: 100%|██████████| 782/782 [00:34<00:00, 22.47it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.0057, Accuracy: 8784/10000 (87.84%)


EPOCH: 30
Loss=0.39371156692504883 Batch_id=781 Accuracy=89.47: 100%|██████████| 782/782 [00:34<00:00, 22.52it/s]

Test set: Average loss: 0.0058, Accuracy: 8782/10000 (87.82%)

