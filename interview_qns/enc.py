def decodeString(numberOfRows, encodedString):
    # Write your code here
    # find length of encodedString n
    # find cols needed cols = n / numberOfRows
    # construct 2d array of [numberOfRows][cols]
    # loop through array diagonally join each word and add space if met
    #ens = 'mnes__ya_____mi' rows = 3
    
    n = len(encodedString)
    cols = n // numberOfRows
    matrix = []
    encodedString = list(encodedString)
    for r in range(numberOfRows):
        for c in range(cols):
            matrix.append([encodedString[c]])
            encodedString.remove(encodedString[c])
    print(matrix)

en = "mnes__ya_____mi"
rows = 3

decodeString(rows, en)