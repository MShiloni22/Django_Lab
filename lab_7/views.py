from django.shortcuts import render


def lab_7(request):
    return render(request, 'lab_7.html')


def input_processor(request):
    input_text = request.POST['input_text']
    num = request.POST['number']
    digits_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for i in range(len(input_text)):
        if input_text[i] not in digits_list:
            input_text = input_text.replace(input_text[i], ' ')
    numbers_in_input = input_text.split()
    sum = 0
    print(numbers_in_input)
    for i in range(len(numbers_in_input)):
        int_num = int(numbers_in_input[i])
        print(int_num)
        if int_num < int(num):
            sum += int_num
    return render(request, 'input_processor.html', {'sum': sum})
