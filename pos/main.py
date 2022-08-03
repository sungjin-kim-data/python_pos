import sys
import datetime
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PySide6.QtCore import QTimer
from ui import Ui_ui


dummy = [
  {"menu": "에스프레소 L", "quantity": "10", "order_amount": "10000", "time": "2022-05-01 22:09", "status": "waiting"},
  {"menu": "에스프레소 L", "quantity": "10", "order_amount": "10000", "time": "2022-05-01 22:09", "status": "waiting"}
]

class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    self.ui = Ui_ui()
    self.ui.setupUi(self)

    self.timer = QTimer()
    self.timer.setInterval(1000)
    self.timer.timeout.connect(self.tick)
    self.timer.start()

    self.load()

  def tick(self):
    now = datetime.datetime.now()
    self.ui.lb_now.setText(f"현재 시각 : {now}")

  def load(self):
    for d in dummy:
      r = self.ui.table_orders.rowCount()
      self.ui.table_orders.insertRow(r)
      self.ui.table_orders.setItem(r, 0, QTableWidgetItem(d["menu"]))
      self.ui.table_orders.setItem(r, 1, QTableWidgetItem(d["quantity"]))
      self.ui.table_orders.setItem(r, 2, QTableWidgetItem(d["order_amount"]))
      self.ui.table_orders.setItem(r, 3, QTableWidgetItem(d["time"]))
      self.ui.table_orders.setItem(r, 4, QTableWidgetItem(d["status"]))

if __name__ == "__main__":
  app = QApplication()

  window = MainWindow()
  window.show()

  sys.exit(app.exec())