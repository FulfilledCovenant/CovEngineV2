from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

class TM:

    DARK = "Dark"
    LIGHT = "Light"
    SYSTEM = "System"
    
    @staticmethod
    def ap_te(app, theme_name):
        if theme_name == TM.DARK:
            TM.ap_dk(app)
        elif theme_name == TM.LIGHT:
            TM.ap_lt(app)
        else:  
            app.setStyle("Fusion")  
    
    @staticmethod
    def ap_dk(app):
        app.setStyle("Fusion")

        dark_palette = QPalette()

        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(35, 35, 35))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)

        app.setPalette(dark_palette)

        app.setStyleSheet("""
        QToolTip { 
            color: #ffffff; 
            background-color: #2a2a2a; 
            border: 1px solid #767676; 
        }
        QTableView, QHeaderView, QTableView::item { 
            background-color: #202020;
            color: white;
        }
        QTableView::item:selected { 
            background-color: #3388ff;
        }
        QHeaderView::section { 
            background-color: #353535;
            color: white;
            border: 1px solid #5c5c5c;
        }
        QFrame[frameShape="4"], QFrame[frameShape="5"] {
            color: #999999;
        }
        QComboBox, QLineEdit, QSpinBox, QTextEdit, QPlainTextEdit {
            background-color: #252525;
            border: 1px solid #555555;
            color: white;
        }
        """)

    @staticmethod
    def ap_lt(app):
        app.setStyle("Fusion")

        light_palette = QPalette()

        light_palette.setColor(QPalette.Window, QColor(240, 240, 240))
        light_palette.setColor(QPalette.WindowText, Qt.black)
        light_palette.setColor(QPalette.Base, QColor(255, 255, 255))
        light_palette.setColor(QPalette.AlternateBase, QColor(245, 245, 245))
        light_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        light_palette.setColor(QPalette.ToolTipText, Qt.black)
        light_palette.setColor(QPalette.Text, Qt.black)
        light_palette.setColor(QPalette.Button, QColor(240, 240, 240))
        light_palette.setColor(QPalette.ButtonText, Qt.black)
        light_palette.setColor(QPalette.BrightText, Qt.red)
        light_palette.setColor(QPalette.Link, QColor(0, 100, 200))
        light_palette.setColor(QPalette.Highlight, QColor(76, 163, 224))
        light_palette.setColor(QPalette.HighlightedText, Qt.white)

        app.setPalette(light_palette)

        app.setStyleSheet("""
        QToolTip { 
            color: #000000; 
            background-color: #f0f0f0; 
            border: 1px solid #767676; 
        }
        QTableView::item:selected { 
            background-color: #3388ff;
            color: white;
        }
        QHeaderView::section { 
            background-color: #f0f0f0;
            border: 1px solid #cccccc;
        }
        QComboBox, QLineEdit, QSpinBox, QTextEdit, QPlainTextEdit {
            background-color: white;
            border: 1px solid #cccccc;
        }
        """)
        
    @staticmethod
    def gt_ss(theme_name, widget_type):

        if theme_name == TM.DARK:
            styles = {
                "sidebar": """
                    background-color: #333333;
                    color: white;
                """,
                "header": """
                    background-color: #2d2d2d;
                    color: white;
                """,
                "card": """
                    background-color: #2a2a2a;
                    border-radius: 8px;
                    color: white;
                """,
                "button_primary": """
                    background-color: #2a82da;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 6px;
                """,
                "button_secondary": """
                    background-color: #444444;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 6px;
                """
            }
        else:  
            styles = {
                "sidebar": """
                    background-color: #f0f0f0;
                    color: black;
                """,
                "header": """
                    background-color: #e0e0e0;
                    color: black;
                """,
                "card": """
                    background-color: white;
                    border: 1px solid #dddddd;
                    border-radius: 8px;
                    color: black;
                """,
                "button_primary": """
                    background-color: #2a82da;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 6px;
                """,
                "button_secondary": """
                    background-color: #e0e0e0;
                    color: black;
                    border: 1px solid #cccccc;
                    border-radius: 4px;
                    padding: 6px;
                """
            }
        
        return styles.get(widget_type, "") 