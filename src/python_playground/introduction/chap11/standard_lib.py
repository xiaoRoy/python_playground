from collections import defaultdict, Counter, deque


def count_food(food_list):
    def default_factory():
        return int

    food_counter = defaultdict(default_factory())
    for food in food_list:
        food_counter[food] += 1
    return food_counter


class EnhancedCounter(Counter):

    def first(self):
        first_one = self.most_common(1)
        if len(first_one) != 1:
            raise IndexError()
        return self.most_common(1)[0]


def get_keys_as_list(dictionary):
    return list(dictionary.keys())


def check_palindrome(word):
    word_to_check = deque(word)
    is_palindrome = False
    while len(word_to_check) > 1:
        if word_to_check.pop() != word_to_check.popleft():
            break
    else:
        is_palindrome = True
    return is_palindrome


def check_palindrome_second(word):
    return word == word[::-1]
