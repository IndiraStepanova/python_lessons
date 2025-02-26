nickname = input()
if (
        nickname.startswith('@')
        and (5 <= len(nickname) <= 15)
        and nickname[1:].isalnum()
        and nickname == nickname.lower()
):
    print("Correct")
else:
    print("Incorrect")

