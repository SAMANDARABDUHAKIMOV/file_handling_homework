def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    a = " "
    for i in range(n):
        a+=str(i)+","
    return a
print(main(3))