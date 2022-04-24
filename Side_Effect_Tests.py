#An example follows, testing the update_counts function (which is deliberately implemented incorrectly…).
# This function takes a string called letters and updates the counts in counts_diction that are associated with each
# character in the string. To do a side effect test, we first create a dictionary with initial counts for some letters.
# Then we invoke the function. Then we test that the dictionary has the correct counts for some letters
# (those correct counts are computed manually when we write the test.
# We have to know what the correct answer should be in order to write a test).
# You can think of it like writing a small exam for your code – we would not give you an exam without knowing the
# answers ourselves.


def update_counts(letters, counts_d):
    for c in letters:
        counts_d[c] = 1
        if c in counts_d:
            counts_d[c] = counts_d[c] + 1


counts = {'a': 3, 'b': 2}
update_counts("aaab", counts)
# 3 more occurrences of a, so 6 in all
assert counts['a'] == 6
# 1 more occurrence of b, so 3 in all
assert counts['b'] == 3
