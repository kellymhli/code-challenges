def find_lonely_pixel(picture) -> int:
    """
    Return the number of lonely black pixels in the picture.
    A lonely pixel is defined as the only occurrence of B in its row and col.
    """
    res = 0
    for row in picture:
        if row.count('B') == 1:
            i = row.index('B')
            col_count = 0
            for j in range(len(picture)):
                if picture[j][i] == 'B':
                    col_count += 1
                    if col_count > 1:
                        break
            if col_count == 1:
                res += 1
    return res

print(find_lonely_pixel([["W","W","B"],["W","B","W"],["B","W","W"]]))  # 3
print(find_lonely_pixel([["B","W","W","W","W","B","W","B","B","W"],["B","B","B","W","W","W","B","W","B","W"],["B","B","B","B","W","W","W","B","W","W"],["B","W","W","B","W","B","B","W","W","W"],["W","W","B","W","B","B","B","W","B","B"],["W","B","B","W","W","W","B","W","W","W"],["B","W","W","B","B","B","W","W","W","W"],["W","W","W","B","B","B","B","W","W","W"],["W","W","B","B","W","W","W","W","B","W"],["W","W","W","B","B","B","W","W","W","B"]]))  # 0