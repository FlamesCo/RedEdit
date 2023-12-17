import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

def edit_bytes(file_path, offset, new_values):
    try:
        with open(file_path, "r+b") as file:
            file.seek(offset)
            file.write(bytes(new_values))
        return True
    except Exception as e:
        print(e)
        return False

class ROMEditorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ROM Hex Editor')

        # Layout
        layout = QVBoxLayout()

        # ROM Path
        self.romPathLabel = QLabel('ROM Path:')
        self.romPathEdit = QLineEdit()
        layout.addWidget(self.romPathLabel)
        layout.addWidget(self.romPathEdit)

        # Offset
        self.offsetLabel = QLabel('Offset (hex):')
        self.offsetEdit = QLineEdit()
        layout.addWidget(self.offsetLabel)
        layout.addWidget(self.offsetEdit)

        # New Values
        self.newValuesLabel = QLabel('New Values (hex):')
        self.newValuesEdit = QLineEdit()
        layout.addWidget(self.newValuesLabel)
        layout.addWidget(self.newValuesEdit)

        # Edit Button
        self.editButton = QPushButton('Edit ROM')
        self.editButton.clicked.connect(self.editRom)
        layout.addWidget(self.editButton)

        self.setLayout(layout)

    def editRom(self):
        rom_path = self.romPathEdit.text()
        if not os.path.exists(rom_path):
            QMessageBox.warning(self, 'Error', 'ROM file does not exist.')
            return

        try:
            offset = int(self.offsetEdit.text(), 16)
            new_values = [int(value, 16) for value in self.newValuesEdit.text().strip().split()]
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Invalid offset or values. Please enter valid hexadecimal values.')
            return

        if edit_bytes(rom_path, offset, new_values):
            QMessageBox.information(self, 'Success', 'ROM edited successfully.')
        else:
            QMessageBox.warning(self, 'Error', 'An error occurred while editing the ROM.')

def main():
    app = QApplication(sys.argv)
    ex = ROMEditorApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
