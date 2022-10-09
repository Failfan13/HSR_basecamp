

def check_triangle(lenth1, length2, length3):
    nums = [lenth1, length2, length3]
    nums.sort()
    if nums[2] >= nums[0] + nums[1]:
        print('impossible')
        return bool(False)
    else:
        print('possible')
        return bool(True)


if __name__ == '__main__':
    side1 = int(input('side 1 lenth'))
    side2 = int(input('side 2 lenth'))
    side3 = int(input('side 3 lenth'))
    check_triangle(side1, side2, side3)
