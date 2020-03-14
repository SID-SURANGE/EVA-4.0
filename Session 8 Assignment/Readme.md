<h2><i><b><font color='blue'>Session 8 Assignment</font></B></i></h2>
<hr>
<h3><i>Things to accomplish</i></h3>
<ol>
  <li>Use <b>Resnet 18</b> architecture and add it to API</li>
  <li>Use your data loader, model loading, train, and test code to train ResNet18 on <B>Cifar10</B></li>
  <li>Your Target is 85% accuracy. No limit on the number of epochs. Use default ResNet18 code (so params are fixed)</li>
</ol>
<hr>
<h3><i> FINAL Model Details</i></h3>
<ul>
  <li><B>Best Validation Accuracy</b>-86.76</li>
  <li><b>Epochs</b>-22</li>
  <li><b>Resnet18-parameters</b>- 11.174M</li>
  <li><b>Regularization</b>- Dropout(0.25), Augumentation(Flip,Rotate,ColorJitter), L2 Regularizer </li>
  <li><b>LR Optimizer</b>- MultiStepLR</li>
</ul>

<hr>
<h3><i>Model logs</i></h3>

```

0%|          | 0/782 [00:00<?, ?it/s]EPOCH: 0
Loss=1.6067308187484741 Batch_id=781 Accuracy=33.74: 100%|██████████| 782/782 [01:04<00:00, 12.12it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 1.4182, Accuracy: 4743/10000 (47.43%)


EPOCH: 1
Loss=1.0658259391784668 Batch_id=781 Accuracy=48.01: 100%|██████████| 782/782 [01:04<00:00, 12.15it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 1.1869, Accuracy: 5687/10000 (56.87%)


EPOCH: 2
Loss=1.1746418476104736 Batch_id=781 Accuracy=56.24: 100%|██████████| 782/782 [01:04<00:00, 12.15it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 1.0810, Accuracy: 6092/10000 (60.92%)


EPOCH: 3
Loss=0.5356218814849854 Batch_id=781 Accuracy=62.06: 100%|██████████| 782/782 [01:04<00:00, 12.11it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.8874, Accuracy: 6925/10000 (69.25%)


EPOCH: 4
Loss=0.8065565228462219 Batch_id=781 Accuracy=66.36: 100%|██████████| 782/782 [01:04<00:00, 12.18it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.7844, Accuracy: 7288/10000 (72.88%)


EPOCH: 5
Loss=1.4584007263183594 Batch_id=781 Accuracy=69.69: 100%|██████████| 782/782 [01:05<00:00, 11.98it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.7148, Accuracy: 7513/10000 (75.13%)


EPOCH: 6
Loss=0.6526321172714233 Batch_id=781 Accuracy=72.45: 100%|██████████| 782/782 [01:04<00:00, 12.03it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6677, Accuracy: 7699/10000 (76.99%)


EPOCH: 7
Loss=0.6602839231491089 Batch_id=781 Accuracy=74.69: 100%|██████████| 782/782 [01:05<00:00, 11.83it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6225, Accuracy: 7862/10000 (78.62%)


EPOCH: 8
Loss=0.7497401237487793 Batch_id=781 Accuracy=76.39: 100%|██████████| 782/782 [01:05<00:00, 11.99it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.6155, Accuracy: 7865/10000 (78.65%)


EPOCH: 9
Loss=0.44029703736305237 Batch_id=781 Accuracy=77.73: 100%|██████████| 782/782 [01:04<00:00, 12.04it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.5372, Accuracy: 8167/10000 (81.67%)


EPOCH: 10
Loss=0.8194993138313293 Batch_id=781 Accuracy=78.92: 100%|██████████| 782/782 [01:04<00:00, 12.08it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.5689, Accuracy: 8073/10000 (80.73%)


EPOCH: 11
Loss=0.45224636793136597 Batch_id=781 Accuracy=79.99: 100%|██████████| 782/782 [01:05<00:00, 11.90it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.5111, Accuracy: 8229/10000 (82.29%)


EPOCH: 12
Loss=0.760530412197113 Batch_id=781 Accuracy=80.74: 100%|██████████| 782/782 [01:05<00:00, 11.95it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.4935, Accuracy: 8321/10000 (83.21%)


EPOCH: 13
Loss=0.8037831783294678 Batch_id=781 Accuracy=81.51: 100%|██████████| 782/782 [01:05<00:00, 11.93it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.4811, Accuracy: 8337/10000 (83.37%)


EPOCH: 14
Loss=0.737858772277832 Batch_id=781 Accuracy=84.86: 100%|██████████| 782/782 [01:05<00:00, 12.03it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.4200, Accuracy: 8581/10000 (85.81%)


EPOCH: 15
Loss=0.20632360875606537 Batch_id=781 Accuracy=86.04: 100%|██████████| 782/782 [01:05<00:00, 12.00it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.4159, Accuracy: 8584/10000 (85.84%)


EPOCH: 16
Loss=0.5089669227600098 Batch_id=781 Accuracy=86.52: 100%|██████████| 782/782 [01:04<00:00, 12.07it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.3937, Accuracy: 8650/10000 (86.50%)


EPOCH: 17
Loss=0.6499801278114319 Batch_id=781 Accuracy=87.17: 100%|██████████| 782/782 [01:05<00:00, 11.94it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.3958, Accuracy: 8655/10000 (86.55%)


EPOCH: 18
Loss=0.33107608556747437 Batch_id=781 Accuracy=87.77: 100%|██████████| 782/782 [01:05<00:00, 11.94it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.3915, Accuracy: 8673/10000 (86.73%)


EPOCH: 19
Loss=0.42251846194267273 Batch_id=781 Accuracy=87.95: 100%|██████████| 782/782 [01:05<00:00, 12.01it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.3916, Accuracy: 8664/10000 (86.64%)


EPOCH: 20
Loss=0.18653617799282074 Batch_id=781 Accuracy=87.96: 100%|██████████| 782/782 [01:05<00:00, 11.98it/s]
  0%|          | 0/782 [00:00<?, ?it/s]
Test set: Average loss: 0.3866, Accuracy: 8676/10000 (86.76%)


EPOCH: 21
Loss=0.10344131290912628 Batch_id=781 Accuracy=87.93: 100%|██████████| 782/782 [01:04<00:00, 12.08it/s]

Test set: Average loss: 0.3919, Accuracy: 8675/10000 (86.75%)


```
<hr>
<h3><i>Misclassified samples</i></h3>

![Image](https://github.com/SID-SURANGE/EVA-4.0/blob/master/Session%208%20Assignment/S8_misclassified.png)

<hr>
Author - Siddharth Surange



  
