user_roles = ("admin", "editor", "viewer")

print("admin" in user_roles)
print("writer" in user_roles)
print(type(user_roles))

#распаковка картежа

role_1, role_2, role_3 = user_roles
role_1, role_2, _ = user_roles

print(role_1)
print(role_3)