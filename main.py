import random


def shuffle(my_list):
    # Cycling all list
    for i in range(0, len(my_list)):
        # Generating a random index
        swap = random.randint(0, len(my_list)-1)
        # Saving a value and swapping
        tmp = my_list[i]
        my_list[i] = my_list[swap]
        my_list[swap] = tmp


random.seed(42)

# Perform this test ten times:
for i in range(10):
    testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffle(testData1)
    # Make sure the number of values hasn't changed:
    assert len(testData1) == 10
    # Make sure the order has changed:
    assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Make sure that when re-sorted, all the original values are there:
    assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Make sure an empty list shuffled remains empty:
testData2 = []
shuffle(testData2)
assert testData2 == []
