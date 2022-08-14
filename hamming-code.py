# Hamming code, https://habr.com/ru/post/140611/ was helped me 

from math import log2

def print_list(lst):
    print('\n-------------------LIST PRINTED----------------------')
    print("positions: ", end=" ")
    for i in range(len(lst)):
        print('{0:2d}'.format(i + 1), end="  ")
    print()
    print("binary code: ", end="")
    for el in lst:
        print('{0:2s}'.format(str(el)), end="  ")

    control_list = [lst[2 ** i - 1] for i in range(6)]
    print("\n\nPosition number: ", end="")
    for i in range(6):
        print('{0:2d}'.format(2 ** i), end="  ")

    print("\nControl bits:    ", end="")
    for el in control_list:
        print('{0:2d}'.format(int(el)), end="  ")
    
    print()


def binary_data_generation(text):
    print('\n--------------------CREATED BINARY LIST----------------------')
    bin_lst = ['0' + bin(ord(el))[2::] for el in text]
    [print(text[i], "digital code:", ord(text[i]), ", binary code", bin_lst[i]) for i in range(len(text))]

    bin_str=''

    for el in bin_lst:
        bin_str += el

    print('\nТекст в двоичном виде:', bin_str, '\nlength of text:', len(bin_str))

    binary_full_list = [(el) for el in bin_str]
    return binary_full_list


def add_zero_to_control_bits(binary_list):
    print('\n-------------------Added zeros to CONTROL BITS----------------------')
    control_bits_counter = round(log2(len(binary_list))) + 1
    for i in range(control_bits_counter):
        binary_list.insert(2 ** i - 1, 0)
    
    print("Added", control_bits_counter, "control bits, Binary list with control bits is:")
    print(*binary_list, "\nlength of text with control bits:", len(binary_list))
    return binary_list, control_bits_counter;


def solve_control_bits(bin_lst, control_bits_cnt):
    print('\n-------------------SOLVE CONTROL BITS----------------------')
    lst_len = len(bin_lst)
    contr_bits_list = []

    for k in range(control_bits_cnt):
        s = 0
        for i in range(2 ** k - 1, lst_len, 2 ** (k + 1)):
            for j in range(2 ** k):
                if i + j < lst_len:
                    s+=int(bin_lst[i + j])
                else:
                    break       
        bin_lst[2 ** k - 1] = (s % 2)
        contr_bits_list.append(s)

    print("Количесвто единиц для соотв контр битов", contr_bits_list)
    print(*bin_lst)
    print_list(bin_lst)
    contr_bits_list = [el % 2 for el in contr_bits_list]
    return bin_lst, contr_bits_list


def solve_control_bits_decoder(bin_lst, control_bits_cnt, wrong_bit):
    print('\n-------------------SOLVE CONTROL BITS decoder----------------------')
    lst_len = len(bin_lst)
    contr_bits_list = []

    for k in range(control_bits_cnt):
        s = 0
        for i in range(2 ** k - 1, lst_len, 2 ** (k + 1)):
            for j in range(2 ** k):
                if i + j < lst_len:
                    s+=int(bin_lst[i + j])
                else:
                    break  
        if (2 ** k == wrong_bit):
            s+=1     
        bin_lst[2 ** k - 1] = (s % 2)
        contr_bits_list.append(s)

    print("Количесвто единиц для соотв контр битов", contr_bits_list)
    print(*bin_lst)
    print_list(bin_lst)
    contr_bits_list = [el % 2 for el in contr_bits_list]
    return bin_lst, contr_bits_list


text = "LaIs"
binary_list = binary_data_generation(text)
binary_list, control_bits_cnt = add_zero_to_control_bits(binary_list)
binary_list, contr_bits_list = solve_control_bits(binary_list, control_bits_cnt)

wrong_bit = int(input('What control bit is wrong, input it??? '))
print('/////////////////////////////////////////// DECODING ////////////////////////////')
binary_list_decode = binary_data_generation(text)
binary_list_decode, control_bits_cnt = add_zero_to_control_bits(binary_list_decode)
binary_list_decode, contr_bits_list_decode = solve_control_bits_decoder(binary_list_decode, control_bits_cnt, wrong_bit)

wrong_bit_position = 0

for i in range(len(contr_bits_list)):
    if (contr_bits_list[i] ^ contr_bits_list_decode[i]):
        wrong_bit_position+=(2**i)

print('Control list before', contr_bits_list)
print('Control list after ', contr_bits_list_decode)
print('Wrong bit found on position:', wrong_bit_position)
