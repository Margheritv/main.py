from random import random
from nltk.corpus import names
from nltk.corpus import wordnet
import random


def generate_names(char, num):
    fembank = []
    fembankNoTupel = []
    malebank = []
    malebankNoTupel = []
    female_names = names.words('female.txt')
    male_names = names.words('male.txt')

    labeled_female_names = [(name, 'female') for name in female_names]
    non_labeled_female_names = [name for name in female_names]
    labeled_male_names = [(name, 'male') for name in male_names]
    non_labeled_male_names = [name for name in male_names]

    female_output = 'female_output.txt'
    male_output = 'male_output.txt'

    if type(char) == str:
        name_check = 0
        for name in range(len(female_names)):
            if female_names[name].startswith(char):
                name_check += 1

    if type(char) != str:
        raise Exception('The character is not a string')
    elif name_check == 0:
        print('No female names were found')
    else:
        for i in range(num):
            j = 0
            while j == 0:
                x = random.randint(0, len(female_names)-1)
                if female_names[x].startswith(char):
                    fembank.append(labeled_female_names[x])
                    fembankNoTupel.append(non_labeled_female_names[x])
                    j += 1
        print(fembank)
        # print(fembankNoTupel)

        with open(female_output, 'w') as writer:  # opens new output file and writes
            for name in fembankNoTupel:
                writer.write(name)  # write el in file
                writer.write("\n")

    if type(char) == str:
        name_check = 0
        for name in range(len(male_names)):
            if male_names[name].startswith(char):
                name_check += 1

    if type(char) != str:
        raise Exception('The character is not a string')
    elif name_check == 0:
        print('No male names were found')
    else:
        for i in range(num):
            j = 0
            while j == 0:
                x = random.randint(0, len(male_names)-1)
                if male_names[x].startswith(char):
                    malebank.append(labeled_male_names[x])
                    malebankNoTupel.append(non_labeled_male_names[x])
                    j += 1
        print(malebank)

        with open(male_output, 'w') as writer:
            for name in malebankNoTupel:
                writer.write(name)
                writer.write("\n")


generate_names('M', 5)


# 3

class SynAnt:
    def __init__(self):
        self.words = []    # this is a list of words for the constructor to find syn/ant

    def append(self, element):  # appends elements (if any) to list
        self.words.append(element)

    def find_synonyms(self):
        if len(self.words) == 0:    # checks if the list is empty. If yes --> exception
            raise Exception('No synonyms found, as there are no elements in the list.')
        for element in self.words:      # checking the elements in the list
            if type(element) != str:     # if type not a string --> exception
                raise Exception('No synonym found for non string types.')
            else:
                synonyms = []   # empty list in which to append synonyms
                for syn in wordnet.synsets(element):   # function to find & append synonyms
                    for l in syn.lemmas():
                        synonyms.append(l.name())

            if len(synonyms) == 0:  # append this custom message to the list, if no syn found
                synonyms.append('No synonym found.')

            print('Synonym of {} --> {}'.format(element, set(synonyms)))    # print synonyms

    def find_antonyms(self):
        if len(self.words) == 0:    # checks if the list is empty. If yes --> exception
            raise Exception('No antonyms found, as there are no elements in the list.')
        for element in self.words:    # checks elements in list
            if type(element) != str:  # if type not a string --> exception
                raise Exception('No antonym found for non string types.')
            else:
                antonyms = []  # empty list in which to append antonyms
                for syn in wordnet.synsets(element):
                    for i in syn.lemmas():
                        if i.antonyms():
                            antonyms.append(i.antonyms()[0].name())

                if len(antonyms) == 0:  # append this custom message to the list, if no antonym found
                    antonyms.append('No antonym found.')

                print('Antonym of {} --> {}'.format(element, set(antonyms)))  # print antonyms


List1 = SynAnt()
List1.append('scooter')
List1.append('hate')
List1.find_synonyms()

List2 = SynAnt()
List2.append('sincere')
List2.append('literate')
List2.find_antonyms()