
# f = open( 'input.txt', 'r')
# a, b=map(int, f.readline().split())

# c = a+b

# w = open( 'output.txt', 'w')
# w.write(str(c))

# f.close()
# w.close()

# Word=input()
Flag = 0
CountLetter = 0
LastIndex = 0
a = 0
try:
    CountLetter = int(input())
except ValueError:
    Flag = 1

a = list(map(int, input().split()))
a.insert(0, 0)
LastIndex = len(a)-1


FirstIndex = 0

FinalArr = []
while FirstIndex != LastIndex and CountLetter == LastIndex and Flag == 0:

    Letter = abs(a[FirstIndex] - a[FirstIndex+1])
    FirstIndex += 1

    if Letter == 1:
        FinalArr.append('a')

    elif Letter == 2:
        FinalArr.append("b")

    elif Letter == 4:
        FinalArr.append("c")

    elif Letter == 8:
        FinalArr.append("d")

    elif Letter == 16:
        FinalArr.append("e")

    elif Letter == 32:
        FinalArr.append("f")

    elif Letter == 64:
        FinalArr.append("g")

    elif Letter == 128:
        FinalArr.append("h")

    elif Letter == 256:
        FinalArr.append("i")

    elif Letter == 512:
        FinalArr.append("j")

    elif Letter == 1024:
        FinalArr.append("k")

    elif Letter == 2048:
        FinalArr.append("l")

    elif Letter == 4096:
        FinalArr.append("m")

    elif Letter == 8192:
        FinalArr.append("n")

    elif Letter == 16384:
        FinalArr.append("o")

    elif Letter == 32768:
        FinalArr.append("p")

    elif Letter == 65526:
        FinalArr.append("q")

    elif Letter == 131072:
        FinalArr.append("r")

    elif Letter == 262144:
        FinalArr.append("s")

    elif Letter == 524288:
        FinalArr.append("t")

    elif Letter == 1048576:
        FinalArr.append("u")

    elif Letter == 2097152:
        FinalArr.append("v")

    elif Letter == 4194304:
        FinalArr.append("w")

    elif Letter == 8388608:
        FinalArr.append("x")

    elif Letter == 16777216:
        FinalArr.append("y")

    elif Letter == 33554432:
        FinalArr.append("z")

    elif Letter == 67108864:
        FinalArr.append(" ")

    else:
        print("cool y", Letter)

if CountLetter == LastIndex and Flag == 0:
    print(*FinalArr, sep="")
