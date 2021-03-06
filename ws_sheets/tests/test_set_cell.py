import numpy
import unittest
import ws_sheets

def test_cell(settings):
    b = ws_sheets.Book(settings)

    b['0'][0, 0] = '2+2'
    
    assert b['0'][0, 0] == 4

    b['0'][0, 0] = '4'
    b['0'][0, 1] = 'sheet[0, 0]'

    assert b['0'][0, 1] == 4

    b['0'][0, 0] = '2'
    b['0'][0, 1] = '3'
    b['0'][0, 2] = 'sheet[0, 0:2]'
    print('cell 0,0 = ', b['0'][0, 0])
    print('cell 0,1 = ', b['0'][0, 1])
    print('cell 0,2 = ', b['0'][0, 2])
    
    assert numpy.all(b['0'][0, 2] == numpy.array([2, 3]))

    assert b.context == 0

    b['0'][0, 0] = 'sheet[0, 0]'

    assert repr(b['0'][0, 0].item()) == "RuntimeError('recursion',)"

    b['0'][0, 0] = ''
    
    assert b['0'][0, 0].item() is None

    b['0'][0, 0] = '4'
    b['1'][0, 0] = 'book[\'0\'][0, 0]'

    assert b['1'][0, 0] == 4

def test_cell2(settings):
    b = ws_sheets.Book(settings)

    b.set_cell('0', 0, 0, '1')
    b.set_cell('0', 1, 0, '2')
    b.set_cell('0', 2, 0, '3')
    b.set_cell('0', 3, 0, '4')
    b.set_cell('0', 4, 0, '5')

    b.set_cell('0', 0, 1, 'sum(sheet[0:5, 0])')

    assert b['0'][0, 1] == 15
   

