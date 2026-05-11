
class AgacDugumu:
    def __init__(self, veri):
        self.veri = veri
        self.sol = None
        self.sag = None

def bst_ekle(kok, deger):
    if kok is None:
        return AgacDugumu(deger)
    if deger < kok.veri:
        kok.sol = bst_ekle(kok.sol, deger)
    else:
        kok.sag = bst_ekle(kok.sag, deger)
    return kok

def bst_ara(kok, aranan):
   
    if kok is None or kok.veri == aranan:
        return kok
    if aranan < kok.veri:
        return bst_ara(kok.sol, aranan)
    return bst_ara(kok.sag, aranan)


class Yigin: # Stack
    def __init__(self):
        self.veriler = []
    def push(self, eleman):
        self.veriler.append(eleman)
    def pop(self):
        return self.veriler.pop()

class Kuyruk: # Queue
    def __init__(self):
        self.veriler = []
    def enqueue(self, eleman):
        self.veriler.append(eleman)
    def dequeue(self):
        return self.veriler.pop(0)


class BasitSozluk:
    def __init__(self):
        self.boyut = 5
        self.tablo = [[] for _ in range(self.boyut)]

    def hash_bul(self, anahtar):
      
        return len(str(anahtar)) % self.boyut

    def ekle(self, anahtar, deger):
        index = self.hash_bul(anahtar)
  
        self.tablo[index].append([anahtar, deger])


class Graf:
    def __init__(self):
        self.liste = {}

    def bag_olustur(self, u, v):
        if u not in self.liste:
            self.liste[u] = []
        self.liste[u].append(v)

    def bfs_ara(self, baslangic):
        ziyaret_edildi = []
        kuyruk = [baslangic]
        while kuyruk:
            dugum = kuyruk.pop(0)
            if dugum not in ziyaret_edildi:
                print(dugum, end=" ")
                ziyaret_edildi.append(dugum) # Komşuları kuyruğa ekle
                
                if dugum in self.liste:
                    kuyruk.extend(self.liste[dugum])

    def dfs_ara(self, dugum, ziyaret_edildi=None):
        if ziyaret_edildi is None:
            ziyaret_edildi = []
        if dugum not in ziyaret_edildi:
            print(dugum, end=" ")
            ziyaret_edildi.append(dugum)
            if dugum in self.liste:
                for komsur in self.liste[dugum]:
                    self.dfs_ara(komsur, ziyaret_edildi)


print("--- BST Test ---")
kok = AgacDugumu(50)
bst_ekle(kok, 30)
bst_ekle(kok, 70)
sonuc = bst_ara(kok, 30)
print("30 bulundu mu:", "Evet" if sonuc else "Hayır")



print("\nStack Queue Test")
s = Yigin()
s.push("Veri 1")
print("Stackten çıkan:", s.pop())

k = Kuyruk()
k.enqueue("Sıra 1")
k.enqueue("Sıra 2")
print("Kuyruktan çıkan:", k.dequeue())

print("\nHash Map Test")
szlk = BasitSozluk()
szlk.ekle("Ad", "Ömer")
print("Tablo durumu:", szlk.tablo)

print("\nGraf Test")
g = Graf()
g.bag_olustur("A", "B")
g.bag_olustur("A", "C")
g.bag_olustur("B", "D")

print("BFS Çıktısı:")
g.bfs_ara("A")
print("\nDFS Çıktısı:")
g.dfs_ara("A")