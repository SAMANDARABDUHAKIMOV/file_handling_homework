def main(data:str):
    return len(data)
f=open("data/data02.txt")
s=f.read()
print(main(s))