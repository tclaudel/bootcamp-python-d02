def ft_filter(function_to_apply, list_of_inputs):
    returned_list = []
    for item in list_of_inputs:
        if function_to_apply(item):
            returned_list.append(item)
    return returned_list


number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
