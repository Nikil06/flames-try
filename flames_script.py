import random
import time

commentTextPath = 'Assets/Data/Comments List.txt'

flamesAcronym = ['Friends', 'Lovers', 'Affectionate', 'Marriage', 'Enemies', 'Siblings']
replaceChar = '^'


def ConvertName(_name: str) -> list:
    output_str = _name.lower()
    output_str = output_str.replace(' ', '')

    output_lst = list(output_str)
    return output_lst


def removeItemFromList(_list: list, _replaceItem) -> list:
    retList = []

    for item in _list:
        if item != _replaceItem:
            retList.append(item)

    return retList


def CreateCommentsList(_path: str):
    file = open(_path, 'r')

    data = file.read()

    commentsList = data.replace('\n', '').split('^')

    sliceIndex = []

    for i in range(len(commentsList[:])):
        line = commentsList[i]
        if line.__contains__('#'):
            commentsList[i] = '*'
            if line.__contains__('*'):
                sliceIndex.append(i)

    commentsList = removeItemFromList(commentsList, '*')

    F_comments = commentsList[(sliceIndex[0] - 1):(sliceIndex[1] - 2)]
    L_comments = commentsList[(sliceIndex[1] - 2):(sliceIndex[2] - 3)]
    A_comments = commentsList[(sliceIndex[2] - 3):(sliceIndex[3] - 4)]
    M_comments = commentsList[(sliceIndex[3] - 4):(sliceIndex[4] - 5)]
    E_comments = commentsList[(sliceIndex[4] - 5):(sliceIndex[5] - 6)]
    S_comments = commentsList[(sliceIndex[5] - 6):(sliceIndex[6] - 7)]

    retList = [F_comments, L_comments, A_comments, M_comments, E_comments, S_comments]

    return retList


def getEliminatedListCount(_list1: list, _list2: list) -> int:
    for i in range(len(_list1)):
        j = 0

        while j < len(_list2):

            if _list1[i] == _list2[j] and _list1[i] != replaceChar:
                _list1[i] = replaceChar
                _list2[j] = replaceChar

            j = j + 1

    _list1 = removeItemFromList(_list1, replaceChar)
    _list2 = removeItemFromList(_list2, replaceChar)

    count = len(_list1) + len(_list2)

    return count


def getRelationshipIndex(_flameCount: int) -> int:
    flames_list = list(flamesAcronym)

    pos = 0

    while len(flames_list) > 1:
        for i in range(_flameCount):
            pos += 1
            if pos > len(flames_list):
                pos = 1

        flames_list.remove(flames_list[pos - 1])
        pos -= 1

    result = flames_list[0]

    return flamesAcronym.index(result)

    print('Error in Getting Relationship Index')


def getRandComment(_relationIndex: int, _commentList: list) -> str:
    randComment = random.choice(_commentList[_relationIndex])
    return randComment


def flameTest(_name1: str, _name2: str):
    print()
    candidate1 = _name1
    candidate2 = _name2

    list1 = ConvertName(candidate1)
    list2 = ConvertName(candidate2)

    flameCount = getEliminatedListCount(list1, list2)

    index = getRelationshipIndex(flameCount)

    retList = [flamesAcronym[index], getRandComment(index, comment_list)]

    return retList


def gameCode():
    print('')
    candidate1 = input('Candidate 1:- ')
    candidate2 = input('Candidate 2:- ')

    results = flameTest(candidate1, candidate2)

    print('The FLAME Test results between', candidate1, '&', candidate2, 'is:-', results[0])

    print('Comments:- ' + results[1])


if __name__ == "__main__":
    print("Welcome to the Test Of F.L.A.M.E.S.")
    comment_list = CreateCommentsList(commentTextPath)
    playing = True


    def Credits():
        print('\nCredits:- Nikil and Balaji')


    def askForNext():
        while True:
            Input = input('\n' + "Are you ready for another Test [Y/N]:- ").upper()[0]

            if Input == 'Y':
                return True
            elif Input == 'N':
                Credits()
                time.sleep(1.5)
                return False
            else:
                print('Error:- Input not Valid, please enter again (just enter "y"/"Y" or "n"/"N")')


    while playing:
        gameCode()
        playing = askForNext()
