### sklearn.cross_validation

##### train_test_split

random_state      随机数的种子。

如果指定了random_state，在重复试验的时候，可以保证得到一组一样的随机数。比如你每次都指定0/1/...，其他参数一样的情况下你得到的随机数是一样的。但如果不填，每次都会不一样。

种子不同，产生不同的随机数；种子相同，即使实例不同也产生相同的随机数。

### sklearn.preprocessing

##### StandardScaler

标准化数据，将每列数据转换成均值为0，方差为1。

fit_transform()

transform()

inverse_transform()

### sklearn.svm

##### 分类

SVC，NuSVC：两者仅仅在于对损失的度量方式不同。**默认的高斯核'rbf‘，也成为径向基函数核**。这时我们主要需要对惩罚系数C和核函数参数γγ进行艰苦的调参，通过多轮的交叉验证选择合适的惩罚系数C和核函数参数γγ。

LinearSVC：线性分类，也就是不支持各种低维到高维的核函数，仅仅支持线性核函数，对线性不可分的数据不能使用。

##### 回归

SVR，NuSVR，LinearSVR    与分类一样

我们使用这些类的时候，如果有经验知道数据是线性可以拟合的，那么使用LinearSVC去分类 或者LinearSVR去回归，它们不需要我们去慢慢的调参去选择各种核函数以及对应参数， 速度也快。如果我们对数据分布没有什么经验，一般使用SVC去分类或者SVR去回归，这就需要我们选择核函数以及对核函数调参了。

linearSVR和 SVR(kernel = linear)是不一样的：

Similar to SVR with parameter kernel=’linear’, but implemented in terms of **liblinear** rather than libsvm, so it has more flexibility in the choice of penalties and loss functions and should scale better to **large numbers of samples**.

### sklearn.feature_extraction.text

文本特征提取

##### CountVectorizer

记录每个词汇在当前训练文本中出现的频率

##### TfidfVectorizer

不仅记录每个词汇在当前训练文本中出现的频率，还关注包含这个词汇的训练文本个数的倒数

向量转化

### sklearn.naive_bayes

朴素贝叶斯，主要有三种实现：GaussianNB，MultinomialNB和BernoulliNB。

GaussianNB就是先验为高斯分布的朴素贝叶斯，MultinomialNB就是先验为多项式分布的朴素贝叶斯，而BernoulliNB就是先验为伯努利分布的朴素贝叶斯。

这三个类适用的分类场景各不相同，一般来说，如果样本特征的分布大部分是连续值，使用GaussianNB会比较好。如果如果样本特征的分大部分是多元离散值，使用MultinomialNB比较合适。而如果样本特征是二元离散值或者很稀疏的多元离散值，应该使用BernoulliNB

### 数据描述

DataFrame: a.describe()    a.info()

数据集（iris) : a.DESCR    (存在a.data a.target)

### sklearn.neighbors

##### KNeighborsClassifier

K近邻分类

##### KNeighborsRegressor

K近邻分类

### sklearn.tree

##### DecisionTreeClassifier

分类决策树

##### DecisionTreeRegressor

回归树

### sklearn.ensemble

集成模型

##### RandomForestClassifier

##### RandomForestRegressor

随机森林

##### ExtraTreeClassifier

##### ExtraTreeRegressor

类似于随机森林，也是一种基于随机决策树的平均算法

##### GradientBoostingClassifier

##### GradientBoostingRegressor

梯度提升树

### sklearn.cluster

##### KMeans

聚类：衡量标准

- 测试数据本身带有正确类别信息

  adjusted_rand_score()

- 测试数据没有类别信息

  轮廓系数

