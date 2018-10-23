# python version 3.5, all 3.x is ok
import sys
sys.path.append('../../')
sys.path.append('.')
from work3.work_info.utils import * # (./utils)make pycharm happy

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.optim as optim



def train(trainData, trainLabel):
    # w 数据维数行，1列
    perceptron = nn.Linear(trainData.shape[0], 1),  # w,b in nn.Linear (weight,bias), x will be feed to perception
    labelData = torch.Tensor()
    torch.nn.init.zeros_(perceptron[0].weight)
    torch.nn.init.zeros_(perceptron[0].bias)

    optimizer = optim.SGD([perceptron[0].weight, perceptron[0].bias], lr=1)

    # alg start here
    while (True):
        badcnt = 0
        for ii in range(len(trainLabel)):
            # variable enables the network to autograd
            inputTensor = Variable(torch.Tensor(trainData[:, ii]), requires_grad=True)
            labelTensor = Variable(torch.Tensor(np.array(trainLabel[ii])), requires_grad=True)
            perceptron[0].zero_grad()
            loss = -1 * perceptron[0](inputTensor) * labelTensor
            if (loss >= 0):
                loss.backward()
                optimizer.step()
                badcnt += 1

        if (badcnt == 0):
            break
    return perceptron[0].weight.data.numpy().transpose(), perceptron[0].bias.data.numpy()


if __name__ == "__main__":
    # trainData, trainLabel = generate_dataset_norm(np.array([[0,0],[1,-1]]),[0.1],50)
    # train data: 数据维度行，样本个数列
    trainData, trainLabel = generate_dataset_static()
    w, b = train(trainData, trainLabel)
    plot_data(w, b, trainData, trainLabel)
