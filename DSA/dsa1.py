
class Dugum:
    def __init__(self, veri):
        self.veri = veri
        self.sonraki = None

class BagliListe:
    def __init__(self):
        self.bas = None

    def ekle(self, veri):
        yeni_dugum = Dugum(veri)
        if self.bas is None:
            self.bas = yeni_dugum
            return
        son = self.bas
        while son.sonraki:
            son = son.sonraki
        son.sonraki = yeni_dugum

    def yazdir(self):
        su_an = self.bas
        while su_an:
            print(su_an.veri)
            su_an = su_an.sonraki


class Yigin:
    def __init__(self):
        self.liste = []
    def ekle(self, veri):
        self.liste.append(veri)
    def cikar(self):
        return self.liste.pop()


class Kuyruk:
    def __init__(self):
        self.liste = []
    def ekle(self, veri):
        self.liste.append(veri)
    def cikar(self):
        return self.liste.pop(0)


class AgacDugumu:
    def __init__(self, veri):
        self.sol = None
        self.sag = None
        self.veri = veri

def agaca_ekle(kok, veri):
    if kok is None:
        return AgacDugumu(veri)
    if veri < kok.veri:
        kok.sol = agaca_ekle(kok.sol, veri)
    else:
        kok.sag = agaca_ekle(kok.sag, veri)
    return kok


class Graf:
    def __init__(self):
        self.yapi = {}
    
    def bag_ekle(self, basla, bitis):
        if basla not in self.yapi:
            self.yapi[basla] = []
        self.yapi[basla].append(bitis)


print("\nLinked List")
bl = BagliListe()
bl.ekle(10)
bl.ekle(20)
bl.yazdir()

print("\nStack ve Queue")
y = Yigin()
y.ekle("ilk")
y.ekle("son")
print(y.cikar()) # son çıkar

k = Kuyruk()
k.ekle("ilk")
k.ekle("son")
print(k.cikar()) # ilk çıkar

print("\nTree")
kok = AgacDugumu(50)
agaca_ekle(kok, 30)
agaca_ekle(kok, 70)
print("Kök:", kok.veri)
print("Sol:", kok.sol.veri)
print("Sağ:", kok.sag.veri)

print("\nGraph")
g = Graf()
g.bag_ekle("A", "B")
g.bag_ekle("A", "C")