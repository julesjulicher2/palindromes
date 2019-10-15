import os
palindromes = set()
for year in range(2019,2201):
    for day in range(1,32):
        for month in range(1, 13):
            if f"{day}{month}{year}" == f"{day}{month}{year}"[::-1]:
                palindromes.add(f"{day}/{month}/{year}")

for year in range(2018,2201):
    for day in range(1,32):
        for month in range(1,13):
            if f"{str(day).zfill(2)}{str(month).zfill(1)}{str(year).zfill(4)}" == f"{str(day).zfill(2)}{str(month).zfill(2)}{str(year).zfill(4)}"[::-1]:
                palindromes.add(f"{str(day).zfill(2)}/{str(month).zfill(1)}/{str(year).zfill(4)}")

print((palindromes, os.linesep))
print(f"count={len(palindromes)}")
