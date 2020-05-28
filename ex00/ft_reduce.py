import functools

def ft_reduce(function_to_apply, list_of_inputs):
    result = 0
    for item in list_of_inputs:
        result = function_to_apply(result, item)
    return result


res = ft_reduce(lambda x, y: x + y, range(10))
print("Résultat final", res)
res = functools.reduce(lambda x, y: x + y, range(10))
print("Résultat final", res)
