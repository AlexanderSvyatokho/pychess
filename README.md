# PyChess

Simple chess game written in Python not using any engines and without studying any chess algorithms. Naive implementation for fun.

## ToDo List
Core:
  - Refactor tests by creating a utilities that return challanges and expected moves
  - Fix Depth N bot for depth > 1
  - Add multi threading
  - Prioritize castling
  - Review and improve the code

Postponed:
  - Ability to play for black
  - Promotion options (currently Queen is the only option)
  - En passant move
  - Threefold repetition: draw if the same position occurs three times during the game
  - Fifty-move rule: draw by 50 moves without captures and pawn moves
  