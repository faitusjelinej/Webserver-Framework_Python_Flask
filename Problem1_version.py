
def compareversion(version1, version2):
    v1 = [int(x) for x in version1.split('.')]
    v2 = [int(x) for x in version2.split('.')]

    for x in range(max(len(v1),len(v2))):
        if x < len(v1):
            version1 = v1[x]
        else:
            version1 = 0

        if x < len(v2):
            version2 = v2[x]
        else:
            version2 = 0

        if version1 > version2:
            return 1
        elif version1 < version2:
            return -1
    return 0

if __name__ == '__main__':
    answer1 = compareversion(version1 = "0.1", version2 = "1.1")
    answer2 = compareversion(version1 = "1.0", version2 = "1.0.0")
    answer3 = compareversion(version1 = "1.1", version2 = "1.0")
    print(answer1)
    print(answer2)
    print(answer3)

