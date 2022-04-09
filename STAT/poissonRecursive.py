p0 = 0.13533528
def nextp(lastp, i):
    return (2/(i+1))*lastp

lastp = p0
sum = 0
for i in range(1, 20):
    lastp = nextp(lastp, i)
    sum += lastp
    print(f'{lastp}, {lastp*20}')
    
