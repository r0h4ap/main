from binaryornot.check import is_binary
import os.path
from window import *
from bincomp import BinaryComparator
from textcomp import TextComparator


class Window(QtWidgets.QMainWindow, MainWindowGui):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setup(self)

        self.file1_name = None
        self.file2_name = None

        self.file1_button.clicked.connect(self.pick_first_file)
        self.file2_button.clicked.connect(self.pick_second_file)
        self.compare_button.clicked.connect(self.compare_files)

    def pick_first_file(self):
        self.file1_name = pick_file_dialog()

        if self.file1_name is not None:
            self.file1_label.setText(os.path.basename(self.file1_name))

    def pick_second_file(self):
        self.file2_name = pick_file_dialog()

        if self.file2_name is not None:
            self.file2_label.setText(os.path.basename(self.file2_name))

    def compare_files(self):
        if self.file1_name is None or self.file2_name is None or not os.path.exists(self.file1_name) or not os.path.exists(self.file2_name):
            print('Unnable to compare this objects')
            return

        file1_is_binary = is_binary(self.file1_name)
        line = 'First file is ' + ('binary' if file1_is_binary else 'text')
        print(line)

        file2_is_binary = is_binary(self.file2_name)
        line = 'Second file is ' + ('binary' if file2_is_binary else 'text')
        print(line)

        if file1_is_binary != file2_is_binary:
            print('Unnable to compare text and binary files')
            return

        if file1_is_binary and file2_is_binary:
            comparator = BinaryComparator(self.file1_name, self.file2_name)
            result = comparator.compare()

            if result:
                text = "<span style=\"font-size:14pt; font-weight:600; color:green;\">Files is indentical</span>"
                w.binary_result(text)
            else:
                text = "<span style=\"font-size:14pt; font-weight:600; color:red;\">Binary files didn't converge in {:0.4f}%</span>"
                w.binary_result(text.format(comparator.failed_percent))
        else:
            comparator = TextComparator(self.file1_name, self.file2_name)
            result1, result2 = comparator.compare()
            w.text_comparing_result(os.path.basename(self.file1_name), os.path.basename(self.file2_name), result1, result2)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    import sys

    sys.excepthook = except_hook

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())