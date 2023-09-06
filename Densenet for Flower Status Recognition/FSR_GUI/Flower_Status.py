import sys

from PyQt5.QtWidgets import QMessageBox, QDialog, QMainWindow

from densenet.predict import predict
from kid import *
from main import *


class MainShow(QtWidgets.QWidget, Ui_Main_Dialog):
    def __init__(self):
        super(MainShow, self).__init__()
        self.setupUi(self)
        # 上传图片
        self.pushButton_2.clicked.connect(self.ChoosePath)
        # 开始识别
        self.pushButton.clicked.connect(self.Recognition)
        self.test_path = ''

    def ChoosePath(self):
        global fname
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, "打开图片", self.test_path, "图片(*.jpg)")
        # print(file_name[0])
        self.test_path = file_name[0]
        # 显示路径
        self.lineEdit_2.setText(self.test_path)
        # 显示待测图片
        self.label_4.setPixmap(QtGui.QPixmap(self.test_path))
        fname = file_name[0]

        # 清空不相关内容
        self.lineEdit.clear()

    def Recognition(self):
        global fname
        # 存获取的地址
        image_path = self.lineEdit_2.text()
        if image_path == "":
            print(QMessageBox.warning(self, "警告", "未插入图片！\n无法进行花卉状态识别！", QMessageBox.Yes, QMessageBox.Yes))
            return
        else:
            img_path = str(fname)
            result = predict(img_path)
            self.lineEdit.setText(result)
            print(QMessageBox.information(self, "成功识别花卉状态类型！", "状态识别结果为：" + result, QMessageBox.Yes, QMessageBox.Yes))


class KidShow(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(KidShow, self).__init__()
        self.setupUi(self)
        # 上传图片
        self.pushButton.clicked.connect(self.ShowOtherTrash)
        # 开始识别
        self.pushButton_2.clicked.connect(self.ShowRecyclableTrash)

    def ShowRecyclableTrash(self):
        self.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; "
                           "color:#428663;\">花卉生长状态介绍</span></p></body></html>")
        self.label_2.setText("<html><head/><body>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">花卉状态通常指花卉的健康和生长状态。以下是一些常见的花卉状态：</span></p><br/>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">1. 生长状况：花卉的生长状态可以分为正常、弱势和病态三种状态。生长状况：</span></p>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">花卉的生长状态可以分为正常、弱势和病态三种状态。正常状态下，花卉叶片茂</span></p>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">盛、花朵艳丽，生长状况良好；弱势状态下，花卉生长缓慢、叶片干枯、花朵不</span></p>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">良，需要及时调整生长环境；病态状态下，花卉被病虫害侵袭或生长环境受到严</span></p>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">重干扰，需要进行病虫害防治或环境调整。</span></p><br/>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">2. 绿叶状态：花卉的叶片颜色可以分为健康的绿色、黄色和褐色。健康的绿色</span></p>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\"表示花卉养分充足，生长健康；黄色则可能表示花卉叶片缺乏养分或遭受病虫害</span></p>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">侵袭；褐色则可能表示花卉遭受灼伤或缺水。</span></p><br/>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">3. 开花状况：花卉开花状况可以分为开花期、花期结束、花期延长三种状态。</span></p>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">开花期内，花卉花朵开放、色彩鲜艳；花期结束后，花卉花朵凋谢、掉落，进入休</span></p>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">眠期；花期延长时，花卉花朵持续开放，需要进行适当的管理和调整。</span></p>"
                             "<p><span font-size:12pt; font-weight:600;\"></span></p></body></html>")
        pixmap = QPixmap("C:/Users/Pengyk/Desktop\Densenet for Flower Status Recognition/image/花1.jpg")
        self.label_3.setScaledContents(True)
        self.label_3.setPixmap(pixmap)

    def ShowOtherTrash(self):
        self.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; "
                           "color:#428663;\">花卉养护策略</span></p></body></html>")
        self.label_2.setText("<html><head/><body>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">1. 给花卉提供适当的光照：不同的花卉对光照的需求不同，一般来说，阳光充足</span></p>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">的地方适合生长喜阳的花卉，阴凉潮湿的环境适合生长喜阴的花卉。在室内养花时</span></p>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">，应选择光线充足的位置，避免过度阴暗或过度照射。</span></p><br/>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">2. 适度浇水：花卉的生长需要适度的水分，过度浇水或缺水都会对花卉的生长产</span></p>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">生影响。浇水时应注意避免水渍积累在花盆底部，同时要注意避免花卉的根系长期</span></p>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">处于水浸状态。</span></p><br/>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">3. 预防和治疗病虫害：病虫害会对花卉造成很大的伤害，影响花卉的生长和开花。</span></p>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">可以采取预防措施，如保持花卉周围环境卫生，定期喷洒杀虫剂或杀菌剂等，同时</span></p>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">注意观察花卉的病虫害状况，及时采取治疗措施。</span></p><br/>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">4. 定期修剪：定期修剪可以促进花卉的生长和分枝，使其更加茂盛和美观。修剪</span></p>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">时应注意保持花卉的自然形态，避免过度修剪和伤害花卉的健康部位。<br/>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">5. 适宜的环境温度：花卉对环境温度的适应范围不同，应注意根据不同花卉的温度</span></p>"
                             "<p><span style=\" font-size:12pt; font-weight:600;\">适应性调节室内温度和通风情况。</span></p></body></html>")
        pixmap = QPixmap("C:/Users/Pengyk/Desktop\Densenet for Flower Status Recognition/image/花.jpg")
        self.label_3.setScaledContents(True)
        self.label_3.setPixmap(pixmap)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # 实例化主窗口
    main = QMainWindow()
    main_ui = Ui_Main_Dialog()
    main_ui.setupUi(main)
    main = MainShow()
    main.setWindowTitle("花卉状态识别系统")
    main.setWindowIcon(QIcon('image/logo1.jpg'))

    # 实例化子窗口
    child = QDialog()
    child.setWindowTitle("花卉状态识别系统")
    child.setWindowIcon(QIcon('image/logo1.jpg'))
    child_ui = Ui_Dialog()
    child_ui.setupUi(child)
    child1 = KidShow()
    # 按钮绑定事件
    btn = main.pushButton_3
    btn.clicked.connect(child1.show)

    # 显示主窗口
    main.show()
    sys.exit(app.exec_())
