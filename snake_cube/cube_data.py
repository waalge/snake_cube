"""
Data of known cubes.
Useful for testing. 
Keys:
    - strip_lengths
    - cube_side_length
    - rel_solutions
"""

cubes = [
        {
        "strip_lengths"     : [2,2,2,2,2,2,2],
        "cube_side_length"  : 2,
        "rel_solutions"     : [
            [0, 0, 0, 3, 1, 2, 2], 
            [0, 0, 2, 1, 1, 2, 0], 
            [0, 0, 3, 1, 1, 3, 0], 
            [0, 0, 3, 1, 2, 2, 1], 
            [0, 0, 3, 3, 0, 2, 1], 
            [0, 0, 3, 3, 3, 3, 0]
            ]
        },  
        {
        "strip_lengths"     : [2,2,2,2,3,3,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,],
        "cube_side_length"  : 3,
        "rel_solutions"     : [
            [0,0,0,1,2,0,0,2,1,0,0,3,1,0,2,2,1,3,1,1,2,3],
            [0,0,0,1,3,1,1,2,0,0,1,3,0,0,3,2,1,3,1,1,2,3],
            [0,0,0,2,1,1,2,0,3,2,1,1,2,0,2,1,1,3,1,2,3,0],
            [0,0,0,3,1,1,3,0,0,0,1,1,2,0,1,2,2,2,2,1,0,3],
            [0,0,0,3,1,1,3,0,1,2,2,1,3,0,1,3,0,0,2,0,1,2],
            [0,0,0,3,1,1,3,0,1,2,2,1,3,2,2,2,1,3,1,1,0,3],
            [0,0,1,2,0,0,2,1,0,3,3,0,2,3,3,3,0,2,0,0,1,3],
            [0,0,1,2,0,0,2,1,1,1,0,0,3,1,0,3,3,3,3,0,1,3],
            [0,0,1,2,2,2,2,1,0,3,1,2,2,3,1,1,2,0,0,2,3,3],
            [0,0,1,2,2,2,2,1,3,3,2,2,1,3,2,1,3,1,1,2,3,3],
            [0,0,2,0,3,3,0,2,1,0,3,3,0,2,2,1,3,1,1,2,3,0],
            [0,0,2,1,1,3,1,2,2,0,1,3,0,0,1,2,0,0,2,1,0,3],
            [0,0,2,1,1,3,1,2,3,0,0,3,1,0,0,2,1,1,3,1,0,3],
            [0,0,2,1,1,3,1,2,3,0,0,3,1,2,3,3,0,2,0,0,1,2],
            [0,0,2,3,0,2,0,0,3,2,2,1,3,2,0,2,1,1,3,1,2,3],
            [0,0,2,3,3,3,3,0,2,0,1,1,2,0,3,2,1,1,3,1,2,3],
            [0,0,3,2,0,0,2,1,1,0,3,3,0,2,1,0,3,3,3,3,0,2],
            [0,0,3,2,0,0,2,1,1,3,2,2,1,3,0,1,2,2,2,2,1,3],
            [0,0,3,2,1,1,3,1,2,2,0,3,3,0,1,2,0,3,3,0,2,0],
            [0,0,3,2,1,1,3,1,2,3,1,2,2,3,3,1,2,2,2,2,1,3],
            [0,0,3,2,1,3,1,1,2,0,2,1,1,2,3,0,2,1,1,2,0,0],
            [0,0,3,2,1,3,1,1,2,3,3,0,2,3,1,3,0,0,2,0,3,3],
            [0,0,3,2,2,2,2,1,3,1,0,0,3,1,2,3,0,0,2,0,3,3],
            [0,0,3,2,2,2,2,1,3,2,1,1,2,0,3,2,1,1,3,1,2,2]
            ]
        },  
        {
        "strip_lengths"     : [3,4,4,4,2,4,2,4,2,2,2,2,2,2,2,2,2,3,2,4,3,3,2,4,2,3,2,2,2,2,2,3,2,2,2,2,4,2,4],
        "cube_side_length"  : 4,
        "rel_solutions"     : [
            [0,0,3,0,0,2,3,0,2,0,0,1,1,1,2,0,3,3,2,1,2,0,1,1,2,1,1,2,2,3,1,2,1,0,3,3,3,3,0],
            [0,0,3,0,0,2,3,0,2,0,0,1,1,1,2,0,3,3,2,1,2,0,1,1,2,1,1,2,2,3,2,1,2,3,0,2,0,0,3],
            [0,0,3,0,0,3,2,1,3,1,1,0,0,0,3,1,2,2,3,0,3,1,0,0,3,0,0,3,3,2,0,3,0,1,2,2,2,2,1],
            [0,0,3,0,0,3,2,1,3,1,1,0,0,0,3,1,2,2,3,0,3,1,0,0,3,0,0,3,3,2,3,0,3,2,1,3,1,1,2],
            [0,0,3,0,2,0,1,2,2,2,2,3,3,1,2,2,1,3,2,1,2,2,3,1,2,1,3,0,2,3,2,1,2,3,0,0,2,0,3],
            [0,0,3,0,2,0,1,2,2,2,2,3,3,1,2,2,1,3,2,1,2,2,3,1,2,1,3,0,2,3,3,0,3,2,1,1,3,1,2],
            [0,0,3,0,2,1,0,3,3,3,3,2,2,0,3,3,0,2,3,0,3,3,2,0,3,0,2,1,3,2,2,1,2,3,0,0,2,0,3],
            [0,0,3,0,2,1,0,3,3,3,3,2,2,0,3,3,0,2,3,0,3,3,2,0,3,0,2,1,3,2,3,0,3,2,1,1,3,1,2], 
            ],
        "abs_solutions"     : [
            [(2,0,0),(2,3,0),(-1,3,0),(-1,0,0),(-1,0,-1),(2,0,-1),(2,0,-2),(-1,0,-2),(-1,1,-2),(-1,1,-1),(0,1,-1),(0,1,0),(0,2,0),(1,2,0),(1,1,0),(1,1,-1),(1,2,-1),(-1,2,-1),(-1,3,-1),(2,3,-1),(2,1,-1),(2,1,-3),(2,0,-3),(-1,0,-3),(-1,1,-3),(1,1,-3),(1,1,-2),(0,1,-2),(0,2,-2),(-1,2,-2),(-1,2,-3),(1,2,-3),(1,2,-2),(2,2,-2),(2,2,-3),(2,3,-3),(-1,3,-3),(-1,3,-2),(2,3,-2)],
            [(2,0,0),(2,3,0),(-1,3,0),(-1,0,0),(-1,0,-1),(2,0,-1),(2,0,-2),(-1,0,-2),(-1,1,-2),(-1,1,-1),(0,1,-1),(0,1,0),(0,2,0),(1,2,0),(1,1,0),(1,1,-1),(1,2,-1),(-1,2,-1),(-1,3,-1),(2,3,-1),(2,1,-1),(2,1,-3),(2,0,-3),(-1,0,-3),(-1,1,-3),(1,1,-3),(1,1,-2),(0,1,-2),(0,2,-2),(-1,2,-2),(-1,3,-2),(1,3,-2),(1,2,-2),(2,2,-2),(2,3,-2),(2,3,-3),(-1,3,-3),(-1,2,-3),(2,2,-3)],
            [(2,0,0),(2,3,0),(-1,3,0),(-1,0,0),(-1,0,-1),(-1,3,-1),(-1,3,-2),(-1,0,-2),(0,0,-2),(0,0,-1),(0,1,-1),(0,1,0),(1,1,0),(1,2,0),(0,2,0),(0,2,-1),(1,2,-1),(1,0,-1),(2,0,-1),(2,3,-1),(0,3,-1),(0,3,-3),(-1,3,-3),(-1,0,-3),(0,0,-3),(0,2,-3),(0,2,-2),(0,1,-2),(1,1,-2),(1,0,-2),(1,0,-3),(1,2,-3),(1,2,-2),(1,3,-2),(1,3,-3),(2,3,-3),(2,0,-3),(2,0,-2),(2,3,-2)],
            [(2,0,0),(2,3,0),(-1,3,0),(-1,0,0),(-1,0,-1),(-1,3,-1),(-1,3,-2),(-1,0,-2),(0,0,-2),(0,0,-1),(0,1,-1),(0,1,0),(1,1,0),(1,2,0),(0,2,0),(0,2,-1),(1,2,-1),(1,0,-1),(2,0,-1),(2,3,-1),(0,3,-1),(0,3,-3),(-1,3,-3),(-1,0,-3),(0,0,-3),(0,2,-3),(0,2,-2),(0,1,-2),(1,1,-2),(1,0,-2),(2,0,-2),(2,2,-2),(1,2,-2),(1,3,-2),(2,3,-2),(2,3,-3),(2,0,-3),(1,0,-3),(1,3,-3)],
            [(2,0,0),(2,3,0),(-1,3,0),(-1,0,0),(-1,0,1),(2,0,1),(2,0,2),(-1,0,2),(-1,1,2),(-1,1,1),(0,1,1),(0,1,0),(0,2,0),(1,2,0),(1,1,0),(1,1,1),(1,2,1),(-1,2,1),(-1,3,1),(2,3,1),(2,1,1),(2,1,3),(2,0,3),(-1,0,3),(-1,1,3),(1,1,3),(1,1,2),(0,1,2),(0,2,2),(-1,2,2),(-1,3,2),(1,3,2),(1,2,2),(2,2,2),(2,3,2),(2,3,3),(-1,3,3),(-1,2,3),(2,2,3)],
            [(2,0,0),(2,3,0),(-1,3,0),(-1,0,0),(-1,0,1),(2,0,1),(2,0,2),(-1,0,2),(-1,1,2),(-1,1,1),(0,1,1),(0,1,0),(0,2,0),(1,2,0),(1,1,0),(1,1,1),(1,2,1),(-1,2,1),(-1,3,1),(2,3,1),(2,1,1),(2,1,3),(2,0,3),(-1,0,3),(-1,1,3),(1,1,3),(1,1,2),(0,1,2),(0,2,2),(-1,2,2),(-1,2,3),(1,2,3),(1,2,2),(2,2,2),(2,2,3),(2,3,3),(-1,3,3),(-1,3,2),(2,3,2)],
            [(2,0,0),(2,3,0),(-1,3,0),(-1,0,0),(-1,0,1),(-1,3,1),(-1,3,2),(-1,0,2),(0,0,2),(0,0,1),(0,1,1),(0,1,0),(1,1,0),(1,2,0),(0,2,0),(0,2,1),(1,2,1),(1,0,1),(2,0,1),(2,3,1),(0,3,1),(0,3,3),(-1,3,3),(-1,0,3),(0,0,3),(0,2,3),(0,2,2),(0,1,2),(1,1,2),(1,0,2),(1,0,3),(1,2,3),(1,2,2),(1,3,2),(1,3,3),(2,3,3),(2,0,3),(2,0,2),(2,3,2)],
            [(2,0,0),(2,3,0),(-1,3,0),(-1,0,0),(-1,0,1),(-1,3,1),(-1,3,2),(-1,0,2),(0,0,2),(0,0,1),(0,1,1),(0,1,0),(1,1,0),(1,2,0),(0,2,0),(0,2,1),(1,2,1),(1,0,1),(2,0,1),(2,3,1),(0,3,1),(0,3,3),(-1,3,3),(-1,0,3),(0,0,3),(0,2,3),(0,2,2),(0,1,2),(1,1,2),(1,0,2),(2,0,2),(2,2,2),(1,2,2),(1,3,2),(2,3,2),(2,3,3),(2,0,3),(1,0,3),(1,3,3)],
            [(2,0,0),(2,3,0),(-1,3,0),(-1,3,-3),(-1,2,-3),(-1,2,0),(-1,1,0),(-1,1,-3),(0,1,-3),(0,2,-3),(0,2,-2),(1,2,-2),(1,2,-3),(1,1,-3),(1,1,-2),(0,1,-2),(0,0,-2),(0,0,0),(-1,0,0),(-1,0,-3),(1,0,-3),(1,0,-1),(2,0,-1),(2,3,-1),(1,3,-1),(1,1,-1),(1,1,0),(1,2,0),(0,2,0),(0,1,0),(0,1,-1),(0,3,-1),(0,3,-2),(1,3,-2),(1,3,-3),(2,3,-3),(2,0,-3),(2,0,-2),(2,3,-2)],
            [(2,0,0),(2,3,0),(-1,3,0),(-1,3,3),(-1,2,3),(-1,2,0),(-1,1,0),(-1,1,3),(0,1,3),(0,2,3),(0,2,2),(1,2,2),(1,2,3),(1,1,3),(1,1,2),(0,1,2),(0,0,2),(0,0,0),(-1,0,0),(-1,0,3),(1,0,3),(1,0,1),(2,0,1),(2,3,1),(1,3,1),(1,1,1),(1,1,0),(1,2,0),(0,2,0),(0,1,0),(0,1,1),(0,3,1),(0,3,2),(1,3,2),(1,3,3),(2,3,3),(2,0,3),(2,0,2),(2,3,2)
]
            ]
        },  
    ]

