from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QFileDialog, QStackedWidget
from pathlib import Path
from structures.logcat_dict import LogcatDict


class Layout:
    _name = "Logcat Reader"
    app = QApplication([])
    window = QWidget()
    search_label = QLabel("")
    result_label = QLabel("")
    button_layout = QHBoxLayout()
    yes_btn = QPushButton("Yes :D")
    no_btn = QPushButton("No :c")
    search_layout = QVBoxLayout()
    result_layout = QVBoxLayout()
    stack = QStackedWidget()
    path: Path

    def __init__(self):
        self.window.setWindowTitle(self._name)
        self.set_search_layout()
        self.set_result_layout()
        search_stack = QWidget()
        search_stack.setLayout(self.search_layout)
        self.stack.addWidget(search_stack)
        result_stack = QWidget()
        result_stack.setLayout(self.result_layout)
        self.stack.addWidget(result_stack)
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.window.setLayout(layout)

    def set_search_layout(self):
        self.search_layout.addWidget(self.search_label)
        self.button_layout.addWidget(self.yes_btn)
        self.button_layout.addWidget(self.no_btn)
        self.yes_btn.clicked.connect(self.on_select_yes)
        self.no_btn.clicked.connect(self.on_select_no)
        self.search_layout.addLayout(self.button_layout)

    def set_result_layout(self):
        self.result_layout.addWidget(self.result_label)

    def on_select_yes(self):
        logcat_dict = LogcatDict(self.path)
        new_name = logcat_dict.print_lines(self.path)
        self.result_label.setText(f"The formatted file was created in the same directory with the name: {new_name}")
        self.stack.setCurrentIndex(1)

    def on_select_no(self):
        self.select_file()

    def select_file(self):
        file_name = QFileDialog.getOpenFileName(self.window, "Read File")
        self.path = Path(file_name[0])
        self.search_label.setText(f"You are going to format the following file {self.path.name}, are you sure?")

    def start(self):
        self.select_file()
        self.window.show()
        self.app.exec()
