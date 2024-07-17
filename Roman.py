def roman(num):
    kir=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    rom=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    rom_num=''
    for i in range(len(kir)):
        while num>=kir[i]:
            rom_num+=rom[i]
            num-=kir[i]
    return rom_num
print(roman(int(input("Введите число"))))
