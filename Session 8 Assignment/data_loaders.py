
from imports_eva import *


def train_test_loaders(b_size, rotate_val, n_workers=2):
    # defining the list of transformations to apply------------------------------------------
    transform = transforms.Compose(
      [transforms.RandomHorizontalFlip(),
        transforms.RandomRotation((-rotate_val, rotate_val)),
         transforms.ColorJitter(hue=.05, saturation=.05),
         transforms.ToTensor(),
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    # Download Train/test data----------------------------------------------------------------
    trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                            download=True, transform=transform)

    testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                           download=True, transform=transform)
    # Define data loaders---------------------------------------------------------------------
    # Train data loader
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=b_size,
                                              shuffle=True, num_workers=n_workers)
    # Test data loader
    testloader = torch.utils.data.DataLoader(testset, batch_size=b_size,
                                             shuffle=False, num_workers=n_workers)

    return trainloader, testloader