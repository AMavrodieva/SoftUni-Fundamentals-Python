def is_ticket_jackpot(ticket):
    for symbol in winning_symbol:
        if symbol in ticket:
            if ticket.count(symbol) == 20:
                print(f'ticket "{ticket}" - {10}{symbol} Jackpot!')
                return True
    return False


def is_ticket_winner(ticket):
    left_side = ticket[0:10]
    right_side = ticket[10:]
    for symbol in winning_symbol:
        if symbol * 6 in left_side and symbol * 6 in right_side:
            left_side_count = left_side.count(symbol)
            right_side_count = right_side.count(symbol)
            matched_symbol = min(left_side_count, right_side_count)
            if symbol * 7 in left_side:
                if symbol * 7 in right_side:
                    matched_symbol = min(left_side.count(symbol), right_side.count(symbol))
                    if symbol * 8 in left_side:
                        if symbol * 8 in right_side:
                            matched_symbol = min(left_side.count(symbol), right_side.count(symbol))
                            if symbol * 9 in left_side:
                                if symbol * 9 in right_side:
                                    matched_symbol = min(left_side.count(symbol), right_side.count(symbol))
                                    if symbol * 10 in left_side:
                                            matched_symbol = min(left_side.count(symbol), right_side.count(symbol))
                                else:
                                    matched_symbol -= 1
                            else:
                                matched_symbol -= 1
                        else:
                            matched_symbol -= 1
                    else:
                        matched_symbol -= 1
                else:
                    if not matched_symbol == 6:
                        matched_symbol -= 1
            else:
                if not matched_symbol == 6:
                    matched_symbol -= 1
            print(f'ticket "{ticket}" - {matched_symbol}{symbol}')
            return True
    return False


text = ["".join(el.split()) for el in input().split(",")]
#text = [el.strip() for el in input().split(", ")]
winning_symbol = ["@", "#", "$", "^"]

for ticket in text:
    if not len(ticket) == 20:
        print(f'invalid ticket')
        continue
    if is_ticket_jackpot(ticket):
        continue
    if is_ticket_winner(ticket):
        continue
    else:
        print(f'ticket "{ticket}" - no match')

