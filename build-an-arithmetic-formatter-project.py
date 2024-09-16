def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        result = 'Error: Too many problems.'
        return result

    
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    for problem in problems:
        problem_list = problem.split(" ")
        longest_number = max(len(problem_list[0]), len(problem_list[2]))
        if longest_number > 4:
            result = 'Error: Numbers cannot be more than four digits.'
            return result
        elif problem_list[1] != '+' and problem_list[1] != '-':
            result = "Error: Operator must be '+' or '-'."
            return result
        elif not problem_list[0].isdigit() or not problem_list[2].isdigit():
            result = 'Error: Numbers must only contain digits.'
            return result

        for _ in range(longest_number - len(problem_list[0]) + 2):
            line1 += ' '
        line1 += problem_list[0] + '    '

        line2 += problem_list[1]
        for _ in range(longest_number - len(problem_list[2]) + 1):
            line2 += ' '
        line2 += problem_list[2] + '    '

        for _ in range(longest_number + 2):
            line3 += '-'
        line3 += '    '

        if show_answers:
            num1 = int(problem_list[0])
            num2 = int(problem_list[2])
            answer = 0
            if problem_list[1] == '+':
                answer = num1 + num2
            elif problem_list[1] == '-':
                answer = num1 - num2
            for _ in range(longest_number + 2 - len(str(answer))):
                line4 += ' '
            line4 += str(answer) + '    '
            
    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()
    line4 = line4.rstrip()
    
    if show_answers:
        result = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    else:
        result = line1 + "\n" + line2 + "\n" + line3

    return result

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "123 + 49"])}')