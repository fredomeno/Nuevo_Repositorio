def test_login(user, password):
    if user == "admin" and password == "1234":
        print("SUCCESS")
    else:
        print("FAILURE")

test_login("admin", "1234")
test_login("user", "0000")
