# 《统计学习方法第二章》
* work_info/alg_2_1.py,代码补全
    * 代码中有两个数据生成函数generate_dataset_norm和generate_dataset_static，分别是以参数设置的类别中心方差生成的正态分布数据以及书上例2.1的数据。static数据线性可分，而norm数据不一定（根据具体参数来说），运行代码，体会这两者的实际表现。
    * 有兴趣的同学参考`http://www.cnblogs.com/Determined22/p/6507329.html`实现松弛算法。
    * 立志于机器学习方向发展的同学，为了打下更深的功底可以参阅PRML，这个很难，看的话要长期坚持下去。
    * IDE推荐Pycharm，下载Community Edition就可以。
    * 如果pip下载速度过慢，可以更换西电linux开源镜像。地址：`https://linux.xidian.edu.cn/mirrors/`。在里面找pypi，链接右边的小问号就是更换教程。这个教程里的链接可在pycharm中使用。下载速度快，免流量。

* work_info/alg_2_2.py,代码补全
    * 实现感知机算法的对偶形式

* work_info/preceptron_2_1_torch.py
    * 利用pytorch的自动求导机制以及pytorch的基本框架完成的感知机原始形式
    * 理解代码，debug看看perceptron变量内包含了什么东西，是什么类型
    * 利用这些知识，使用感知机对偶形式补全preceptron_2_1_torch.py
----------------------------

* 建议python版本3.x
* 拷贝work_info内的文件到自己的目录，补全代码
* 若使用ide，注意不要提交ide产生的杂乱文件（.gitignore）
