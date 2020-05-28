def ft_map(function_to_apply, list_of_inputs):
    returned_list = []
    for item in list_of_inputs:
        returned_list.append(function_to_apply(item))
    return returned_list


print(ft_map(lambda x: x.upper(), ["pouet", "coucou"]))
