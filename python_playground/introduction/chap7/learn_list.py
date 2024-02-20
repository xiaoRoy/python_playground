def learn_for_loop_break():
    cheeses = ['brie', 'gjetost', 'havarti', 'x']
    for cheese in cheeses:
        if cheese.startswith('x'):
            print(f'This {cheese} starts with x')
            break
        else:
            print(cheese)
    else:
        print('Not Found')


learn_for_loop_break()
