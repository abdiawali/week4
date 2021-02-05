from unittest import TestCase
import camelcase
import unittest


class Test_inputs(TestCase):

    def test_expected_input(self):
        user_input=camelcase.change_to_camelcase('hello world')
        expected_output='helloWorld'
        self.assertEqual(expected_output,user_input)
        # tests sentence with space between it
        self.assertEqual('thisIsASentence',camelcase.change_to_camelcase('This is a sentence'))
        #tests all caps sentence
        self.assertEqual('goodMorning',camelcase.change_to_camelcase('GOOD MORNING'))
        #tests all lower sentence
        self.assertEqual('goodNight',camelcase.change_to_camelcase('good night'))

    def test_sentences_with_spaces_and_no_space(self):
        #test no input
        self.assertEqual('',camelcase.change_to_camelcase(''))
        #test space
        self.assertEqual('',camelcase.change_to_camelcase('            '))
        #tests spaces before, in between, and after sentence
        self.assertEqual('helloWorld',camelcase.change_to_camelcase('  hello   world  '))
        #tests no spaces before, in between, and after sentence
        self.assertEqual('thisisallonesentence',camelcase.change_to_camelcase('thisisallonesentence'))
        #test space between every letter
        self.assertEqual('sPACEAFTEREVERYLETTER',camelcase.change_to_camelcase('s p a c e a f t e r e v e r y l e t t e r'))

    def test_mix_letters_numbers(self):
        #test numbers between letters
        self.assertEqual('helloR2D2',camelcase.change_to_camelcase('hello R2D2'))
        #test numbers before sentence
        self.assertEqual('123Go',camelcase.change_to_camelcase('123 go'))
        #test numbers after sentence
        self.assertEqual('myUsernameIsAbdi123',camelcase.change_to_camelcase('my username is abdi123'))
        #test mix of letters and numbers no space
        self.assertEqual('abdi123FatahIsMyU5Ernam3',camelcase.change_to_camelcase('abdi123fatah is my u5ernam3'))

    def test_symbols(self):
        #test symbols between letters
        self.assertEqual('hello@Abdi',camelcase.change_to_camelcase('hello @ abdi'))
        #
        self.assertEqual('west<North^East>',camelcase.change_to_camelcase('west<north^east>'))

    def test_emojis(self):
        #test emoji with spaces
        self.assertEqual('😃😃⛹️‍♂️🤼‍♂️🏋️‍♂️🏇🏊‍♂️🎮',camelcase.change_to_camelcase('😃😃 ⛹️‍♂️🤼‍♂️ 🏋️‍♂️🏇 🏊‍♂️🎮'))
        #test emoji with no spaces
        self.assertEqual('😃😃⛹️‍♂️🤼‍♂️🏋️‍♂️🏇🏊‍♂️🎮',camelcase.change_to_camelcase('😃😃⛹️‍♂️🤼‍♂️🏋️‍♂️🏇🏊‍♂️🎮'))
        #test emoji with sentence
        self.assertEqual('thingsILikeToDo⛹️‍♂️🤼‍♂️🏋️‍♂️🏇🏊‍♂️🎮',camelcase.change_to_camelcase('things i like to do ⛹️‍♂️🤼‍♂️🏋️‍♂️🏇🏊‍♂️🎮'))
        #test emoji with numbers
        self.assertEqual('1⛹️‍♂️2🤼‍♂️3🏋️‍♂️4🏇5🏊‍♂️6🎮',camelcase.change_to_camelcase('1⛹️‍♂️2🤼‍♂️3🏋️‍♂️4🏇5🏊‍♂️6🎮'))
        #test emoji with letters and numbers
        self.assertEqual('words⛹️‍♂️🤼‍♂️🏋️‍♂️With🏇🏊‍♂️🎮Emojis',camelcase.change_to_camelcase('words⛹️‍♂️🤼‍♂️🏋️‍♂️with🏇🏊‍♂️🎮emojis'))



if __name__=='__main__':
    unittest.main()
