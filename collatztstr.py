def collatz_sequence(n):
    """Collatz dizisini hesaplayan fonksiyon."""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:  # Sayı çiftse
            n //= 2
        else:  # Sayı tekse
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def test_collatz(limit, max_iterations=1000):
    """
    Collatz hipotezini test etmek için bir fonksiyon.
    Belirli bir sınır (limit) içerisindeki tüm pozitif sayılar için çalışır.
    Eğer bir sayı belirli bir döngüde 1'e ulaşmazsa, bunu rapor eder.
    """
    for i in range(1, limit + 1):
        n = i
        iterations = 0
        while n != 1 and iterations < max_iterations:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            iterations += 1

        if iterations == max_iterations:
            print(f"Sayı {i} için döngü sonlanmadı (muhtemelen 1'e ulaşmıyor).")
            return i  # İlk problemli sayıyı döndür
    print(f"1 ile {limit} arasındaki tüm sayılar hipotezi doğruluyor.")
    return None

# Kullanıcıdan giriş alarak çalıştırma
limit = int(input("Hangi sayıya kadar test etmek istiyorsunuz? "))
result = test_collatz(limit)

if result:
    print(f"Collatz hipotezine uymadığı tespit edilen sayı: {result}")
else:
    print("Tüm test edilen sayılar hipotezi doğruluyor.")
