# pychess

# ToDo

Core:
- Update check prevention logic so that it is impossible to move other peices if this results in king's check
- Fix isCellUnder attack logic for pawns
- If the king is currently checked - only moves that uncheck it are valid
- If there are no valid moves for a checked King - it is a checkmate

- O-O and O-O-O
- Empasane move

Refactoring:
- Can we get rid of ignoreChecks? Split Board class?

GUI:
- Add moves record list
