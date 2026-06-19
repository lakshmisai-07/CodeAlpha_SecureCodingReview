username = input("Enter Username: ")
password = input("Enter Password: ")

query = "SELECT * FROM users WHERE username=? AND password=?"

print("\nSecure Query:")
print(query)

print("\nSQL Injection Prevented")