import re
test_string = "aabbb_camelCaseExample TestStringToSplit"

#Task 1
def match_a_zero_or_more_b(string):
    return bool(re.fullmatch(r"ab*", string))
print(match_a_zero_or_more_b("abbb"))



#Task 2
def match_a_two_to_three_b(string):
    return bool(re.fullmatch(r"ab{2,3}", string))
print(match_a_two_to_three_b("abbb")) 



#Task 3
def find_lowercase_with_underscore(string):
    return re.findall(r"[a-z]+_[a-z]+", string)

print(find_lowercase_with_underscore(test_string))



#Task 4
def find_uppercase_followed_by_lowercase(string):
    return re.findall(r"[A-Z][a-z]+", string)

print(find_uppercase_followed_by_lowercase(test_string))



#Task 5
def match_a_anything_b(string):
    return bool(re.fullmatch(r"a.*b", string))

print(match_a_anything_b("aAnythingHereb"))  # True



#Task 6
def replace_with_colon(string):
    return re.sub(r"[ ,.]", ":", string)
print(replace_with_colon("Hello, world. How are you?"))



#Task 7
def snake_to_camel(string):
    return ''.join(word.title() if i > 0 else word for i, word in enumerate(string.split('_')))

print(snake_to_camel("snake_case_example"))  



#Task 8
def split_at_uppercase(string):
    return re.findall(r"[A-Z][^A-Z]*", string)

print(split_at_uppercase("TestStringToSplit"))



#Task 9
def insert_spaces_capitals(string):
    return re.sub(r"(?<=[a-z])(?=[A-Z])", " ", string)
print(insert_spaces_capitals("TestStringToSplit"))  



#Task 10
def camel_to_snake(string):
    return re.sub(r"(?<=[a-z])(?=[A-Z])", "_", string).lower()

print(camel_to_snake("camelCaseExample"))