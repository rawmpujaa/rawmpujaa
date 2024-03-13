#Program by 22343010_Rawim Puja Aviola
def optimal_binary_search_tree(P):
    n = len(P)
    
    # Inisialisasi tabel C, R, dan penambahan dummy entry di P
    C = [[0] * (n + 2) for _ in range(n + 2)]  # Perlu diperpanjang dengan 1 elemen tambahan
    R = [[0] * n for _ in range(n)]
    for i in range(1, n + 1):
        C[i][i - 1] = 0
        C[i][i] = P[i - 1]
        R[i - 1][i - 1] = i
        C[i + 1][i] = 0
    
    # Perhitungan tabel C dan R
    for d in range(1, n):
        for i in range(1, n - d + 1):
            j = i + d
            minval = float('inf')
            for k in range(i, j + 1):
                if C[i][k - 1] + C[k + 1][j] < minval:
                    minval = C[i][k - 1] + C[k + 1][j]
                    kmin = k
            R[i - 1][j - 1] = kmin
            sum_P = sum(P[i - 1:j])
            C[i][j] = minval + sum_P
    
    # Mengembalikan jumlah perbandingan minimum dan tabel R
    return C[1][n], R

# Contoh penggunaan
P = [0.1, 0.2, 0.3, 0.1, 0.15, 0.15]
min_comparisons, R_table = optimal_binary_search_tree(P)
print("Jumlah perbandingan minimum:", min_comparisons)
print("Tabel R:")
for row in R_table:
    print(row)
