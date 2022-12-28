class Hero:
    name = "Kuuhaku"
    hp =  0
    damage = 0
    defense = 0

    def __init__(self, name, hp, damage, defense):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defense = defense

    def attack(self, target):
        target.hp = target.hp - self.damage
        print("sisa hp ", target.name, "=", target.hp)

#inisialisasi class hero
hero1 = Hero("Hayabuset", 200, 5000, 0)
hero2 = Hero("Atlanto", 6000, 30, 4500)

hero2.attack(hero1)