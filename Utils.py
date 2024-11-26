def oppositeColor(color: str):
    return 'W' if color == 'B' else 'B'

# Convert a cell name (e.g. 'e4') to a tuple of (row, col)
def toCell(cell: str) -> tuple[int, int]:
    cellLC = cell.lower()
    return (ord(cellLC[0]) - ord('a'), int(cellLC[1]) - 1)

# Convert a list of cell names to a list of tuples
def toCells(cells: list[str]) -> list[tuple[int, int]]:
    return [toCell(cell) for cell in cells]