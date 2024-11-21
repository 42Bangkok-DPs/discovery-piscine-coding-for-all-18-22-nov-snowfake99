def can_attack(piece, position, king_pos, board):
    """
    ตรวจสอบว่าตัวหมากสามารถโจมตี King ได้หรือไม่
    """
    directions = {
        'P': [(-1, -1), (-1, 1)],  # Pawn โจมตีเฉียงซ้ายบนและขวาบน
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],  # Bishop โจมตีแนวทแยง
        'R': [(0, -1), (0, 1), (-1, 0), (1, 0)],  # Rook โจมตีแนวตั้งและแนวนอน
        'Q': [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]  # Queen รวม Bishop และ Rook
    }

    if piece not in directions:
        return False

    for dr, dc in directions[piece]:
        r, c = position
        if piece == 'P':  # Pawn โจมตีได้แค่ 1 ช่อง
            r += dr
            c += dc
            if (r, c) == king_pos:
                return True
            continue

        while 0 <= r < len(board) and 0 <= c < len(board[r]):  # เดินไปเรื่อย ๆ ตามทิศทาง
            r += dr
            c += dc
            if (r, c) == king_pos:
                return True
            if 0 <= r < len(board) and 0 <= c < len(board[r]) and board[r][c] != '.':
                break

    return False


def checkmate(board):
    """
    ตรวจสอบว่ามีตัวหมากใดสามารถโจมตี King ได้หรือไม่
    """
    # หาตำแหน่ง King
    king_pos = None
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        return "Fail"  # ไม่มี King บนกระดาน

    # ตรวจสอบตัวหมากทั้งหมดบนกระดาน
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell in "PBRQ":  # ตัวหมากที่สามารถโจมตีได้
                if can_attack(cell, (i, j), king_pos, board):
                    return "Success"  # พบการโจมตีแล้ว

    return "Fail"  # ไม่มีตัวหมากใดโจมตี King ได้
