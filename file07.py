def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    
# Read data from file
    s=0
    for i in data:
        if i.isdigit():
            s+=int(i)
    return s
f=open("data/data07.txt")
s=f.read()
print(main(s))