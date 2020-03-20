from PyQt5 import QtCore, QtWidgets


class MainWindowGui(object):

    def setup(self, main_window):
        main_window.resize(480, 150)
        main_window.setMinimumSize(QtCore.QSize(480, 150))

        menu_bar = QtWidgets.QMenuBar(main_window)
        menu_bar.setGeometry(QtCore.QRect(0, 0, 240, 26))
        main_window.setMenuBar(menu_bar)

        status_bar = QtWidgets.QStatusBar(main_window)
        main_window.setStatusBar(status_bar)

        central_widget = QtWidgets.QWidget(main_window)

        vertical_layout = QtWidgets.QVBoxLayout(central_widget)

        h_layout = QtWidgets.QHBoxLayout()

        v_layout = QtWidgets.QVBoxLayout()
        self.file1_button = QtWidgets.QPushButton(central_widget)
        v_layout.addWidget(self.file1_button)

        self.file1_label = QtWidgets.QLabel(central_widget)
        self.file1_label.setAlignment(QtCore.Qt.AlignCenter)
        v_layout.addWidget(self.file1_label)

        h_layout.addLayout(v_layout)

        v_layout = QtWidgets.QVBoxLayout()
        self.file2_button = QtWidgets.QPushButton(central_widget)
        v_layout.addWidget(self.file2_button)

        self.file2_label = QtWidgets.QLabel(central_widget)
        self.file2_label.setAlignment(QtCore.Qt.AlignCenter)
        v_layout.addWidget(self.file2_label)

        h_layout.addLayout(v_layout)
        vertical_layout.addLayout(h_layout)

        h_layout = QtWidgets.QHBoxLayout(main_window)
        self.compare_button = QtWidgets.QPushButton(central_widget)
        self.compare_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        h_layout.addWidget(self.compare_button)
        vertical_layout.addLayout(h_layout)

        main_window.setCentralWidget(central_widget)

        self.translate(main_window)

    def translate(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate('MainWindow', 'File Comparator'))
        self.file1_button.setText(_translate('File1Button', 'Select first file'))
        self.file2_button.setText(_translate('File2Button', 'Select second file'))
        self.compare_button.setText(_translate('CompareButton', 'Compare files'))

    def binary_result(self, info):
        QtWidgets.QMessageBox.about(self, 'Binary comparing result', info)

    def text_comparing_result(self, name1, name2, text1, text2):
        dialog = QtWidgets.QDialog(parent=self)
        dialog.setMinimumSize(QtCore.QSize(480, 150))

        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel()
        label.setText(name1)
        label.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(label)

        label = QtWidgets.QLabel()
        label.setText(name2)
        label.setAlignment(QtCore.Qt.AlignCenter)
        hbox.addWidget(label)
        vbox.addLayout(hbox)

        hbox = QtWidgets.QHBoxLayout()
        text1_edit = QtWidgets.QTextEdit()
        text1_edit.setText(text1)
        text1_edit.setReadOnly(True)
        hbox.addWidget(text1_edit)

        text2_edit = QtWidgets.QTextEdit()
        text2_edit.setText(text2)
        text2_edit.setReadOnly(True)
        hbox.addWidget(text2_edit)
        vbox.addLayout(hbox)

        ok_button = QtWidgets.QPushButton('Ok')
        ok_button.setFocus(False)
        vbox.addWidget(ok_button)

        dialog.setLayout(vbox)
        dialog.setWindowTitle('Text comparing result')
        dialog.show()

        ok_button.clicked.connect(dialog.close)



def pick_file_dialog():
    name = QtWidgets.QFileDialog.getOpenFileName()
    if name[0] == '':
        return None

    return name[0]
