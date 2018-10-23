# python version 3.5, all 3.x is ok
import sys
sys.path.append('../../')
sys.path.append('.')
from work3.work_info.utils import * # (./utils)make pycharm happy


def train(trainData, trainLabel):
    # w 数据维数行，1列
    w = np.array([0, 0], float).transpose()
    b = 0
    lrate = 1
    # --------------------------------------------
    # algorithm start here
    while (True):
        badcnt = 0
        for ii in range(len(trainLabel)):
            if (trainLabel[ii] * (w.dot(trainData[:, ii]) + b) <= 0):
                badcnt += 1
                w += lrate * trainLabel[ii] * trainData[:, ii]
                b += lrate * trainLabel[ii]
        if (badcnt == 0):
            break
    return w, b


if __name__ == "__main__":
    # trainData, trainLabel = generate_dataset_norm(np.array([[0,0],[1,-1]]),[0.1],50)
    # train data: 数据维度行，样本个数列
    trainData, trainLabel = generate_dataset_static()
    w, b = train(trainData, trainLabel)
    plot_data(w, b, trainData, trainLabel)
