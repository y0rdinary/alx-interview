#!/usr/bin/python3
def canUnlockAll(boxes):
    keys = set()
    opened_boxes = []
    i = 0

    while i < len(boxes):
        old = i
        opened_boxes.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < len(boxes) and key not in opened_boxes:
                i = key
                break
        if old != i:
            continue
        else:
            break

    for i in range(len(boxes)):
        if i not in opened_boxes and i != 0:
            return False
    return True