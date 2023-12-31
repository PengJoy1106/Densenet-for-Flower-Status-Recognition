# 目录框架
Densenet for Flower Status Recognition
	datasets
		train
		val
	densenet
		model.py
		predict.py
		train.py
		utils.py
	FSR_GUI
		Flower_Status.py
		kid.py
		kid.ui
		main.py
		main.ui
	image
	results
	weights
	my_dataset.py


# datasets
该目录下存放的为数据集，数据集分为两大类，分别是侵染性和非侵染性

# densenet
该目录下存放了Densenet网络的模型以及训练、预测文件
- model.py: 即网络模型文件
- train.py: 为网络训练文件，执行此脚本即可对模型进行训练
- predict.py: 为预测文件，可以单独预测每一张图片，并返回预测结果
- class_indices.json: 记录数据集的类别和标签

# FSR_GUI
该目录为上位机的构成文件
- main.py / main.ui  : 主界面构成文件
- kid.py / kid.ui : 次界面构成文件
- Flower_Status.py : 各种点击事件的功能实现
- 
# image
存放了一些在上位机显示的图片
# results
存放了两种数据集的训练结果，这些结果包括：
- tensorbord日志：可以在网页查看训练效果，并自动生成曲线图
- 权重文件：保留了识别率最高的权重，以便检测用
- 训练结果表格数据和曲线图：保存了将训练的准确率、损失值、学习率，并基于这些数据绘制了前100轮的三种数据的曲线
# weights
存放了densenet网络官方默认的权重文件
# 其他文件
1. my_darasets.py
   用于读取图像文件和其对应的标签，并将它们组成数据返回给训练或测试模型，此外还可以与PyTorch的dataloader结合使用，实现批量加载和预处理数据。
2. plot.py
   读取.CSV的表格文件，并基于表格里的数据绘制曲线图，分别绘制了准确率、损失值、学习率的曲线图
# 相关说明
1. 准确率
‌‌‌　　准确率（Accuracy）是评估分类模型性能的一种常用指标，表示模型正确预测的样本占总样本数的比例。在二分类问题中，准确率可以表示为：
‌‌‌　　$$ accuracy = \frac{TP + TN}{TP + TN + FP + FN} $$
‌‌‌　　$$ 精度= \frac{TP + TN}{TP + TN + FP + FN} $$
‌‌‌　　其中，$TP$表示真阳性的数量，即实际为正类且被模型正确预测为正类的样本数；$TN$表示真阴性的数量，即实际为负类且被模型正确预测为负类的样本数；$FP$表示假阳性的数量，即实际为负类但被模型错误预测为正类的样本数；$FN$表示假阴性的数量，即实际为正类但被模型错误预测为负类的样本数。
‌‌‌　　准确率反映了模型对于所有样本的整体分类效果，值越高表示模型具有更好的分类能力。但是，在某些情况下，准确率并不能完全反映模型的优劣，比如当不同类别的样本数量不平衡时，准确率可能会出现误导性结果。因此，在实际应用中，可能需要结合其他指标来综合评估模型性能。
2. 损失值
‌‌‌　　损失值（Loss）是评估模型训练过程中优化目标函数的一种指标，表示模型在当前参数下对训练数据的预测误差大小。常用的损失函数包括均方误差（MSE）、交叉熵（Cross Entropy）等。
‌‌‌　　在训练过程中，模型的目标是通过不断迭代调整参数，使得损失值逐渐降低，直到收敛于一个较小的值。因此，损失值可以作为监控模型训练过程中是否收敛以及调整超参数的参考指标。
‌‌‌　　但是，损失值本身并不能完全反映模型的性能，因为过拟合和欠拟合都可能导致训练集上的损失值较低，但在测试集上表现不佳。因此，在实际应用中，需要综合考虑其他指标，如测试集上的准确率、召回率等来综合评估模型的性能。
3. 学习率
‌‌‌　　学习率（Learning Rate）是指在训练神经网络时，控制权重参数更新步幅的一个超参数。在神经网络中，每一层都有许多权重需要被学习和调整，而学习率就是控制每次权重更新的大小，从而让模型在训练过程中逐渐接近最优解。
‌‌‌　　通常情况下，学习率需要在训练前进行初始化，并在训练过程中根据模型的性能动态调整。如果学习率设置太小，模型训练收敛速度会变慢；如果学习率设置太大，模型可能无法收敛或者收敛到不理想的局部最优解。因此，在实际应用中，需要通过调试来找到一个合适的学习率值，以达到更好的训练效果。
‌‌‌　　除了常见的固定学习率外，还有很多自适应学习率算法，如Adagrad、Adam等，它们可以根据每个参数的历史梯度信息来动态地调整学习率，进一步提高模型的训练效果。