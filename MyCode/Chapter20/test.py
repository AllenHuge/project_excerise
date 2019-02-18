def flatten(nested):
    for sublist in nested:
        for element in sublist:
            print(element)

def flatten2(nested):
    for sublist in nested:
        for element in sublist:
            yield element

if __name__ == "__main__":
    input = [[1,2],[3,4],[5]]
    print(list(flatten2(input)))