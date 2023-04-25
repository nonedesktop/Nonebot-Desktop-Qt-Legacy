# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
import nonebot_desktop_wing as wing
from subprocess import PIPE, STDOUT, Popen

# import time
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui import UI
from create_project import Ui_NewProject as CP
from terminal_page import Ui_terminal_page as TP
from help_pages import Ui_help_page as HP


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UI()
        self.ui.setupUi(self)
        
        self.hp = HP()
        self.hp.setupUi(self.hp)
        # so strange - why does `setupUi` receive two same objects?
        # It's a method and `self=self.hp` and `help_page=self.hp`.
        # (commented by worldmozara(NCBM))
        self.cp = CP()
        self.cp.setupUi(self.cp)
        self.tp = TP()
        self.tp.setupUi(self.tp)
        
        self.ui.pages.addWidget(self.hp)
        self.ui.pages.addWidget(self.tp)
        self.ui.pages.addWidget(self.cp)

        # self.tp.output("test!!!\n")
        # self.tp.output("test2!!!\n")

        # print(self.ui.pages.currentIndex())
        # self.ui.pages.setCurrentIndex(1)
        # print(self.ui.pages.currentIndex())
        
        # TODO: Initialize Objects
        # TODO: Initialize Client Information
        # TODO: Initialize default state
        # TODO: Initialize default Assets
        # TODO: Initialize Thread
        # TODO: Initialize Worker
        # TODO: Initalize Widgets Slots Connection
        # TODO: Initalize Threads Slots Connection
        # TODO: Initalize Bootup Checking

        # time_end = time.perf_counter()
        # print(f"系统初始化耗时{((time_end - time_start) * 1000):.1f}毫秒")
        # self.text_log.log(f"系统初始化耗时{((time_end - time_start) * 1000):.1f}毫秒")

        # set singal and slot
        self.ui.help_us.triggered.connect(lambda: self.set_pages_index(0))
        self.ui.senior_terminal.triggered.connect(lambda: self.set_pages_index(1))
        self.ui.new_project.triggered.connect(lambda: self.set_pages_index(2))

    def set_pages_index(self, page_num: int):
        self.ui.pages.setCurrentIndex(page_num)

    def create_project(self):  # add args if needed
        # require working directory

        # validate args
        sel_drvs = [...]  # selected drivers
        sel_adps = [...]  # selected adapters
        if not sel_drvs:
            # show_error("NoneBot2 项目需要*至少一个*驱动器才能正常工作！")
            return
        if not sel_adps:
            # show_error("NoneBot2 项目需要*至少一个*适配器才能正常工作！")
            return

        # lock widgets
        ...

        try:
            # proc = wing.create(..., new_win=False, catch_output=True)
            # Then read data from `proc.stdout`.
            ...
        except Exception as e:
            # show_error(e)
            return
        
        # unlock widgets
        ...

        # show complete

    def run_project(self):
        # require working directory
        ...

        # use sys.executable as `python_path` if nb-cli is installed with this,
        # otherwise use `wing.find_python(workdir)`.

        # proc = Popen((python_path, "-m", "nb_cli", "run"), stdout=PIPE, stderr=STDOUT)
        # Then read data from `proc.stdout`.