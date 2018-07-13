
def word_count1(str):
    count2=dict()
    w=str.split()
    for a in w:
        if a in count2:
            count2[a]=count2[a]+1
        else:
            count2[a]=1

    return count2

str11=input("Enter string")
c=word_count1(str11)
print(c)
e=sorted(c.items(),reverse=False)
print("Ascending sorted list : ")
print(e)

f=sorted(c.items(),reverse=True)
print("Decending sorted list : ")
print(f)
print("Using for loop")
for f in sorted(set(c)):
    print(f)

