import numpy as np

def read_row(filename):
    '''
    Reads row of numbers from file
    :param filename: name of file with numbers
    :return: list of numbers from file
    '''
    data = []
    with open(filename, 'r') as data_file:
        data_str = data_file.read()

    data_str = data_str.split('\n')
    for line in data_str:
        data.append(np.float16(line))
    return data

def read_matrix(filename, separator = '\t'):
    '''
    Reads matrix from file
    :param filename: name of file with numbers
    :param separator: separator in lines in file. Default value: '\t'
    :return: matrix of numbers from file
    '''
    data = []
    with open(filename, 'r') as data_file:
        for line in data_file:
            data_line = line.split(separator)
            line_float = []
            for number in data_line:
                try:
                    line_float.append(np.float16(number))
                except ValueError:
                    line_float.append(np.float16('nan'))
            data.append(np.array(line_float))
        return np.array(data)

def read_line(filename, separator = '\t'):
    '''
    Reads line of numbers from file
    :param filename: name of file with numbers
    :param separator: separator in lines in file. Default value: '\t'
    :return: list of numbers from file
    '''
    data = []
    with open(filename, 'r') as data_file:
        data_str = data_file.readline().split(separator)
        for element in data_str:
            data.append(np.float16(element))
    return data