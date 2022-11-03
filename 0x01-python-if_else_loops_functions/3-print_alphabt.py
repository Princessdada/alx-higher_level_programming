for chr_a in range(97, 123):
    if chr_a == 101 or chr_a == 113:
        continue
    print("{:c}".format(chr_a), end="")
