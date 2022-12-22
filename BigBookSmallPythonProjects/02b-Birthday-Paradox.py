def facto(n):
    if n==1:
        return n
    else:
        return n*(facto(n-1))

leap = input("\nLeap or not (yes/no):\t")
# while leap != ('yes' or 'no'):
if leap == 'yes':
    days = 366
elif leap == 'no':
    days = 365
# print(days)
peeps = int(input("Enter number of people:\t"))

proba1 = facto(days)/facto(days-peeps)

proba2 = 365**peeps

proba3 = float(proba1/proba2)

print(round((1-proba3)*100,2),"%")