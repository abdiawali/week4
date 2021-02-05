def change_to_camelcase(sentence):
    title_case = sentence.title() # Uppercase first letter of each word
    no_space_title_case = title_case.replace(' ', '') # remove spaces 
    # Lowercase first letter, join with rest of string 
    return no_space_title_case[0:1].lower() + no_space_title_case[1:] 


def main():
    print("Enter a sentence to convert to camelCase")
    sentence = input('Enter your sentence: ')
    camelcased = change_to_camelcase(sentence)
    print(camelcased)

if __name__=='__main__':
    main()