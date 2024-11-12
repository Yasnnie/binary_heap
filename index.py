from binary_heap import BinaryHeap


QUESTS = [
    {
        "initial_array": [10, 5, 20, 1, 15, 30, 25],
        "remove_range": 3,
        "priority_change": [
            {
                "index": 3,
                "value": 50
            },
            {
                "index":1,
                "value":8
            }
        ]
    },
    {
        "initial_array": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "remove_range": 5,
        "priority_change": [
            {
                "index": 4,
                "value": 15
            },
            {
                "index":8,
                "value":3
            }
        ]
    },
    {
        "initial_array": [50, 40, 30, 20, 10, 5, 3],
        "remove_range": 3,
        "priority_change": [
            {
                "index": 2,
                "value": 60
            },
            {
                "index":5,
                "value":1
            }
        ]
    },
    {
        "initial_array": [13, 26, 19, 17, 24, 31, 22, 11, 8, 20, 5, 27, 18],
        "remove_range": 4,
        "priority_change": [
            {
                "index": 7,
                "value": 35
            },
            {
                "index":10,
                "value":12
            }
        ]
    },

]




def response(title_index, initial_array, remove_range, priority_change):
    print(f"\n\n\n\n\nTeste Conjunto {title_index}\n\n")
    binaryHeap = BinaryHeap()

    for x in initial_array:
        binaryHeap.insert(x)
        binaryHeap.display_heap()

    for change in priority_change:
        binaryHeap.change_priority(change["index"], change["value"])

    for x in range(remove_range):
        binaryHeap.remove()
        binaryHeap.display_heap()

    binaryHeap.heap_sort()
    binaryHeap.get_high_priority()


for x in range(len(QUESTS)):
    response(x + 1, QUESTS[x]["initial_array"], QUESTS[x]["remove_range"] ,QUESTS[x]["priority_change"])

