import itertools
import numpy as np

# Fungsi untuk membuat matriks jarak antar titik
def distance_matrix(locations):
    n = len(locations)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = np.linalg.norm(np.array(locations[i]) - np.array(locations[j]))
    return dist_matrix

# Fungsi untuk menghitung total jarak dari rute
def total_distance(route, dist_matrix):
    return sum(dist_matrix[route[i-1]][route[i]] for i in range(len(route)))

# Implementasi Brute Force untuk TSP
def brute_force_tsp(dist_matrix):
    n = len(dist_matrix)
    min_route = None
    min_distance = float('inf')
    all_points = list(range(1, n))
    
    for perm in itertools.permutations(all_points):
        current_route = [0] + list(perm) + [0]  # Mulai dan kembali ke titik awal
        current_distance = total_distance(current_route, dist_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            min_route = current_route
    
    return min_route, min_distance

# Main function to run the Brute Force Algorithm
def main():
    # Contoh lokasi titik pengumpulan sampah (koordinat x, y)
    locations = [(2, 3), (5, 7), (8, 3), (12, 8), (3, 8)]

    # Matriks jarak antar titik
    dist_matrix = distance_matrix(locations)

    # Rute optimal menggunakan Brute Force Algorithm
    brute_force_route, brute_force_distance = brute_force_tsp(dist_matrix)
    print("Rute optimal dengan Brute Force Algorithm:", brute_force_route)
    print(f"Total jarak dengan Brute Force Algorithm: {brute_force_distance:.2f} meter")

    # Cetak semua titik yang dilalui
    print("Titik yang dilalui:")
    for i in range(len(brute_force_route) - 1):
        start, end = brute_force_route[i], brute_force_route[i + 1]
        print(f"Truk bergerak dari titik {start} ke titik {end} dengan jarak {dist_matrix[start][end]:.2f} meter")

if __name__ == "__main__":
    main()