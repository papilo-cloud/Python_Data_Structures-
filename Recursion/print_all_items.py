def print_all_items(array):
    for value in array:
        if type(value) == list:
            print_all_items(value)
        else:
            print(value)
        

array = [ 1,
            2,
            3,
            [4, 5, 6],
            7,
            [8,
                [9, 10, 11,
                    [12, 13, 14]
                ]
            ],
            [15, 16, 17, 18, 19,
                [20, 21, 22,
                    [23, 24, 25,
                        [26, 27, 29]
                    ], 30, 31
                ], 32
            ], 33
        ]
(print_all_items(array))
x = [1,2,3]
# print(x ==)

