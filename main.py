from colorama import Fore

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Pembagian dengan nol tidak diperbolehkan."

print(Fore.RED + "██╗  ██╗ █████╗ ██╗     ██╗  ██╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ ")
print("██║ ██╔╝██╔══██╗██║     ██║ ██╔╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗")
print("█████╔╝ ███████║██║     █████╔╝ ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝")
print("██╔═██╗ ██╔══██║██║     ██╔═██╗ ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗")
print("██║  ██╗██║  ██║███████╗██║  ██╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║")
print("╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝\n" + Fore.RESET)
print(Fore.BLUE + "Pilih operasi:")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi" + Fore.RESET)

pilihan = input(Fore.LIGHTMAGENTA_EX + "Masukkan pilihan (1/2/3/4): ")

angka1 = float(input(Fore.YELLOW + "Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
print(Fore.RESET)

if pilihan == '1':
    print(f"{Fore.CYAN}Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")
    print(Fore.RESET)
elif pilihan == '2':
    print(f"{Fore.CYAN}Hasil: {angka1} - {angka2} = {kurang(angka1, angka2)}")
    print(Fore.RESET)
elif pilihan == '3':
    print(f"{Fore.CYAN}Hasil: {angka1} * {angka2} = {kali(angka1, angka2)}")
    print(Fore.RESET)
elif pilihan == '4':
    print(f"{Fore.CYAN}Hasil: {angka1} / {angka2} = {bagi(angka1, angka2)}")
    print(Fore.RESET)
else:
    print(Fore.RED + "Pilihan tidak valid.")
    print(Fore.RESET)
