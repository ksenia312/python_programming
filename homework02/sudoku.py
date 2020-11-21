from typing import Tuple, List, Set, Optional
import math
from random import randint
def read_sudoku(filename: str) -> List[List[str]]:
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(grid: List[List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(grid[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def group(values: List[str], n: int) -> List[List[str]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return [[values[i+j*n] for i in range(n)] for j in range(n)]
    pass


def get_row(grid: List[List[str]], pos: Tuple[int, int]) -> List[str]:
    """ Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return grid[pos[0]]
    pass


def get_col(grid: List[List[str]], pos: Tuple[int, int]) -> List[str]:
    """ Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    a=[grid[i][pos[1]] for i in range(len(grid))]

    return a
    pass


def get_block(grid: List[List[str]], pos: Tuple[int, int]) -> List[str]:
    """ Возвращает все значения из квадрата, в который попадает позиция pos

    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    if 0 <= pos[0] <= 2:
        st=1
    elif 3 <= pos[0] <= 5:
        st=2
    elif 6 <= pos[0] <= 8:
        st=3  
    if 0 <= pos[1] <= 2:
        sto=1
    elif 3 <= pos[1] <= 5:
        sto=2
    elif 6 <= pos[1] <= 8:
        sto=3 
    a=[]
    k=3
    for i in range((st-1)*k,(st-1)*k+k):
        for j in range((sto-1)*k,(sto-1)*k+k):
            a.append(grid[i][j])
    return a
    pass


def find_empty_positions(grid: List[List[str]]) -> Optional[Tuple[int, int]]:
    """ Найти первую свободную позицию в пазле

    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    s=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                s=(i,j)
                break
    return s
    pass


def find_possible_values(grid: List[List[str]], pos: Tuple[int, int]) -> Set[str]:
    """ Вернуть множество возможных значения для указанной позиции

    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    a=set(get_row(grid, pos))
    b=set(get_col(grid, pos))
    c=set(get_block(grid, pos))
   
    fin={str(i) for i in range(1,10)}
    fin=fin.difference(a)
    fin=fin.difference(b)
    fin=fin.difference(c)
    
    return fin
    pass



def solve(grid: List[List[str]]) -> Optional[List[List[str]]]:
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    """
    pos = find_empty_positions(grid)
   
    if not pos:
        return grid
    possible = find_possible_values(grid,pos)
    possible=list(possible)
    for i in range(len(possible)):
        grid[pos[0]][pos[1]] = possible[i]
        if solve(grid):
            return grid
        else:
            grid[pos[0]][pos[1]] = '.'
    return None
    pos = find_empty_positions(grid)
    if pos != 0:
        row,col=pos
        vse=find_possible_values(grid, pos)
        for i in range(len(vse)):
            grid[row][col]=i
            solve(grid)
    return grid
    pass
def check_solution(solution: List[List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    # TODO: Add doctests with bad puzzles
    a=[k for k in range(1,10)]
    for i in range(len(solution)):
        row=str(get_row(solution,(i,0)))
        for j in range(9):
            if row.find(str(a[j])) == -1:
                return False
        col=str(get_col(solution,(0,i)))
        for t in range(9):
            if col.find(str(a[t])) == -1:
                return False
        block=str(get_block(solution,(i,i)))   
        for m in range(9):
            if block.find(str(a[m])) == -1:
                return False

    return True
    pass


def generate_sudoku(N: int) -> List[List[str]]:
    """ Генерация судоку заполненного на N элементов

    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
   
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    """
    line = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    grid=[]
    for i in range(9):
        if i == 3 or i == 6:
            x=line[0]
            for j in range(8):
                line[j]=line[j+1]
            line[-1]=x
        buffer=line[:3]
        for j in range(len(line)-3):
            line[j]=line[j+3]
        for j in range(3):
            line[j+6]=buffer[j]
        grid.append(list(line))
        
    for i in range(9):
        grid[i]=list(map(str, grid[i]))
        
    if N<81:
        while sum(1 for row in grid for e in row if e == '.') != (81-N):
            grid[randint(0,8)][randint(0,8)] = '.'
    
    return grid
	
    pass


if __name__ == '__main__':
    for fname in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
