from color import MAJOR_COLORS, MINOR_COLORS
from conversion import get_pair_number_from_color


def generate_manual():
    manual = ""
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            pair_number = get_pair_number_from_color(major_color, minor_color)
            manual += f"{major_color} {minor_color}: {pair_number}\n"
    return manual
