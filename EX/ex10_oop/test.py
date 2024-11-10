

class Associate:

    def __init__(self, name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary

    def __repr__(self):
        return '{' + self.name + ', ' + self.dept + ', ' + str(self.salary) + '}'


if __name__ == '__main__':
    associates = [
    Associate('James', 'Finance', 80000),
    Associate('Robert', 'Construction', 60000),
    Associate('James', 'Telecom', 70000)
    ]

# 1. Sort by only `dept` attribute
associates.sort(key=lambda x: x.dept)

# [{Robert, Construction, 60000}, {James, Finance, 80000}, {James, Telecom, 70000}]
print(associates)

# 2. Sort by `name` attribute, followed by `dept` attribute
associates.sort(key=lambda x: (x.name, x.dept))

# [{James, Finance, 80000}, {James, Telecom, 70000}, {Robert, Construction, 60000}]
print(associates)

# 3. Sort by `name` attribute in reverse order,
# , followed by `dept` attribute in reverse order
associates.sort(key=lambda x: (x.name, x.dept), reverse=True)

# [{Robert, Construction, 60000}, {James, Telecom, 70000}, {James, Finance, 80000}]
print(associates)

# 4. Sort by `name` attribute in the natural order,
# , followed by numeric `salary` attribute in reverse order
associates.sort(key=lambda x: (x.name, -x.salary))

# [{James, Finance, 80000}, {James, Telecom, 70000}, {Robert, Construction, 60000}]
print(associates)