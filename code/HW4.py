from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import numpy as np
import time
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 211, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.origin_label = QtWidgets.QLabel(self.layoutWidget)
        self.origin_label.setObjectName("origin_label")
        self.verticalLayout.addWidget(self.origin_label)
        self.pushButton_select = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_select.setObjectName("pushButton_select")
        self.verticalLayout.addWidget(self.pushButton_select)
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setObjectName("layout")
        self.f_time = QtWidgets.QLineEdit(self.layoutWidget)
        self.f_time.setObjectName("f_time")
        self.layout.addWidget(self.f_time)
        self.verticalLayout.addLayout(self.layout)
        self.if_time = QtWidgets.QLineEdit(self.layoutWidget)
        self.if_time.setObjectName("if_time")
        self.verticalLayout.addWidget(self.if_time)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(240, 40, 861, 231))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_8.addWidget(self.lineEdit_5)
        self.spectrum = QtWidgets.QLabel(self.layoutWidget1)
        self.spectrum.setObjectName("spectrum")
        self.verticalLayout_8.addWidget(self.spectrum)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_9.addWidget(self.lineEdit_6)
        self.phase_angle = QtWidgets.QLabel(self.layoutWidget1)
        self.phase_angle.setObjectName("phase_angle")
        self.verticalLayout_9.addWidget(self.phase_angle)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_10.addWidget(self.lineEdit_7)
        self.inv_fourier = QtWidgets.QLabel(self.layoutWidget1)
        self.inv_fourier.setObjectName("inv_fourier")
        self.verticalLayout_10.addWidget(self.inv_fourier)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_11.addWidget(self.lineEdit_8)
        self.subtract_ori_invF = QtWidgets.QLabel(self.layoutWidget1)
        self.subtract_ori_invF.setObjectName("subtract_ori_invF")
        self.verticalLayout_11.addWidget(self.subtract_ori_invF)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 280, 261, 261))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ILPF = QtWidgets.QPushButton(self.layoutWidget2)
        self.ILPF.setObjectName("ILPF")
        self.horizontalLayout_3.addWidget(self.ILPF)
        self.GLPF = QtWidgets.QPushButton(self.layoutWidget2)
        self.GLPF.setObjectName("GLPF")
        self.horizontalLayout_3.addWidget(self.GLPF)
        self.BLPF = QtWidgets.QPushButton(self.layoutWidget2)
        self.BLPF.setObjectName("BLPF")
        self.horizontalLayout_3.addWidget(self.BLPF)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.IHPF = QtWidgets.QPushButton(self.layoutWidget2)
        self.IHPF.setObjectName("IHPF")
        self.horizontalLayout_4.addWidget(self.IHPF)
        self.GHPF = QtWidgets.QPushButton(self.layoutWidget2)
        self.GHPF.setObjectName("GHPF")
        self.horizontalLayout_4.addWidget(self.GHPF)
        self.BHPF = QtWidgets.QPushButton(self.layoutWidget2)
        self.BHPF.setObjectName("BHPF")
        self.horizontalLayout_4.addWidget(self.BHPF)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filter_image = QtWidgets.QLabel(self.layoutWidget2)
        self.filter_image.setObjectName("filter_image")
        self.horizontalLayout_2.addWidget(self.filter_image)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_3.addWidget(self.lineEdit_9)
        self.spinBox_filter = QtWidgets.QSpinBox(self.layoutWidget2)
        self.spinBox_filter.setProperty("value", 10)
        self.spinBox_filter.setObjectName("spinBox_filter")
        self.verticalLayout_3.addWidget(self.spinBox_filter)
        self.distance = QtWidgets.QSlider(self.layoutWidget2)
        self.distance.setProperty("value", 10)
        self.distance.setOrientation(QtCore.Qt.Vertical)
        self.distance.setObjectName("distance")
        self.verticalLayout_3.addWidget(self.distance)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.setStretch(0, 7)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.homo_button = QtWidgets.QPushButton(self.centralwidget)
        self.homo_button.setGeometry(QtCore.QRect(530, 520, 51, 23))
        self.homo_button.setObjectName("homo_button")
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(310, 290, 221, 251))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_6.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_6.addWidget(self.lineEdit_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gamma_h = QtWidgets.QDoubleSpinBox(self.layoutWidget3)
        self.gamma_h.setProperty("value", 3.0)
        self.gamma_h.setObjectName("gamma_h")
        self.horizontalLayout_5.addWidget(self.gamma_h)
        self.gamma_l = QtWidgets.QDoubleSpinBox(self.layoutWidget3)
        self.gamma_l.setProperty("value", 0.4)
        self.gamma_l.setObjectName("gamma_l")
        self.horizontalLayout_5.addWidget(self.gamma_l)
        self.d0 = QtWidgets.QDoubleSpinBox(self.layoutWidget3)
        self.d0.setProperty("value", 20.0)
        self.d0.setObjectName("d0")
        self.horizontalLayout_5.addWidget(self.d0)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.homohorphic = QtWidgets.QLabel(self.layoutWidget3)
        self.homohorphic.setObjectName("homohorphic")
        self.verticalLayout_4.addWidget(self.homohorphic)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 9)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(580, 290, 241, 251))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.blur = QtWidgets.QPushButton(self.layoutWidget4)
        self.blur.setObjectName("blur")
        self.horizontalLayout_7.addWidget(self.blur)
        self.wiener = QtWidgets.QPushButton(self.layoutWidget4)
        self.wiener.setObjectName("wiener")
        self.horizontalLayout_7.addWidget(self.wiener)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.inverse = QtWidgets.QPushButton(self.layoutWidget4)
        self.inverse.setObjectName("inverse")
        self.horizontalLayout_8.addWidget(self.inverse)
        self.subtract_wie_inv = QtWidgets.QPushButton(self.layoutWidget4)
        self.subtract_wie_inv.setObjectName("subtract_wie_inv")
        self.horizontalLayout_8.addWidget(self.subtract_wie_inv)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.motion_blur = QtWidgets.QLabel(self.layoutWidget4)
        self.motion_blur.setObjectName("motion_blur")
        self.verticalLayout_5.addWidget(self.motion_blur)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(2, 9)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(830, 290, 271, 251))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.blur_n = QtWidgets.QPushButton(self.layoutWidget_2)
        self.blur_n.setObjectName("blur_n")
        self.horizontalLayout_9.addWidget(self.blur_n)
        self.wiener_n = QtWidgets.QPushButton(self.layoutWidget_2)
        self.wiener_n.setObjectName("wiener_n")
        self.horizontalLayout_9.addWidget(self.wiener_n)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.inverse_n = QtWidgets.QPushButton(self.layoutWidget_2)
        self.inverse_n.setObjectName("inverse_n")
        self.horizontalLayout_10.addWidget(self.inverse_n)
        self.subtract_wie_inv_n = QtWidgets.QPushButton(self.layoutWidget_2)
        self.subtract_wie_inv_n.setObjectName("subtract_wie_inv_n")
        self.horizontalLayout_10.addWidget(self.subtract_wie_inv_n)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.motion_blur_n = QtWidgets.QLabel(self.layoutWidget_2)
        self.motion_blur_n.setObjectName("motion_blur_n")
        self.horizontalLayout_11.addWidget(self.motion_blur_n)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_7.addWidget(self.lineEdit_4)
        self.spinBox_sigma = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.spinBox_sigma.setPrefix("")
        self.spinBox_sigma.setMinimum(1)
        self.spinBox_sigma.setMaximum(9999999)
        self.spinBox_sigma.setProperty("value", 20)
        self.spinBox_sigma.setObjectName("spinBox_sigma")
        self.verticalLayout_7.addWidget(self.spinBox_sigma)
        self.verticalSlider_sigma = QtWidgets.QSlider(self.layoutWidget_2)
        self.verticalSlider_sigma.setMinimum(1)
        self.verticalSlider_sigma.setMaximum(9999999)
        self.verticalSlider_sigma.setPageStep(1)
        self.verticalSlider_sigma.setProperty("value", 20)
        self.verticalSlider_sigma.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_sigma.setObjectName("verticalSlider_sigma")
        self.verticalLayout_7.addWidget(self.verticalSlider_sigma)
        self.horizontalLayout_11.addLayout(self.verticalLayout_7)
        self.horizontalLayout_11.setStretch(0, 9)
        self.horizontalLayout_11.setStretch(1, 1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_6.setStretch(2, 11)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1118, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.distance.valueChanged['int'].connect(self.spinBox_filter.setValue) # type: ignore
        self.spinBox_filter.valueChanged['int'].connect(self.distance.setValue) # type: ignore
        self.verticalSlider_sigma.valueChanged['int'].connect(self.spinBox_sigma.setValue) # type: ignore
        self.spinBox_sigma.valueChanged['int'].connect(self.verticalSlider_sigma.setValue) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.origin_label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_select.setText(_translate("MainWindow", "PushButton"))
        self.lineEdit_5.setText(_translate("MainWindow", "spectrum"))
        self.spectrum.setText(_translate("MainWindow", "TextLabel"))
        self.lineEdit_6.setText(_translate("MainWindow", "phase angle"))
        self.phase_angle.setText(_translate("MainWindow", "TextLabel"))
        self.lineEdit_7.setText(_translate("MainWindow", "inverse fourier"))
        self.inv_fourier.setText(_translate("MainWindow", "TextLabel"))
        self.lineEdit_8.setText(_translate("MainWindow", "subtract(origin,processed)"))
        self.subtract_ori_invF.setText(_translate("MainWindow", "TextLabel"))
        self.ILPF.setText(_translate("MainWindow", "ILPF"))
        self.GLPF.setText(_translate("MainWindow", "GLPF"))
        self.BLPF.setText(_translate("MainWindow", "BLPF"))
        self.IHPF.setText(_translate("MainWindow", "IHPF"))
        self.GHPF.setText(_translate("MainWindow", "GHPF"))
        self.BHPF.setText(_translate("MainWindow", "BHPF"))
        self.filter_image.setText(_translate("MainWindow", "TextLabel"))
        self.lineEdit_9.setText(_translate("MainWindow", "D0"))
        self.homo_button.setText(_translate("MainWindow", "click"))
        self.lineEdit.setText(_translate("MainWindow", "gamma_h"))
        self.lineEdit_2.setText(_translate("MainWindow", "gamma_l"))
        self.lineEdit_3.setText(_translate("MainWindow", "D0"))
        self.homohorphic.setText(_translate("MainWindow", "TextLabel"))
        self.blur.setText(_translate("MainWindow", "blur"))
        self.wiener.setText(_translate("MainWindow", "wiener"))
        self.inverse.setText(_translate("MainWindow", "inverse"))
        self.subtract_wie_inv.setText(_translate("MainWindow", "subtract_wie_inv"))
        self.motion_blur.setText(_translate("MainWindow", "motion_blur"))
        self.blur_n.setText(_translate("MainWindow", "blur"))
        self.wiener_n.setText(_translate("MainWindow", "wiener"))
        self.inverse_n.setText(_translate("MainWindow", "inverse"))
        self.subtract_wie_inv_n.setText(_translate("MainWindow", "subtract_wie_inv"))
        self.motion_blur_n.setText(_translate("MainWindow", "motion_blur + noise"))
        self.lineEdit_4.setText(_translate("MainWindow", "sigma"))

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.Noise = None
        self.m_n = None
        self.H = None
        self.motion_blur = None
        self.fshift = None
        self.setupUi(self)
        self.img = None
        self.img_path = None
        self.pushButton_select.clicked.connect(self.select_pic_Clicked)
        self.ILPF.clicked.connect(self.ilpf_clicked)
        self.IHPF.clicked.connect(self.ihpf_clicked)
        self.GLPF.clicked.connect(self.glpf_clicked)
        self.GHPF.clicked.connect(self.ghpf_clicked)
        self.BHPF.clicked.connect(self.bhpf_clicked)
        self.BLPF.clicked.connect(self.blpf_clicked)
        self.homo_button.clicked.connect(self.homo_button_clicked)
        self.blur.clicked.connect(self.blur_clicked)
        self.wiener.clicked.connect(self.wiener_clicked)
        self.inverse.clicked.connect(self.inverse_clicked)
        self.subtract_wie_inv.clicked.connect(self.subtract_wie_inv_clicked)
        self.wiener_n.clicked.connect(self.wiener_n_clicked)
        self.blur_n.clicked.connect(self.blur_n_clicked)
        self.inverse_n.clicked.connect(self.inverse_n_clicked)
        self.subtract_wie_inv_n.clicked.connect(self.subtract_wie_inv_n_clicked)
        self.spinBox_sigma.valueChanged.connect((self.verticalSlider_sigma.sliderReleased))
        self.verticalSlider_sigma.sliderReleased.connect(self.motion_blur_img_n)

    def select_pic_Clicked(self):
        # 開啟資料夾選則照片
        self.img_path, _ = QFileDialog.getOpenFileName(self,
                                                       "Open file",
                                                       "./",
                                                       "Images (*.png *.BMP *.jpg *.JPG)")

        self.img = cv2.imread(self.img_path)  # 讀檔

        height, width, channel = self.img.shape
        qimg = QImage(self.img, width, height, 3 * width, QImage.Format_RGB888).rgbSwapped()
        self.origin_label.setPixmap(QPixmap.fromImage(qimg))
        self.origin_label.setScaledContents(True)
        # 取灰階圖
        self.gray = np.zeros((self.img.shape[0], self.img.shape[1]), np.uint8)
        for i in range(self.gray.shape[0]):
            for j in range(self.gray.shape[1]):
                self.gray[i, j] = np.mean(self.img[i, j, :])
        self.fourier_transform()
        self.inv_fourier_transform()
        self.motion_blur_img()
        self.motion_blur_img_n()

    def fourier_transform(self):
        t0 = time.time()
        fnew = np.zeros_like(self.gray, np.uint8)
        phase_new = np.zeros_like(self.gray, np.uint8)

        f = np.fft.fft2(self.gray)  # fourier transform

        self.fshift = np.fft.fftshift(f)  # shift to center
        t1 = time.time()
        fimg = np.log(np.abs(self.fshift) + 1)

        fmin = np.log(1 + abs(np.min(fimg)))
        fmax = np.log(1 + abs(np.max(fimg)))

        phase_spectrum = np.angle(self.fshift, deg=True)  # get phase angle

        for i in range(fnew.shape[0]):  # let image get better display
            for j in range(fnew.shape[1]):
                fnew[i, j] = 255 * (np.log(1 + abs(fimg[i, j])) - fmin) / (fmax - fmin)

                if phase_spectrum[i, j] < 0:
                    phase_new[i, j] = (phase_spectrum[i, j] + 360) * (255 / 360)
                elif phase_spectrum[i, j] > 255:
                    phase_new[i, j] = (phase_spectrum[i, j]) * (255 / 360)

        self.f_time.setText("fourier time: %.5f" % (t1 - t0))
        qimg = QImage(fnew.data, fnew.shape[1], fnew.shape[0], QImage.Format_Grayscale8)
        qimg2 = QImage(phase_new.data, phase_new.shape[1], phase_new.shape[0], QImage.Format_Grayscale8)
        self.spectrum.setPixmap(QPixmap.fromImage(qimg))
        self.spectrum.setScaledContents(True)
        self.phase_angle.setPixmap(QPixmap.fromImage(qimg2))
        self.phase_angle.setScaledContents(True)

    def inv_fourier_transform(self):
        t0 = time.time()
        self.f_ishift = np.fft.ifftshift(self.fshift)  # shift fourier image rom center to origin vector
        img_back = np.fft.ifft2(self.f_ishift)  # inverse fourier
        t1 = time.time()
        img_back = abs(img_back)
        new_back = np.array(img_back.copy(), np.uint8)

        self.subtract(new_back)  # subtract origin image from new_back
        self.if_time.setText("inv fourier time: %.5f" % (t1 - t0))
        qimg = QImage(new_back.data, new_back.shape[1], new_back.shape[0], QImage.Format_Grayscale8)

        self.inv_fourier.setPixmap(QPixmap.fromImage(qimg))
        self.inv_fourier.setScaledContents(True)

    def subtract(self, new):  # subtract new image from origin grayscale image
        img = np.abs(self.gray - new)
        img *= 255
        qimg = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_Grayscale8)

        self.subtract_ori_invF.setPixmap(QPixmap.fromImage(qimg))
        self.subtract_ori_invF.setScaledContents(True)

    def ilpf_clicked(self):  # show ilpf processed image
        print("start..")
        value = self.distance.value()
        img = np.array(self.fshift)

        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                d = ((i - img.shape[0] / 2) ** 2 + (j - img.shape[1] / 2) ** 2) ** 0.5

                if d <= value:
                    continue

                else:
                    img[i, j] = 0

        img_back = np.fft.ifft2(img)  # inv fourier transform

        img_back = abs(img_back)
        new_back = np.array(img_back.copy(), np.uint8)

        qimg = QImage(new_back.data, new_back.shape[1], new_back.shape[0], QImage.Format_Grayscale8)

        self.filter_image.setPixmap(QPixmap.fromImage(qimg))
        self.filter_image.setScaledContents(True)
        print("finish..")

    def glpf_clicked(self):  # show glpf processed image
        print("start..")
        value = self.distance.value()
        img = np.zeros_like(self.fshift)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                d = ((i - img.shape[0] / 2) ** 2 + (j - img.shape[1] / 2) ** 2) ** 0.5
                img[i, j] = np.exp((-d ** 2) / (2 * value ** 2)) * self.fshift[i, j]

        img_back = np.fft.ifft2(img)

        img_back = abs(img_back)
        new_back = np.array(img_back.copy(), np.uint8)

        qimg = QImage(new_back.data, new_back.shape[1], new_back.shape[0], QImage.Format_Grayscale8)

        self.filter_image.setPixmap(QPixmap.fromImage(qimg))
        self.filter_image.setScaledContents(True)
        print("finish..")

    def blpf_clicked(self):  # show blpf processed image
        print("start..")
        value = self.distance.value()
        img = np.zeros_like(self.fshift)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                d = ((i - img.shape[0] / 2) ** 2 + (j - img.shape[1] / 2) ** 2) ** 0.5
                img[i, j] = 1 / (1 + (d / value) ** (2 * 2.25)) * self.fshift[i, j]

        img_back = np.fft.ifft2(img)  # inv fourier transform

        img_back = abs(img_back)
        new_back = np.array(img_back.copy(), np.uint8)

        qimg = QImage(new_back.data, new_back.shape[1], new_back.shape[0], QImage.Format_Grayscale8)

        self.filter_image.setPixmap(QPixmap.fromImage(qimg))
        self.filter_image.setScaledContents(True)
        print("finish..")

    def ihpf_clicked(self):  # show ihpf processed image
        print("start..")
        value = self.distance.value()
        img = np.zeros_like(self.fshift)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                d = ((i - img.shape[0] / 2) ** 2 + (j - img.shape[1] / 2) ** 2) ** 0.5
                if d >= value:
                    img[i, j] = self.fshift[i, j]
                else:
                    img[i, j] = 0
        img_back = np.fft.ifft2(img)  # inv fourier transform

        img_back = abs(img_back)
        new_back = np.array(img_back.copy(), np.uint8)

        qimg = QImage(new_back.data, new_back.shape[1], new_back.shape[0], QImage.Format_Grayscale8)

        self.filter_image.setPixmap(QPixmap.fromImage(qimg))
        self.filter_image.setScaledContents(True)
        print("finish..")

    def ghpf_clicked(self):  # show ghpf processed image
        print("start..")
        value = self.distance.value()
        # fimg = np.log(np.abs(self.fshift))
        img = np.zeros_like(self.fshift)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                d = ((i - img.shape[0] / 2) ** 2 + (j - img.shape[1] / 2) ** 2) ** 0.5
                img[i, j] = (1 - np.exp((-d ** 2) / (2 * value ** 2))) * self.fshift[i, j]

        img_back = np.fft.ifft2(img)  # inv fourier transform

        img_back = abs(img_back)
        new_back = np.array(img_back.copy(), np.uint8)

        qimg = QImage(new_back.data, new_back.shape[1], new_back.shape[0], QImage.Format_Grayscale8)

        self.filter_image.setPixmap(QPixmap.fromImage(qimg))
        self.filter_image.setScaledContents(True)
        print("finish..")

    def bhpf_clicked(self):  # show bhpf processed image
        print("start..")

        value = self.distance.value()
        img = np.zeros_like(self.fshift)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                d = ((i - img.shape[0] / 2) ** 2 + (j - img.shape[1] / 2) ** 2) ** 0.5 + 0.0001
                img[i, j] = 1 / (1 + (value / d) ** (2 * 2.25)) * self.fshift[i, j]

        img_back = np.fft.ifft2(img)  # inv fourier transform

        img_back = abs(img_back)
        # print(img_back)
        new_back = np.array(img_back.copy(), np.uint8)

        qimg = QImage(new_back.data, new_back.shape[1], new_back.shape[0], QImage.Format_Grayscale8)

        self.filter_image.setPixmap(QPixmap.fromImage(qimg))
        self.filter_image.setScaledContents(True)
        print("finish..")

    def homo_button_clicked(self):  # implement homography
        print("waitimg..")
        gamma_l = self.gamma_l.value()
        gamma_h = self.gamma_h.value()
        d0 = self.d0.value()
        c = 5
        # print(np.min(self.gray))
        log = np.log(self.gray + 0.000001)  # log(gray image)
        f = np.fft.fft2(log)  # fourier transform
        filter_img = np.zeros_like(f)
        for i in range(f.shape[0]):  # make filtered_image
            for j in range(f.shape[1]):
                d = ((i - f.shape[0] / 2) ** 2 + (j - f.shape[1] / 2) ** 2) ** 0.5
                filter_img[i, j] = f[i, j] * ((gamma_h - gamma_l) * (1 - np.exp(-c * d ** 2 / d0 ** 2)) + gamma_l)

        iff = np.fft.ifft2(filter_img)  # inv fourier transform
        exp = np.exp(iff)
        exp = np.array(abs(exp).copy(), np.uint8)

        qimg = QImage(exp.data, exp.shape[1], exp.shape[0], QImage.Format_Grayscale8)
        self.homohorphic.setPixmap(QPixmap.fromImage(qimg))
        self.homohorphic.setScaledContents(True)
        print("finish..")

    def motion_blur_img(self):  # motion blur image
        img = self.gray / np.max(self.gray)  # normalize grayscale image
        img = np.fft.fft2(img)  # fourier transform

        H = np.zeros((self.gray.shape[0] + 1, self.gray.shape[1] + 1), dtype=np.complex128)  # shape +1 to avoid u,v=0
        T = 1
        a = 0.1
        b = 0.1
        for i in range(1, H.shape[0]):  # get H(u,v)
            for j in range(1, H.shape[1]):
                s = np.pi * (a * i + j * b)
                H[i, j] = (T / s) * np.sin(s) * np.exp(-1j * s)

        self.H = H[1:, 1:]
        self.m = self.H * img

    def blur_clicked(self):  # ahow blur image
        img_back = np.fft.ifft2(self.m)
        img_back = np.abs(img_back) * 255 / np.max(np.abs(img_back))
        new_back = np.array(img_back.copy(), np.uint8)
        qimg = QImage(new_back.data, new_back.shape[1], new_back.shape[0], new_back.shape[1], QImage.Format_Grayscale8)
        self.motion_blur.setPixmap(QPixmap.fromImage(qimg))
        self.motion_blur.setScaledContents(True)

    def wiener_filter(self, S_n=False):  # make wiener filter
        if S_n:
            S_f = np.abs(self.fshift)
            S_n = self.Noise
            K = np.abs(S_n) ** 2 / S_f ** 2
            filter = (1 / self.H) * (np.power(np.abs(self.H), 2) / (np.power(np.abs(self.H), 2) + K))
        else:

            filter = (1 / self.H)
        return filter

    def inverse_filter(self):  # make inverse filter
        H_star = np.conjugate(self.H)
        filter = H_star / np.power(np.abs(self.H), 2)
        return filter

    def wiener_clicked(self):  # show wiener image(without noise
        F_hat = self.wiener_filter() * self.m
        f_hat = np.fft.ifft2(F_hat)
        f_hat = np.abs(f_hat) * 255 / np.max(np.abs(f_hat))
        out = np.array(np.abs(f_hat.copy()), np.uint8)
        qimg = QImage(out.data, out.shape[1], out.shape[0], out.shape[1], QImage.Format_Grayscale8)

        self.motion_blur.setPixmap(QPixmap.fromImage(qimg))
        self.motion_blur.setScaledContents(True)

    def inverse_clicked(self):  # show inverse filter image(without noise
        F_hat = self.inverse_filter() * self.m
        f_hat = np.fft.ifft2(F_hat)
        f_hat = np.abs(f_hat) * 255 / np.max(np.abs(f_hat))
        out = np.array(np.abs(f_hat.copy()), np.uint8)
        qimg = QImage(out.data, out.shape[1], out.shape[0], out.shape[1], QImage.Format_Grayscale8)

        self.motion_blur.setPixmap(QPixmap.fromImage(qimg))
        self.motion_blur.setScaledContents(True)

    def subtract_wie_inv_clicked(self):  # show subtraction image
        F_hat = self.wiener_filter() * self.m
        f_hat = np.fft.ifft2(F_hat)
        f_hat = np.abs(f_hat) * 255 / np.max(np.abs(f_hat))
        out1 = np.array(np.abs(f_hat.copy()), np.uint8)
        F_hat = self.inverse_filter() * self.m
        f_hat = np.fft.ifft2(F_hat)
        f_hat = np.abs(f_hat) * 255 / np.max(np.abs(f_hat))
        out2 = np.array(np.abs(f_hat.copy()), np.uint8)
        out = np.array(np.abs(out1 - out2), np.uint8)
        qimg = QImage(out.data, out.shape[1], out.shape[0], out.shape[1], QImage.Format_Grayscale8)

        self.motion_blur.setPixmap(QPixmap.fromImage(qimg))
        self.motion_blur.setScaledContents(True)

    def gaussion_noise(self):  # make gaussian noise
        sigma = self.spinBox_sigma.value()
        z = np.random.rand(self.img.shape[0], self.img.shape[1])
        n = np.zeros_like(z)
        for i in range(z.shape[0]):
            for j in range(z.shape[1]):
                n[i, j] = 1 * np.exp(-1 * z[i, j] ** 2 / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
        self.Noise = np.fft.fft2(n)

    def motion_blur_img_n(self):  # blur image with noise
        self.gaussion_noise()
        self.m_n = self.m + self.Noise

    def blur_n_clicked(self):  # show blur image with noise

        img_back = np.fft.ifft2(self.m_n)
        img_back = np.abs(img_back) * 255 / np.max(np.abs(img_back))
        new_back = np.array(img_back.copy(), np.uint8)
        # print(new_back)
        qimg = QImage(new_back.data, new_back.shape[1], new_back.shape[0], new_back.shape[1], QImage.Format_Grayscale8)
        self.motion_blur_n.setPixmap(QPixmap.fromImage(qimg))
        self.motion_blur_n.setScaledContents(True)

    def wiener_n_clicked(self):  # show winer image with noise
        F_hat = self.wiener_filter(True) * self.m_n
        f_hat = np.fft.ifft2(F_hat)
        f_hat = np.abs(f_hat) * 255 / np.max(np.abs(f_hat))
        # print(f_hat)
        out = np.array(f_hat.copy(), np.uint8)
        qimg = QImage(out.data, out.shape[1], out.shape[0], out.shape[1], QImage.Format_Grayscale8)

        self.motion_blur_n.setPixmap(QPixmap.fromImage(qimg))
        self.motion_blur_n.setScaledContents(True)

    def inverse_n_clicked(self):  # show inv filter image with noise
        F_hat = self.inverse_filter() * self.m_n
        f_hat = np.fft.ifft2(F_hat)
        f_hat = np.abs(f_hat) * 255 / np.max(np.abs(f_hat))
        out = np.array(np.abs(f_hat.copy()), np.uint8)
        qimg = QImage(out.data, out.shape[1], out.shape[0], out.shape[1], QImage.Format_Grayscale8)

        self.motion_blur_n.setPixmap(QPixmap.fromImage(qimg))
        self.motion_blur_n.setScaledContents(True)

    def subtract_wie_inv_n_clicked(self):  # subtraction image with noise
        F_hat = self.wiener_filter(True) * self.m_n
        f_hat = np.fft.ifft2(F_hat)
        f_hat = np.abs(f_hat) * 255 / np.max(np.abs(f_hat))
        out1 = np.array(np.abs(f_hat.copy()), np.uint8)

        F_hat = self.inverse_filter() * self.m_n
        f_hat = np.fft.ifft2(F_hat)
        f_hat = np.abs(f_hat) * 255 / np.max(np.abs(f_hat))
        out2 = np.array(np.abs(f_hat.copy()), np.uint8)

        out = np.array(np.abs(out1 - out2), np.uint8)
        qimg = QImage(out.data, out.shape[1], out.shape[0], out.shape[1], QImage.Format_Grayscale8)

        self.motion_blur_n.setPixmap(QPixmap.fromImage(qimg))
        self.motion_blur_n.setScaledContents(True)
if __name__ == '__main__':
    app = QApplication([])
    w = MainWindow()
    w.show()
    app.exec()
