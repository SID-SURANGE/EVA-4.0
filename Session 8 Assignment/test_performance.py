#https://www.stefanfiott.com/machine-learning/cifar-10-classifier-using-cnn-in-pytorch/
from imports_eva import *


def test_performance(model, testloader, device, classes):
    total_correct = 0
    total_images = 0
    confusion_matrix = np.zeros([10,10], int)
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total_images += labels.size(0)
            total_correct += (predicted == labels).sum().item()
            for i, l in enumerate(labels):
                confusion_matrix[l.item(), predicted[i].item()] += 1

    model_accuracy = total_correct / total_images * 100
    print('------------------------------------------------------------')
    print('Model accuracy on {0} test images: {1:.2f}%'.format(total_images, model_accuracy))
    print('------------------------------------------------------------')
    print(' ')

    # print the category wise accuracy
    print('{0:10s} - {1}'.format('Category', 'Accuracy'))
    for i, r in enumerate(confusion_matrix):
        print('{0:10s} - {1:.2f}'.format(classes[i], r[i] / np.sum(r) * 100))

    # plot confusion matrix for each category
    print(' ')
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.matshow(confusion_matrix, aspect='auto', vmin=0, vmax=1000, cmap=plt.get_cmap('Reds'))
    plt.ylabel('Actual Category')
    plt.yticks(range(10), classes)
    plt.xlabel('Predicted Category')
    plt.xticks(range(10), classes)
    plt.show()