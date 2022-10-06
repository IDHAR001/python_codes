from pydoc import doc


dict01 = {}
for item in range(1,11):
    dict01[item] = item ** 2

dict02 = {item: item ** 2 for item in range(1,11)}