# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Metode 1: Integrasi Reimann
def reimann_integration(f, a, b, N):
    dx = (b - a) / N
    total = 0.0
    for i in range(N):
        x = a + i * dx
        total += f(x) * dx
    return total

# Fungsi untuk menghitung galat RMS
def calculate_rms_error(estimate, reference):
    return ((estimate - reference) ** 2) ** 0.5

# Fungsi untuk mengukur waktu eksekusi (dengan menggunakan modul `time`)
def measure_time(func, *args):
    import time
    start_time = time.process_time()
    result = func(*args)
    end_time = time.process_time()
    elapsed_time = end_time - start_time
    return result, elapsed_time

# Nilai referensi untuk pi
pi_ref = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Menyimpan hasil galat RMS dan waktu eksekusi
errors = []
times = []

for N in N_values:
    pi_estimate, elapsed_time = measure_time(reimann_integration, f, 0, 1, N)
    error = calculate_rms_error(pi_estimate, pi_ref)
    
    errors.append(error)
    times.append(elapsed_time)
    
    print(f'N = {N}:')
    print(f'Estimated Pi = {pi_estimate}')
    print(f'Error (RMS) = {error}')
    print(f'Elapsed Time = {elapsed_time} seconds')
    print('----------------------------------------')

# Hasil galat dan waktu eksekusi untuk tiap N
print('Summary of errors and times:')
for N, error, t in zip(N_values, errors, times):
    print(f'N = {N}, Error (RMS) = {error}, Elapsed Time = {t} seconds')