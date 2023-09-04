# Is Alive?

Toy problem on a [Go Board](https://en.wikipedia.org/wiki/Go_(game)) where for a given initial position, check whether a stone is alive or dead. For the stone to be dead, there needs to be a perimiter of stones of opposite color (diagonal cells are ignored) around the initial position. For an initial position (1,1): 

## Dead Examples

```
board = [
        ['','B','','',''],
        ['B','W','B','',''],
        ['','B','','',''],
        ['','','','',''],
        ['','','','','']
    ]

board = [
        ['','W','W','',''],
        ['W','B','B','W',''],
        ['W','B','B','W',''],
        ['','W','W','',''],
        ['','','','','']
    ]
```

## Alive Examples

```
board = [
        ['','','','',''],
        ['','B','','',''],
        ['','','','',''],
        ['','','','',''],
        ['','','','','']
    ]

board = [
        ['','B','B','B',''],
        ['B','W','W','B',''],
        ['B','W','W','B',''],
        ['','B','W','B',''],
        ['','','','','']
    ]


```

This solution functions by implementing the [Breadth-First-Search](https://en.wikipedia.org/wiki/Breadth-first_search) algorithm to recursively search through the board for the alive condition which is a an empty cell. If none are found, the initial cell is determinted to be dead. 