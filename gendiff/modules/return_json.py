from gendiff.modules.diff import diff


def return_json(file1, file2):
    result = diff(file1, file2)
    result = make_stylish(result)
    # last symbol of result is '\n', don't need it
    return '\n'.join(['{', result[:-1], '}'])\
               .replace('False', 'false')\
               .replace('True', 'true')\
               .replace('None', 'null')


def make_stylish(node, memory='', indent='    '):
    node = dict(sorted(node.items(), key=custom_sort))

    for key, value in node.items():
        key_indent = indent_checker(key, indent)
        memory += ''.join([key_indent, str(key), ': '])
        if not isinstance(value, dict):
            memory += ''.join([str(value), '\n'])
        else:
            memory += '{\n'
            memory = make_stylish(value, memory, indent + '    ')
            memory += ''.join([indent, '}', '\n'])
    return memory


def custom_sort(items):
    if items[0][0] in ['-', '+']:
        return items[0][2:]
    else:
        return items[0]


def indent_checker(dict_key, indent):
    if str(dict_key)[0] in ['-', '+']:
        key_indent = indent[2:]
    else:
        key_indent = indent
    return key_indent
