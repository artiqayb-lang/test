class jonzot:
    def __init__(self, nomi):
        self.nomi = nomi


class it(jonzot):
    def __str__(self):
        return f"Bu it nomli class"

    def tezlik(self):
        return f"{self.nomi} --- bu hayvon tez yuguradi"

    class SHer(jonzot):
        def qirol(self):
            return f"{self.nomi} O'rmon va hayvonlar qiroli"

b = sher('')
a = it('maks')
print(a.tezlik())
print(b.qirol())