import yaml, string, random, os, sys

class Variable:

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.generated_value = ""

    def __str__(self):
        return str(self.name) + "=" + str(self.generated_value)


def get_variable_file():
    if (len(sys.argv) <= 1):
        raise Exception('You should type at least one argument which is variable file!')
    return sys.argv[1]


def get_name_file():
    if (len(sys.argv) <= 2):
        raise Exception('You should type at least two arguments which is variable file and name file!')
    return sys.argv[2]


def get_cwd(file):
    # cwd = os.getcwd()
    _ROOT = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(_ROOT, file)


def get_random_name(fname):
    l = []
    with open(fname, "r") as f:
        for name in f:
            l.append(name[:-1])
        return l[random.randint(0, len(l) - 1)]


def get_random_port():
    return str(35400 + random.randint(0, 4600))


def get_random_password(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str


def generate_randomized_arg(variables):
    for var in variables:
        if (var.type).lower() == 'username':
            var.generated_value = get_random_name(get_cwd(get_name_file()))
        elif (var.type).lower() == 'password':
            var.generated_value = get_random_password(8)
        elif (var.type).lower() == 'port':
            var.generated_value = get_random_port()
    return variables


def parser_var_file():
    with open(get_cwd(get_variable_file())) as file:
        var_list = yaml.load(file, Loader=yaml.FullLoader)
        var_objects = []
        for var in var_list.keys():
            var_objects.append(Variable(var, var_list[var][0]["type"]))
        return var_objects


def print_result(objects):
    res = "ANSIBLE_ARGS='--extra-vars \""
    for var in objects:
        res += str(var) + " "
    res += "\"' vagrant up server"
    print(res)
    return res


def generate():
    list_of_generated_objects = generate_randomized_arg(parser_var_file())
    return list_of_generated_objects


def test():
    print_result(generate())


test()
