from module_variables import DEBUG_MODE

def convert_string_to_list(in_value: str):
    output = []
    for row in in_value.split('\n'):
        values = row.split(';')
        if DEBUG_MODE: print(values)
        if len(values) != 2:
            break
        output.append([float(values[0]), float(values[1])])
    return output
def convert_list_to_string(in_value):
    output = ""
    for row in in_value:
        output += str(row[0]) + ";" + str(row[1]) + '\n'
    return output
