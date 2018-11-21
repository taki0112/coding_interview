def solution(phoneBook):
    phoneBook = sorted(phoneBook)


    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

phone_book = ['12','123','1235','567','88']
x = solution(phone_book)
print(x)