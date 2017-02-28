
import numpy as np

casual = np.matrix([[1, 1, 2],
                    [0, 3, 1]])
                   
small = np.matrix([[2, 2],
                   [2, 0]])

many3  = np.matrix([[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 12]])

large = np.matrix([[0, 0, 0],
                   [0, 2, 2],
                   [0, 2, 4]])

basic_fail = np.matrix([[0, 0, 3],
                        [0, 0, 0],
                        [3, 0, 3]])

asymmetric = np.matrix([[0, 0, 1, 1],
                        [0, 0, 2, 2],
                        [0, 2, 3, 1]])
asymmetric2 = np.transpose(asymmetric)

romance = np.matrix([[63,56,30,16, 2, 0, 0, 2],
                     [46,40,25,14, 1, 0, 0, 4],
                     [23,20,18, 8, 1, 0, 0, 2],
                     [26,24,21, 4, 1, 0, 0, 0],
                     [ 8, 9, 1, 2, 0, 0, 0, 0],
                     [ 4, 1, 1, 0, 0, 0, 0, 0]])

southern_women = np.matrix(
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
     [0, 0, 0, 1, 1, 4, 0, 6, 0, 4, 0, 3, 0, 5],
     [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
     [0, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
     [0, 0, 5, 1, 1, 3, 0, 4, 0, 3, 0, 1, 0, 3],
     [0, 0, 5, 3, 1, 3, 0, 5, 0, 2, 0, 3, 0, 2]])

malaria = np.matrix(
    [[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [ 4, 8,22,44,28,49,30,25,10,21,21,45,43,41,35,40,22,36,15,30, 0,15, 8, 0,12, 5, 6, 5, 0, 0, 0, 0, 1, 0, 5],
     [ 2, 3, 8,32,20,57,32,28,13,26,18,32,36,41,54,45,26,37,12,31, 0,12, 8, 0,11, 4, 8, 5, 0, 0, 0, 0, 7, 0, 7],
     [ 0, 2, 6,30,15,19,23,26,11,13,10,31,35,28,24,36,25,25, 8,24, 0,10, 6, 0,11, 5, 5, 4, 0, 0, 0, 0, 6, 0, 6],
     [ 0, 3, 4, 8, 7,19, 9, 9, 5,20,16,17,18,17,16,19, 8,31,11,21, 0, 7, 3, 0,13, 3, 3, 3, 0, 0, 0, 0, 3, 0, 2],
     [ 0, 1, 4,23, 8,19,11, 9, 4,11, 7,18,14,12,10,11,14,29, 8,11, 0, 3, 3, 0, 6, 2, 0, 3, 0, 0, 0, 0, 2, 0, 3],
     [ 0, 0, 0, 0, 2, 6, 4, 5, 1, 9, 4, 7,11, 8, 8, 4, 5,22, 2,10, 0, 2, 2, 0, 2, 1, 1, 0, 0, 0, 0, 0, 2, 0, 1],
     [ 0, 1, 4, 3, 4, 4, 2, 7, 5,14,10,11,17,16,15,11,10,20, 4, 6, 0, 3, 4, 0, 7, 3, 0, 1, 0, 0, 0, 0, 1, 0, 1],
     [ 0, 0, 0, 0, 1, 0, 2, 3, 3, 0, 2, 6,12, 9, 8, 6, 3, 3, 6, 6, 0, 3, 5, 0, 1, 0, 1, 4, 0, 0, 0, 0, 2, 0, 4],
     [ 0, 0, 3, 3, 3, 8, 2, 2, 6, 2, 3,10,11, 7, 6, 2, 5, 7, 1, 3, 0, 3, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [ 0, 0, 0, 0, 0, 3, 0, 1, 0, 0, 1, 4, 4, 3, 4, 4, 7, 3, 0, 3, 0, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
     [ 0, 0, 0, 0, 2, 1, 3, 0, 0, 0, 1, 3, 3, 3, 2, 2, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [ 0, 0, 0, 0, 3, 3, 0, 1, 2, 1, 1, 2, 2, 2, 4, 0, 4, 1, 2, 4, 0, 3, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
     [ 0, 0, 0, 1, 1, 2, 0, 2, 2, 1, 1, 3, 4, 4, 4, 3, 1, 7, 3, 4, 0, 2, 1, 0, 3, 0, 1, 1, 0, 0, 0, 0, 3, 0, 2],
     [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [ 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 3, 1, 7, 0, 2, 4, 3, 6, 3, 6, 0, 0, 2, 0, 3, 1, 0, 1, 0, 0, 0, 0, 2, 0, 2],
     [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [ 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 2, 3, 2, 3, 0, 5, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [ 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 2, 2, 2, 1, 2, 2, 2, 0, 0, 0, 1, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]])
