
# plot Loss and acc plots for train/test data
from imports_eva import *


def train_testplots(trainloss, trainacc, testloss, testacc):
    fig, axs = plt.subplots(2,2,figsize=(15,10))
    axs[0, 0].plot(trainloss)
    axs[0, 0].set_title("Training Loss")
    axs[1, 0].plot(trainacc)
    axs[1, 0].set_title("Training Accuracy")
    axs[0, 1].plot(testloss)
    axs[0, 1].set_title("Test Loss")
    axs[1, 1].plot(testacc)
    axs[1, 1].set_title("Test Accuracy")
  
