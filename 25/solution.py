file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines()]
file.close()

domain = "=-012"


def snafu_to_int(snum):
    decimal = 0
    power = 0
    for digit in snum[::-1]:
        decimal += (domain.index(digit) - 2) * 5 ** power
        power += 1
    return decimal


# decimal to "balanced quinary" numeral system
def int_to_snafu(num):
    snafu = ""
    while num > 0:
        num, remainder = divmod(num, 5)
        match remainder:
            case 0:
                snafu += "0"
            case 1:
                snafu += "1"
            case 2:
                snafu += "2"
            case 3:
                snafu += "="
                num += 1
            case 4:
                snafu += "-"
                num += 1
    return snafu[::-1]


print(int_to_snafu(sum(map(snafu_to_int, myin))))