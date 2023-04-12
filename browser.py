import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

app = QApplication(sys.argv)
QApplication.setApplicationName('xor722')

view = QWebEngineView()
view.load(QUrl("https://www.google.com"))
view.show()

sys.exit(app.exec_())