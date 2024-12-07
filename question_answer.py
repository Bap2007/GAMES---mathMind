import random
import math

# Functions which returns the question and the answer for each level

#  EASY MODE:   operations + - x and numbers between 2 and 20 (mult: 2 -> 12)
#  MEDIUM MODE: operations + - x / and numbers between 2 and 25 (mult: 2 -> 15)
#  HARD MODE: operations + - x / power(p) square(s) and number between 25 and 150 (mult: 2 -> 25)
#  EXTREME MODE: operations + x p s ln log(l) ≡ (c)




def round_power():
    square_liste = []
    cube_liste = []
    power4_liste = []

    power4 = 1
    cube = 1
    square = 1
    k = 2
    j = 2
    l = 2

    while square < 600:
        square = k ** 2
        square_liste.append(square)
        k += 1
    while cube < 600:
        cube = j ** 3
        cube_liste.append(cube)
        j += 1
    while power4 < 600:
        power4 = l ** 4
        power4_liste.append(power4)
        l += 1


    return square_liste, cube_liste, power4_liste



power_liste = round_power()
SQUARE_LISTE = power_liste[0]
CUBE_LISTE = power_liste[1]
POWER4_LISTE = power_liste[2]



def all_qr(mode):

    global SQUARE_LISTE, CUBE_LISTE, POWER4_LISTE

    special_operation_power = ['²', '³', '⁴', '⁵', '⁶', '⁷', '⁸']
    special_operation_square = ['√', '∛', '∜']
    special_operation_logarithm = ['log₂', 'log₃', 'log₄', 'log₅', 'ln']
    square_liste = SQUARE_LISTE
    cube_liste = CUBE_LISTE
    power4_liste = POWER4_LISTE
    
    

    qr = [None, None]
    operation = []
    question = ''
    answer = 1

    is_power_feasible = True
    is_power_weak = False
    is_congruence_weak = False

    # EASY MODE QR
    if mode == 'easy':           
        operation = ['+', '-', 'x']
        current_operation = random.choice(operation) # choose an operation
        a = random.randint(2, 20)
        b = random.randint(2, 20)

        if current_operation == '+':
            answer = a + b
        elif current_operation == '-':
            while a <= b:
                a, b = random.randint(2, 20), random.randint(2, 20)
            answer = a - b
        else:
            a, b = random.randint(2, 12), random.randint(2, 12)
            answer = a * b

        question = f'{a} {current_operation} {b}'



            
    # MEDIUM MODE QR
    elif mode == 'medium':
        operation = ['+', '-', 'x', '/']
        current_operation = random.choice(operation)
        a = random.randint(2, 25)
        b = random.randint(2, 25)

        if current_operation == '+':
            a, b = random.randint(20, 50), random.randint(15, 70)
            answer = a + b
        elif current_operation == '-':
            while a <= b:
                a, b = random.randint(2, 25), random.randint(2, 25)
            answer = a - b
        elif current_operation == 'x':
            a, b = random.randint(2, 15), random.randint(2, 15)
            answer = a * b
        else:
            while (a%b) != 0:
                a, b = random.randint(2, 100), random.randint(2, 10)
            answer = int(a/b)

        question = f'{a} {current_operation} {b}'


    # HARD MODE QR
    elif mode == 'hard':
        operation = ['+', 'x', '/', 'p', 's']
        probability_weight_h = [20, 15, 15, 23, 27]  
        current_operation = random.choices(operation, weights=probability_weight_h, k=1)
        current_operation = current_operation[0]
        a = random.randint(2, 25)
        b = random.randint(2, 25)

        if current_operation == '+':
            a, b = random.randint(20, 150), random.randint(15, 120)   
            answer = a + b

        elif current_operation == 'x':
            a, b = random.randint(8, 20), random.randint(12, 25)
            answer = a * b
            
        elif current_operation == '/':
            while (a%b) != 0:
                a, b = random.randint(50, 300), random.randint(3, 50)
            answer = int(a/b)

        elif current_operation == 'p':
            current_operation = random.choice(special_operation_power)
            for i in range(len(special_operation_power)):
                if current_operation == special_operation_power[i]:
                    answer = a ** (i+2)
            
            if answer > 600 or answer < 16:
                is_power_feasible = False

            while is_power_feasible == False:
                current_operation = random.choice(special_operation_power)
                a = random.randint(2, 14)
                for i in range(len(special_operation_power)):
                    if current_operation == special_operation_power[i]:
                        answer = a ** (i+2)
                        if answer < 600 and answer > 15:
                            is_power_feasible = True

        elif current_operation == 's':
            current_operation = random.choice(special_operation_square)
            if current_operation == special_operation_square[0]:
                a = random.choice(square_liste)
                answer = a ** (1/2)
            elif current_operation == special_operation_square[1]:
                a = random.choice(cube_liste)
                answer = a ** (1/3)
            else:
                a = random.choice(power4_liste)
                answer = a ** (1/4)
      
            answer = round(answer)
            answer = int(answer)
            
        if current_operation in ('+', 'x', '/'): 
            question = f'{a} {current_operation} {b}'

        elif current_operation in special_operation_power:
            question = f'{a}{current_operation}'

        elif current_operation in special_operation_square:
            question = f'{current_operation}{a}'


    # EXTREME MODE QR
    else:
        operation = ['+', 'x', 'p', 'l', 'c'] 
        probability_weight_e = [15, 10, 20, 30,25]
        current_operation = random.choices(operation, weights=probability_weight_e, k=1)
        current_operation = current_operation[0]
        a = random.randint(2, 25)
        b = random.randint(2, 25)

        if current_operation == '+':
            add_type = ['integer', 'float']
            add_type_choice = random.choice(add_type)
            if add_type_choice == 'integer':
                a, b = random.randint(100, 500), random.randint(100, 1000)
                answer = a + b
            elif add_type_choice == 'float':
                a_fl, b_fl = random.uniform(10, 100), random.uniform(2, 50)
                a, b = round(a_fl, 2), round(b_fl, 2)
                answer = a + b

        elif current_operation == 'x':
            a, b = random.randint(15, 100), random.randint(8, 30)
            answer = a * b

        elif current_operation == 'p':
            a = random.randint(2, 50)
            current_operation = random.choice(special_operation_power)
            for i in range(len(special_operation_power)):
                if current_operation == special_operation_power[i]:
                    answer = a ** (i+2)
            
            if answer > 1000 or answer < 50:
                is_power_feasible = False

            while is_power_feasible == False:
                current_operation = random.choice(special_operation_power)
                a = random.randint(2, 50)
                for i in range(len(special_operation_power)):
                    if current_operation == special_operation_power[i]:
                        answer = a ** (i+2)
                        if answer < 1000 and answer > 50:
                            is_power_feasible = True

            if answer < 400:
                is_power_weak = True

            if is_power_weak:
                intern_operation = random.choice(['+', '-'])
                b = random.randint(30, 100)
                if intern_operation == '+':
                    answer += b
                if intern_operation == '-':
                    answer -= b



        elif current_operation == 'l':
            current_operation = random.choice(special_operation_logarithm)
            if current_operation in special_operation_logarithm[:4]:
                for i in range(len(special_operation_logarithm[:4])):
                    if current_operation == special_operation_logarithm[i]:
                        k = 2
                        logarithm = base = j = i + 2
                        logarithms = []
                        while logarithm < 5000:
                            logarithm = base ** k
                            logarithms.append(logarithm)
                            k += 1
                        a = random.choice(logarithms)
                        answer = round(math.log(a) / math.log(j))  # law of change of base with logarithms

            elif current_operation == 'ln':
                intern_operation = random.choice(['+', '-', 'x'])
                a, b = random.choice(special_operation_power), random.choice(special_operation_power)
                for i in range(len(special_operation_power)):
                    if a == special_operation_power[i]:
                        c = i + 2
                    elif b == special_operation_power[i]:
                        d = i + 2
                if intern_operation == '+':
                    answer = c + d
                elif intern_operation == 'x':
                    answer = c * d
                elif intern_operation == '-':
                    answer = c - d
                
        elif current_operation == 'c':
            a = random.randint(20, 100)
            m = random.randint(7, 100)
            while a <= m:
                a, m = random.randint(20, 100), random.randint(7, 100)

            if a < 50:
                is_congruence_weak = True

            if is_congruence_weak:
                b = random.randint(20, 50)
                intern_operation = random.choice(['+', '-', 'x'])
                if intern_operation == '+':
                    answer = (a + b) % m
                elif intern_operation == '-':
                    answer = (a - b) % m
                elif intern_operation == 'x':
                    answer = (a * b) % m
            
            else:
                answer = a % m


        if current_operation in ('+', 'x'):
            question = f'{a} {current_operation} {b}'

        elif current_operation in special_operation_power:
            if is_power_weak:
                question = f'{a}{current_operation} {intern_operation} {b}'
            else:
                question = f'{a}{current_operation}'

        
        elif current_operation in special_operation_logarithm[:4]:
            question = f'{current_operation}({a})'

        elif current_operation == 'ln':
            question = f'{current_operation}(e{a}) {intern_operation} {current_operation}(e{b})'


        elif current_operation == 'c':
            if is_congruence_weak:
                question = f'r ≡ {a} {intern_operation} {b} (mod {m})'
            else:
                question = f'r ≡ {a} (mod {m})'











    qr[0] = question
    qr[1] = answer

    return qr




# test the function on the different modes


'''
while True:
    print()
    question_answer = all_qr('extreme')
    print(f'la question est : {question_answer[0]}')
    print(question_answer[1])
    reponse = None
    while reponse != question_answer[1]:
        try:
            reponse = float(input('Réponse: '))
        except:
            print('entrez uniquement des nombres!')
    print('correct!')

'''



