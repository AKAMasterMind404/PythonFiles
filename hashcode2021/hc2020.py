import operator


def bookInLibrary(lib, book):
    return book in lib[3]


def worth(numbooks, bookscore, shipcapacity, signuptime):
    return (bookscore / numbooks) * (shipcapacity / signuptime)


# def LibraryPoints(books):
#     return sum(booksScores[i] for i in books)


def removeBook(book):
    global libraryData

    for lib in libraryData:
        lib[2].remove(book)


def signUp(lib):
    global days
    days -= lib[1][1]


def scan(libraryData):
    global days
    global scannedBooks

    if days > 0:
        z = 0
        days -= libraryData[1][1] # scan time for a library
        books = libraryData[2]
        scanRange = libraryData[1][2]

        while days > 0 and z + scanRange < len(books):
            for book in books[z:z+scanRange]:
                if book not in scannedBooks:
                    print(book, end=' ')
                    scannedBooks.append(book)
            days -= 1
            z += 1
        print()


with open('20ip.txt', 'r') as ip:
    books, libraries, days = map(int, ip.readline().strip().split())
    print(books, libraries, days)
    scannedBooks = []
    booksScores = []
    scores = list(map(int, ip.readline().strip().split()))
    print(scores)
    libraryData = []
    for i in range(books):
        booksScores.append([scores[i]])
    print('###########')
    print(sorted(booksScores,key=operator.itemgetter(1),reverse=True))
    for i in range(libraries):
        numbooks, signuptime, shipcapacity = list(map(int, ip.readline().strip().split()))
        books_in_lib = list(set(list(map(int, ip.readline().strip().split()))))
        books_in_lib = sorted(books_in_lib,key=operator.itemgetter(1),reverse=True)
        library_points = sum([scores[i] for i in books_in_lib])
        libraryData.append(
            [
                i,  # 0 Library number
                [numbooks, signuptime, shipcapacity],  # 1
                books_in_lib,  # 2 Books list
                library_points,  # 3 Library points
                worth(numbooks, library_points, shipcapacity, signuptime),  # 4 Library Worth
                False  # 5 Whether a library is signed up or not
            ])
        # print(numbooks, signuptime, shipcapacity)
        # print(books)

        # zeroth index = library number
        # first index = numberofbooks,capacity,shipcapacity
        # second index = books in that library
        # third index = value of all the books in a library
        # fourth index = worth

    libraries_by_priority = sorted(libraryData, key=operator.itemgetter(4), reverse=True)

    index = 0
    while days > 0:
        scan(libraries_by_priority[index])