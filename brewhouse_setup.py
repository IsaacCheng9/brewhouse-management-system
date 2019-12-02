# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'brewhouse.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mwindow_brewhouse(object):
    def setupUi(self, mwindow_brewhouse):
        mwindow_brewhouse.setObjectName("mwindow_brewhouse")
        mwindow_brewhouse.resize(960, 720)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        mwindow_brewhouse.setFont(font)
        self.central_widget = QtWidgets.QWidget(mwindow_brewhouse)
        self.central_widget.setObjectName("central_widget")
        self.layoutWidget = QtWidgets.QWidget(self.central_widget)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 289, 309))
        self.layoutWidget.setObjectName("layoutWidget")
        self.vert_layout_brewhouse = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.vert_layout_brewhouse.setContentsMargins(0, 0, 0, 0)
        self.vert_layout_brewhouse.setObjectName("vert_layout_brewhouse")
        self.lbl_brewhouse = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_brewhouse.setFont(font)
        self.lbl_brewhouse.setObjectName("lbl_brewhouse")
        self.vert_layout_brewhouse.addWidget(self.lbl_brewhouse)
        self.hori_line_brewhouse = QtWidgets.QFrame(self.layoutWidget)
        self.hori_line_brewhouse.setFrameShape(QtWidgets.QFrame.HLine)
        self.hori_line_brewhouse.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hori_line_brewhouse.setObjectName("hori_line_brewhouse")
        self.vert_layout_brewhouse.addWidget(self.hori_line_brewhouse)
        self.hori_layout_nav = QtWidgets.QHBoxLayout()
        self.hori_layout_nav.setObjectName("hori_layout_nav")
        self.btn_predict = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_predict.setObjectName("btn_predict")
        self.hori_layout_nav.addWidget(self.btn_predict)
        self.btn_process_monitoring = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_process_monitoring.setObjectName("btn_process_monitoring")
        self.hori_layout_nav.addWidget(self.btn_process_monitoring)
        self.vert_layout_brewhouse.addLayout(self.hori_layout_nav)
        self.hori_line_nav = QtWidgets.QFrame(self.layoutWidget)
        self.hori_line_nav.setFrameShape(QtWidgets.QFrame.HLine)
        self.hori_line_nav.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hori_line_nav.setObjectName("hori_line_nav")
        self.vert_layout_brewhouse.addWidget(self.hori_line_nav)
        self.lbl_ratios = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lbl_ratios.setFont(font)
        self.lbl_ratios.setObjectName("lbl_ratios")
        self.vert_layout_brewhouse.addWidget(self.lbl_ratios)
        self.lbl_red_helles_ratio = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_red_helles_ratio.setObjectName("lbl_red_helles_ratio")
        self.vert_layout_brewhouse.addWidget(self.lbl_red_helles_ratio)
        self.lbl_pilsner_ratio = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_pilsner_ratio.setObjectName("lbl_pilsner_ratio")
        self.vert_layout_brewhouse.addWidget(self.lbl_pilsner_ratio)
        self.lbl_dunkel_ratio = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_dunkel_ratio.setObjectName("lbl_dunkel_ratio")
        self.vert_layout_brewhouse.addWidget(self.lbl_dunkel_ratio)
        self.hori_line_ratios = QtWidgets.QFrame(self.layoutWidget)
        self.hori_line_ratios.setFrameShape(QtWidgets.QFrame.HLine)
        self.hori_line_ratios.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hori_line_ratios.setObjectName("hori_line_ratios")
        self.vert_layout_brewhouse.addWidget(self.hori_line_ratios)
        self.lbl_growth = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lbl_growth.setFont(font)
        self.lbl_growth.setObjectName("lbl_growth")
        self.vert_layout_brewhouse.addWidget(self.lbl_growth)
        self.lbl_red_helles_growth = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_red_helles_growth.setObjectName("lbl_red_helles_growth")
        self.vert_layout_brewhouse.addWidget(self.lbl_red_helles_growth)
        self.lbl_pilsner_growth = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_pilsner_growth.setObjectName("lbl_pilsner_growth")
        self.vert_layout_brewhouse.addWidget(self.lbl_pilsner_growth)
        self.lbl_dunkel_growth = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_dunkel_growth.setObjectName("lbl_dunkel_growth")
        self.vert_layout_brewhouse.addWidget(self.lbl_dunkel_growth)
        mwindow_brewhouse.setCentralWidget(self.central_widget)
        self.status_bar = QtWidgets.QStatusBar(mwindow_brewhouse)
        self.status_bar.setObjectName("status_bar")
        mwindow_brewhouse.setStatusBar(self.status_bar)

        self.retranslateUi(mwindow_brewhouse)
        QtCore.QMetaObject.connectSlotsByName(mwindow_brewhouse)

    def retranslateUi(self, mwindow_brewhouse):
        _translate = QtCore.QCoreApplication.translate
        mwindow_brewhouse.setWindowTitle(
            _translate("mwindow_brewhouse", "MainWindow"))
        self.lbl_brewhouse.setText(_translate(
            "mwindow_brewhouse", "Barnaby\'s Brewhouse"))
        self.btn_predict.setText(_translate(
            "mwindow_brewhouse", "Predict Sales"))
        self.btn_process_monitoring.setText(_translate(
            "mwindow_brewhouse", "Process Monitoring"))
        self.lbl_ratios.setText(_translate(
            "mwindow_brewhouse", "Sales Ratios"))
        self.lbl_red_helles_ratio.setText(_translate(
            "mwindow_brewhouse", "Organic Red Helles - "))
        self.lbl_pilsner_ratio.setText(_translate(
            "mwindow_brewhouse", "Organic Pilsner - "))
        self.lbl_dunkel_ratio.setText(_translate(
            "mwindow_brewhouse", "Organic Dunkel - "))
        self.lbl_growth.setText(_translate(
            "mwindow_brewhouse", "Average Monthly Growth Percentages"))
        self.lbl_red_helles_growth.setText(_translate(
            "mwindow_brewhouse", "Organic Red Helles - "))
        self.lbl_pilsner_growth.setText(_translate(
            "mwindow_brewhouse", "Organic Pilsner  - "))
        self.lbl_dunkel_growth.setText(_translate(
            "mwindow_brewhouse", "Organic Dunkel - "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mwindow_brewhouse = QtWidgets.QMainWindow()
    ui = Ui_mwindow_brewhouse()
    ui.setupUi(mwindow_brewhouse)
    mwindow_brewhouse.show()
    sys.exit(app.exec_())
