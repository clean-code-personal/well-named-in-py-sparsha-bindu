from testing import test_number_to_pair, test_pair_to_number
from manual import generate_manual

if __name__ == '__main__':
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    print(generate_manual())
    print('Done :)')
