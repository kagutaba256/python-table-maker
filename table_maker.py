# sam 10.10.2020
# prettytable replacement
import pandas as pd


def make_table(titles, data):
    # find longest string
    longest_lengths = []
    for item in titles:
        longest = 0
        if len(item) > longest:
            longest = len(item)
        for item in pd.DataFrame(data).T.values.tolist()[titles.index(item)]:
            if len(str(item)) > longest:
                longest = len(str(item))
        longest_lengths.append(longest + 2)
    top = "+"
    for item in titles:
        top += longest_lengths[titles.index(item)] * '-' + '+'
    print(top)
    string = "| "
    for item in titles:
        padding = longest_lengths[titles.index(item)] - len(item) - 1
        string += str(item) + " " * padding + "| "
    print(string)
    print(top)
    string = "| "
    for col in data:
        string = "| "
        for item in col:
            padding = longest_lengths[col.index(item)] - len(str(item)) - 1
            string += str(item) + " " * padding + "| "
        print(string)
    print(top)


# example
titles = ["category 1", "category 2", "category 3", "category 4", "category 5"]
data = [[1, 3, 6, 2, 1], ["cool", "swag", "nice", "awesome", "yay"],
        [1.3, 343124.123423, 12341234123.12343123, 1234.632, .123412351]]

make_table(titles, data)
