import random

class Player:
    def __init__(self):
        self.energy = 100
        self.health = 100
        self.food = 3
        self.time = 12

    def rest(self):
        if self.food > 0:
            self.food -= 1
            self.energy += 30
            if self.energy > 100:
                self.energy = 100
            print("Puhkasid ja taastasid energiat.")
        else:
            print("Sul pole toitu, et puhata.")

    def heal(self):
        if self.energy >= 20:
            self.energy -= 20
            self.health += 25
            if self.health > 100:
                self.health = 100
            print("Taastasid tervist.")
        else:
            print("Pole piisavalt energiat tervise taastamiseks.")

    def search_resources(self):
        success = random.randint(1, 100)
        if success <= 40:  
            print("Leidsid 1 toidu.")
            self.food += 1
        elif success <= 70:
            print("Leidsid natuke energiat. +15")
            self.energy += 15
            if self.energy > 100:
                self.energy = 100
        else:
            print("Ei leidnud midagi.")

    def move_forward(self):
        print("Liikusid edasi. Kulu: -15 energia, -1 aeg.")
        self.energy -= 15
        self.decrease_time(1)
        self.random_event(extra=True)

    def stay_put(self):
        print("Jäid paigale. Võid sattuda rünnaku alla.")
        danger = random.randint(1, 100)
        if danger <= 30:  
            print("Sind rünnati ootamatult! Kaotasid 15 tervist.")
            self.health -= 15
        else:
            print("Kõik oli vaikne. Ei juhtunud midagi.")

    def show_status(self):
        print(f"\nTervis: {self.health}")
        print(f"Energia: {self.energy}")
        print(f"Toit: {self.food}")
        print(f"Aega jäänud: {self.time} tundi")

    def decrease_time(self, amount=1):
        self.time -= amount
        if self.time < 0:
            self.time = 0

    def collapse_check(self):
        if self.energy <= 0:
            print("Kukkusid kurnatusest kokku. Kaotasid 10 tervist ja 1 tund.")
            self.health -= 10
            self.decrease_time(1)
            self.energy = 20

    def random_event(self, extra=False):
        events = [
            ("Sind ründas röövel", lambda p: setattr(p, "health", max(p.health - 20, 0))),
            ("Leidsid toitu", lambda p: setattr(p, "food", p.food + 1)),
            ("Said vigastada", lambda p: setattr(p, "health", max(p.health - 10, 0))),
            ("Leidsid energiajooki", lambda p: setattr(p, "energy", min(p.energy + 20, 100))),
            ("Kaotasid toidu", lambda p: setattr(p, "food", max(p.food - 1, 0))),
            ("Öö möödus vaikselt", lambda p: None)
        ]
        if extra:
            print("Liikumise käigus toimus sündmus:")
        else:
            print("Toimus sündmus:")
        msg, effect = random.choice(events)
        print(msg)
        effect(self)

def game_loop():
    player = Player()

    while player.time > 0 and player.health > 0:
        player.show_status()
        print("\nValikud:")
        print("1. Puhka (kasutab 1 toitu, taastab energiat)")
        print("2. Tervise taastamine (kasutab energiat)")
        print("3. Otsi ressursse (% tõenäosus)")
        print("4. Liigu edasi (kulu ja sündmus)")
        print("5. Jää paigale (risk rünnakuks)")
        action = input("Sisesta oma valik (1-5): ")

        if action == "1":
            player.rest()
        elif action == "2":
            player.heal()
        elif action == "3":
            player.search_resources()
            player.energy -= 10
            player.decrease_time()
        elif action == "4":
            player.move_forward()
        elif action == "5":
            player.stay_put()
            player.decrease_time()
        else:
            print("Vale sisestus. Kaotasid aega.")
            player.decrease_time()

        player.collapse_check()

    print("\nMäng on läbi.")
    if player.health <= 0:
        print("Sinu tegelane suri.")
    else:
        print("Öö sai läbi. Sa jäid ellu!")

game_loop()
