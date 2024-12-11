import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QImage

def resourcePath(relative_path):
    """Get the absolute path to a resource, works for dev and PyInstaller."""
    if getattr(sys, 'frozen', False):  # PyInstaller adds this attribute
        base_path = Path(sys._MEIPASS)  # Temporary folder for bundled app
    else:
        base_path = Path(__file__).parent
    return base_path / relative_path

# Loads board images and provides access to them
class BoardImages:
    def __init__(self, cellSize):
        pieces = ['WR', 'WN', 'WB', 'WQ', 'WK', 'WK#', 'WK=', 'WP', 'BR', 'BN', 'BB', 'BQ', 'BK', 'BK#', 'BK=', 'BP']
        self.images = {piece: self.loadImage(piece, cellSize) for piece in pieces}
        
    def loadImage(self, imageName, cellSize):
        img = QImage(resourcePath(f'resources/imgs/{imageName}.png'))
        return img.scaled(cellSize, cellSize, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    
    def getImage(self, imageName):
        return self.images[imageName]