# Tic Tac 2.0
The childhood game of Tic Tac Toe except you can edit the grid..

## Rules
X player goes first, then O and they alternate turns.
You win if you get three of your character in a row, column or diagonal.

By default, the grid starts with 4 empty tiles vertically in the center. The rest of the grid isn't valid play space.

Each turn 1 of 3 actions can be made:
1. Place you symbol on an empty grid tile
2. Create 4 new grid tiles
3. Block two empty grid tiles

1. Your symbol has to be on an empty grid tile, you can't replace an opponents or place it on a non-existing tile (shown with a '|')
2. The first new tile must neighbour an already existing tile. All 4 newly created grid tiles must be neighbouring in any direction. By neighbouring, it refers to the diagram below.
❌❌❌❌❌
❌✓ ✓ ✓ ❌
❌✓ T ✓ ❌
❌✓ ✓ ✓ ❌
❌❌❌❌❌
3. Like action 1, only empty grid tiles can be blocked. A blocked tile cannot be replaced with a symbol.