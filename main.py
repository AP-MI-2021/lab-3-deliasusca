def citire(lst):
    n = int(input('Cate numere sunt:'))
    for i in range (0,n):
        x = input()
        lst.append(x)

def get_longest_div_k(lst, k):
    """
    Toate numerele sunt divizibile cu k (citit).
    :param lst: lista de numere
    :param k: divizorul
    :return: cea mai lunga lista de numere care se divid cu k
    """
    cea_mai_lunga_secventa = []
    secventa_actuala = []
    k = int(k)
    i = 0
    while i < len(lst):
        if int(lst[i]) % k == 0:
            secventa_actuala.append(lst[i])
            i+=1
        else:
            if len(secventa_actuala) > len(cea_mai_lunga_secventa):
                cea_mai_lunga_secventa = secventa_actuala.copy()
            secventa_actuala.clear()
            i+=1
    if len(secventa_actuala) > len(cea_mai_lunga_secventa):
        cea_mai_lunga_secventa = secventa_actuala.copy()
    return cea_mai_lunga_secventa

def test_get_longest_div_k():
    assert get_longest_div_k ([2, 4, 13, 3, 23], 2) == [2, 4]
    assert get_longest_div_k([89, 5, 9, 2, 18], 9) == [9]
    assert get_longest_div_k([41, 57, 13, 3, 23], 2) == []

test_get_longest_div_k()

def citire_k_formare_secventa(lst):
    k = int(input('Introduceti numarul: '))
    print(get_longest_div_k(lst, k))

def get_longest_product_is_odd(lst):
    """
    Produsul numerelor este impar.
    :param lst: lista de numere
    :return: lista de numere a caror produs e impar
    """
    cea_mai_lunga_secventa = []
    secventa_actuala = []
    i = 0
    while i<len(lst):
        if int(lst[i])%2==1:
            secventa_actuala.append(lst[i])
            i+=1
        else:
            if len(secventa_actuala) > len(cea_mai_lunga_secventa):
                cea_mai_lunga_secventa = secventa_actuala.copy()
            secventa_actuala.clear()
            i += 1
    if len(secventa_actuala) > len(cea_mai_lunga_secventa):
        cea_mai_lunga_secventa = secventa_actuala.copy()
    return cea_mai_lunga_secventa

def test_get_longest_product_is_odd():
    assert get_longest_product_is_odd([2, 4, 13, 3, 23]) ==[13, 3 , 23]
    assert get_longest_product_is_odd([22, 8, 14, 4, 2]) == []
    assert get_longest_product_is_odd([67, 3, 53]) == [67, 3, 53]

test_get_longest_product_is_odd()

def secventa_produs_impar(lst):
    print(get_longest_product_is_odd(lst))

def numar_puterea_k(x, k):
    if x == 1 or k == 1:
        return True
    for i in range(2, int(int(x)/2)):
        if int(x)%i == 0:
            p = 1
            for j in range(0,int(k)):
                p*=i
            if p == x:
                return True
    return False

def test_numar_puterea_k():
    assert numar_puterea_k(1, 7)== True
    assert numar_puterea_k(16, 1) == True

test_numar_puterea_k()

def get_longest_powers_of_k(lst, k):
    """
    Toate numerele se pot scrie ca x**k, k citit, x întreg pozitiv.
    :param lst: lista de numere
    :param k:
    :return:
    """
    cea_mai_lunga_secventa = []
    secventa_actuala = []
    i = 0
    while i < len(lst):
        if numar_puterea_k(int(lst[i]), k) == 1:
            secventa_actuala.append(lst[i])
            i += 1
        else:
            if len(secventa_actuala) > len(cea_mai_lunga_secventa):
                cea_mai_lunga_secventa = secventa_actuala.copy()
            secventa_actuala.clear()
            i += 1
    if len(secventa_actuala) > len(cea_mai_lunga_secventa):
        cea_mai_lunga_secventa = secventa_actuala.copy()
    return cea_mai_lunga_secventa

def test_get_longest_powers_of_k():
    assert get_longest_powers_of_k([27, 11, 6, 4, 2], 3) == [27]
    assert get_longest_powers_of_k([5, 8, 7, 11], 2) == []
    assert get_longest_powers_of_k([3, 16, 66, 9, 5], 2) == [16]

test_get_longest_powers_of_k()

def formare_secventa_puterea_k(lst):
    k = int(input('Introduceti puterea: '))
    print(get_longest_powers_of_k(lst, k))

def afisare_optiuni():
    print('1 - Citeste datele. \n'
          '2 - Afiseaza cea mai lunga secventa de numere divizibile cu un numar citit. \n'
          '3 - Afiseaza cea mai lunga secventa de numere care au produsul impar. \n'
          '4 - Afiseaza cea mai lunga secventa de numere care pot fi scrise la puterea introdusa. \n'
          'x - Iesi din aplicatie.')

def meniu():
    lst = []
    optiuni = {1: citire, 2: citire_k_formare_secventa, 3: secventa_produs_impar, 4:formare_secventa_puterea_k}
    while True:
        afisare_optiuni()
        optiune = input('Introduceti optiunea:')
        if optiune == 'x':
            break
        optiune = int(optiune)
        optiuni[optiune](lst)

if __name__ == '__main__':
    meniu()

