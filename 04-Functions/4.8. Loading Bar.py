number = int(input())

loading_bar = ['.'] * 10
number_of_percentage = number // 10
symbol = "%"

loading_bar[0:number_of_percentage] = [symbol] * number_of_percentage
loading_bar = ''.join(loading_bar)
if symbol * 10 in loading_bar:
    print(f'100% Complete!')
    print(f'[{loading_bar}]')
else:
    print(f'{number}% [{loading_bar}]')
    print(f"Still loading...")
