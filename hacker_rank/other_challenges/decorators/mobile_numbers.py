def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            a = len(l[i]) - 10
            l[i] = l[i][a:]
            l[i] = "+91 " + l[i][:5] + " " + l[i][5:]
        return f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
