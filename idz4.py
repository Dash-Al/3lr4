#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# C помощью алгоритма поиска с ограничением глубины найдем минимальное расстояние между начальным и конечным пунктами
import itertools

def calculate_total_distance(route, distance_matrix):
    """Вычисление общей дистанции для данного маршрута."""
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    # Добавляем расстояние обратно к начальной точке
    total_distance += distance_matrix[route[-1]][route[0]]
    return total_distance

def traveling_salesman(distance_matrix):
    """Решение задачи коммивояжера методом полного перебора."""
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    min_distance = float('inf')
    best_route = None
    # Генерация всех возможных маршрутов
    for route in itertools.permutations(cities):
        current_distance = calculate_total_distance(route, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route
    return best_route, min_distance

# Пример использования
if __name__ == "__main__":
    # Матрица расстояний между городами для 10 узлов
    distance_matrix = [
        [0, 222, 234, 420, 498, 677, 853, 555, 457, 455],
        [222, 0, 59, 545, 732, 456, 17, 109, 983, 833],
        [234, 59, 0, 232, 183, 100, 938, 78, 73, 284],
        [420, 545, 232, 0, 37, 274, 112, 82, 877, 458],
        [498, 732, 183, 37, 0, 883, 755, 560, 555, 101],
        [677, 456, 100, 274, 883, 0, 768, 643, 638, 184],
        [853, 17, 938, 112, 755, 768, 0, 462, 674, 654],
        [555, 109, 78, 82, 560, 643, 462, 0, 212, 666],
        [457, 983, 73, 877, 555, 638, 674, 212, 0, 656],
        [455, 833, 284, 458, 101, 184, 654, 666, 656, 0],
    ]

    best_route, min_distance = traveling_salesman(distance_matrix)
    print(f"Лучший маршрут: {best_route}")
    print(f"Минимальное расстояние: {min_distance}")
