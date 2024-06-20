import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class YouTubeShortsApp:
    def __init__(self, root):
        self.root = root
        self.root.setGeometry(100, 100, 800, 600)
        
        self.tab_widget = QTabWidget(self.root)
        self.tab_widget.setGeometry(0, 0, 800, 600)
        
        # Load YouTube Shorts page
        self.load_youtube_shorts()

    def load_youtube_shorts(self):
        browser = QWebEngineView()
        url = QUrl("https://www.youtube.com/shorts/")
        browser.load(url)
        self.tab_widget.addTab(browser, "YouTube Shorts")

def main():
    app = QApplication(sys.argv)
    root = QMainWindow()
    root.setWindowTitle("YouTube Shorts Viewer")

    # Create instance of YouTubeShortsApp
    app_instance = YouTubeShortsApp(root)

    # Set the central widget of the QMainWindow to the QTabWidget
    root.setCentralWidget(app_instance.tab_widget)

    # Show the main window
    root.show()

    # Start the application event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
