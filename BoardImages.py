
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage

# Loads board images and provides access to them
class BoardImages:
    def __init__(self, cellSize):
        pieces = ['WR', 'WN', 'WB', 'WQ', 'WK', 'WK#', 'WP', 'BR', 'BN', 'BB', 'BQ', 'BK', 'BK#', 'BP']
        self.images = {piece: self.loadImage(piece, cellSize) for piece in pieces}
        
    def loadImage(self, imageName, cellSize):
        img = QImage(f'resources/imgs/{imageName}.png')
        return img.scaled(cellSize, cellSize, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    
    def getImage(self, imageName):
        return self.images[imageName]