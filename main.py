import os

filename_list = ['1.txt', '2.txt', '3.txt']
file_dict = {}

for filename in os.listdir(os.getcwd()):
    count = 0
    list_lines = []
    if filename in filename_list:
        with open(os.path.join(os.getcwd(), filename), encoding='utf-8') as file_obj:
            for idx in file_obj:
                list_lines.append(idx.strip())
                count += 1
            file_dict[count] = {filename: list_lines}

sorted_file_dict = dict(sorted(file_dict.items()))


with open('result.txt', 'w', encoding='utf-8') as file_obj:
    for key, value in sorted_file_dict.items():
        new_value = dict(value)
        for inside_key, inside_value in new_value.items():
            file_obj.write(f'{inside_key}\n')
            file_obj.write(f'{str(key)}\n')
            new_inside_value = list(inside_value)
            for idx in new_inside_value:
                file_obj.write(f'{idx}\n')
                print(idx)
