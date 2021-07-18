dict_ = {"Joseph":"W@12"}
string_ = input("To see your password write your username correctly : ").strip().title()

if string_ == "Joseph":
    print(f"Hello, {string_}!The password is : {dict_[string_]}")
else:
    print(f"Hello, {string_}.See you later.")
