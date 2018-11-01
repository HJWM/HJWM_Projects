# 手写数字识别
* 数据集下载地址：链接: https://pan.baidu.com/s/1m98ASFDcTtqEQKwGPE0V_Q 提取码: a3bq
* 数据集内有三个文件具体定义在https://www.kaggle.com/c/digit-recognizer/data
    * sample_submission.csv为一个提交样例，28kx2列，每列分别为图像id以及预测的标签。
    * test.csv 28Kx784，每一行组成一个28x28像素的手写数字图像，如下图所示
    ```
        000 001 002 003 ... 026 027
        028 029 030 031 ... 054 055
        056 057 058 059 ... 082 083
         |   |   |   |  ...  |   |
        728 729 730 731 ... 754 755
        756 757 758 759 ... 782 783 
    ```
    * 比赛任务为对这个test.csv的数据提交一个结构如sample_submission.csv的预测结果
    * train.csv 42Kx785比test.csv多了一列，为标签列。
    * 评价指标：预测正确占测试集的百分比。
* 作业任务：使用KNN和朴素贝叶斯方法对数据集进行训练。对test集生成结果。
    * 代码依旧按照姓名首字母为文件夹整体提交
    * 有兴趣的同学可以注册kaggle账号提交自己的预测结果。
    * 如果无法登录到kaggle，可将train的一部分提取出来作为自己的验证集合。也可做出对test集的预测，小组解决网络支持进行结果的提交。
    * 自行将自己的得分统计到下方表格
    * 可将代码提交到kaggle上，将kaggle kernel的页面加入到下方表格。
# 已提交结果
| 姓名首字母 | 得分(%) | kaggle kernel url |
| :------: | :------: | :------: |
| FZ_NB | 83.114 | outline |
| FZ_PCA&KNN | 97.242 | outline |
| FZ_PCA&SVM | 98.185 | outline |
