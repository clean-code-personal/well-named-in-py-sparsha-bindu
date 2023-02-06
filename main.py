from testing import test_number_to_pair, test_pair_to_number
from conversion import get_color_from_pair_number

if __name__ == '__main__':
  test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number('Red', 'Orange', 7)
  print('Done :)')

def format_color_coding_manual():
    manual = []
    for pair_number in range(1, 26):
        major_color, minor_color = get_color_from_pair_number(pair_number)
        manual.append(f"{pair_number}: {major_color} {minor_color}")
    return "\n".join(manual)

print(format_color_coding_manual())

