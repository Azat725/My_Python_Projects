default_level_experience = 200

def is_level_up(*, current_experience: int, gained_experience: int):
    total_experience = current_experience + gained_experience
    level_up = False
    
    if total_experience >= default_level_experience:
        level_up = True
        
    return level_up

print(is_level_up(current_experience = 150, gained_experience = 60)) #True
print(is_level_up(current_experience = 130, gained_experience = 20)) #False