from faker import Faker
fake= Faker()
with open("output.txt","w") as f:
    for i in range(10):
        f.write(F"{fake.name()}\n")
for line in open("output.txt"):
    print(line)