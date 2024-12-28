#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Система управления складом

class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __repr__(self):
        return f"<{self.value}>"
def depth_limited_search(node, goal, limit, depth=0):
    if node is None:
        return None
    if node.value == goal:
        return node
    if depth >= limit:
        return None
    # Поиск в левом и правом поддереве
    found_in_left = depth_limited_search(node.left, goal, limit, depth + 1)
    if found_in_left is not None:
        return found_in_left
    found_in_right = depth_limited_search(node.right, goal, limit, depth + 1)
    return found_in_right
# Создание дерева и установка значений
root = BinaryTreeNode(
    1,
    BinaryTreeNode(25, None, BinaryTreeNode(45)),
    BinaryTreeNode(35, BinaryTreeNode(55), None),
)
goal = 45
limit = 2
# Вызов функции поиска
result = depth_limited_search(root, goal, limit)
if result is not None:
    print(f"Цель найдена: {result}")
else:
    print("Цель не найдена")
