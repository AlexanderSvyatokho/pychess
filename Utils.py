def oppositeColor(color: str):
    return 'W' if color == 'B' else 'B'

def toCell(cell: str) -> tuple[int, int]:
    cellLC = cell.lower()
    return (ord(cellLC[0]) - ord('a'), int(cellLC[1]) - 1)

def toCells(cells: list[str]) -> list[tuple[int, int]]:
    return [toCell(cell) for cell in cells]