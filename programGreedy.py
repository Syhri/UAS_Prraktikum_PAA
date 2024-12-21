import numpy as np

# Fungsi untuk membuat matriks jarak antar titik
def distance_matrix(locations):
    n = len(locations)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = np.linalg.norm(np.array(locations[i]) - np.array(locations[j]))
    return dist_matrix

# Implementasi Greedy Algorithm untuk TSP dengan informasi lebih detail
def greedy_tsp(dist_matrix):
    n = len(dist_matrix)
    visited = [False] * n
    route = [0]  # Mulai dari titik pertama
    visited[0] = True
    visited_points = [(0, 0)]  # Simpan titik awal
    total_distance = 0

    for _ in range(n - 1):
        last = route[-1]
        next_city = None
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and dist_matrix[last][i] < min_dist:
                min_dist = dist_matrix[last][i]
                next_city = i
        route.append(next_city)
        visited[next_city] = True
        visited_points.append((last, next_city))  # Simpan titik yang dikunjungi
        total_distance += min_dist

    # Kembali ke titik awal
    route.append(0)
    total_distance += dist_matrix[route[-2]][0]
    visited_points.append((route[-2], 0))  # Simpan titik akhir
    
    return route, visited_points, total_distance

# Main function to run the Greedy Algorithm
def main():
    # Contoh lokasi titik pengumpulan sampah (koordinat x, y)
    locations = [(2, 3), (5, 7), (8, 3), (12, 8), (3, 8)]

    # Matriks jarak antar titik
    dist_matrix = distance_matrix(locations)

    # Rute optimal menggunakan Greedy Algorithm
    greedy_route, visited_points, total_distance = greedy_tsp(dist_matrix)
    print("Rute optimal dengan Greedy Algorithm:", greedy_route)
    print(f"Total jarak dengan Greedy Algorithm: {total_distance:.2f} meter")

    # Cetak semua titik yang dilalui
    print("Titik yang dilalui:")
    for start, end in visited_points:
        print(f"Truk bergerak dari titik {start} ke titik {end} dengan jarak {dist_matrix[start][end]:.2f} meter")

if __name__ == "__main__":
    main()