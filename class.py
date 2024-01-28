class Character: #класс наследник
    
    
    def __init__(self, level: int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level
        
        
    def attack(self, *, target: "Character"):
        target.got_damage(damage = self.attack_power)
        
    def got_damage(self, *, damage: int) -> None:
        damage = (100 - self.defence) / 100
        damage = round(damage)  #round округляет float
        self.health_points -= damage

        
    def is_alive(self) -> bool:
        return self.health_points > 0
    
    
    @property
    def max_health_points(self) -> int:
        return self.level * self.base_health_points   
    
    @property
    def health_points_percent(self) -> int:
        return 100 * self.health_points / self.max_health_points
    
    @property
    def defence(self) -> int:
        defence = self.base_defence * self.level
        return defence
        
        
    def __str__(self) -> str:
        return f"{self.character_name} level: {self.level}, health points: {self.health_points}"
    
    
class Ork(Character): #наследуемый класс
    base_defence = 15
    base_health_points = 100
    base_attack_power = 10
    character_name = "Ork"
    
    @property
    def defence(self) -> int:
        defence = super().defence
        if self.health_points < 50:
            defence *= 3
        return defence
    
class Elf(Character): #наследуемый класс
    base_defence = 10
    base_health_points = 50
    base_attack_power = 20
    character_name = "Elf"
    
    @property
    def attack(self, *, target: "Character"):
        attack_power = self.attack_power
        if target.health_points_percent() < 30:
            attack_power = self.attack_power * 3
        target.got_damage(damage = self.attack_power)
    

def fight(*, character_1: Character, character_2: Character) -> None:
    while character_1.is_alive() and character_2.is_alive():
        character_1.attack(target=character_2)
        if character_2.is_alive():
            character_2.attack(target=character_1)
        
    print(f"Character 1: {character_1} is alive {character_1.is_alive()}")
    print(f"Character 2: {character_2} is alive {character_2.is_alive()}")
    
ork = Ork(level = 1)
elf = Elf(level = 1)

fight(character_1 = ork, character_2 = elf)