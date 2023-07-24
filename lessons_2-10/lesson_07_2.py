import random

user_list = [x := random.randint(1, 10) for i in range(1, 201)]
result_dict = {elem: user_list.count(elem) for elem in user_list}
define = lambda x: "раза" if str(x)[-1] in "234" else "раз"

for elem in set(result_dict):
    print(f"Число {elem} встречается в первоначальном списке {result_dict[elem]} {define(result_dict[elem])}")
