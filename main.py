def test_login(user, password):
    if user == "admin" and password == "1234":
        print("Login successful")
    else:
        print("Login failed")

test_login("admin", "1234")
test_login("user", "0000")
