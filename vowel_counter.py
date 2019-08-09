# vowels.py - Counts the number of vowels in a user entered string

# Global variables
vowels = 'aeiou'

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

def count_vowels(string):
    """ Returns the total number of vowels in string. """
    
    count = 0
    for s in string.lower():
        if s in vowels:
            count += 1
            which(s)
           
    return count


def which(vowel):
    """ Counts occurrance of each vowel. """
    global a_count, e_count, i_count, o_count, u_count

    if vowel == 'a':
        a_count += 1 

    elif vowel == 'e':
        e_count += 1

    elif vowel == 'i': 
        i_count += 1

    elif vowel == 'o':
        o_count += 1

    else:
        u_count += 1


if __name__ == '__main__':
    print('Hello and welcome to Vowel Counter 3000!')
    print('Please, enter a string')
    s = input('> ')

    total = count_vowels(s)

    print()
    print('Results:')
    print(' a: %d' % a_count)
    print(' e: %d' % e_count)
    print(' i: %d' % i_count)
    print(' o: %d' % o_count)
    print(' u: %d' % u_count)
    print()
    print('total vowels: %d' % total)
