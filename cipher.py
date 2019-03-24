# -*- coding: utf-8-*-




# SYSTEM THINGS
import random, sys

reload(sys)
sys.setdefaultencoding('utf-8 ')
###############

chars = u" PİJAMLIHSTYĞZŞOFÖREÇBUCKGÜVNDQXWpijamlıhstyğzşoföreçbuckgüvndqxw0123456789!'<>;`()=&%+^£$½{[]}|.,*/-_\\\"?############################################################################################################################################"


all_chars = {}
all_charsRVS = {}

for i in range(1,len(chars)):
    all_chars[chars[i-1]] = i
    all_charsRVS[i] = chars[i-1]

# CHECK FOR IF IT IS PRIME OR NOT FUNC
def isPrime(num):
    for n in range(2, num):
        if num % n == 0:
            return False
        else:
            continue
    return True


######################################


# EUCLID ALGORITHM FUNCTION FOR CONTROL
def euclid(num1, num2):
    if num1 <= num2:
        num1, num2 = num2, num1

    else:
        try:
            num3 = num1 % num2
            if num3 == 0:
                return num2
            else:
                return euclid(num2, num3)
        except:
            return 0


#######################################



# FUNCTION THAT CREATES EQUATITION FOR EUCLID ALGORITHM SOLVER FUNC
def createEQT4eu(nums):
    if nums[1] > nums[0]:
        nums[0], nums[1] = nums[1], nums[0]

    num1 = nums[0]
    num2 = nums[1]
    equation = "1=({}*x)+({}*y)".format(num1, num2)
    return equation


###################################################################



# EULER FUNC OR PHI FUNC
def phi(num, prime):
    num = (prime[0] - 1) * (prime[1])
    return num


########################



# A SOLVER FUNCTION FOR EULER EQUATITION
def solveEQT(equation):
    fNUM = 0
    cik = False
    nEQT = equation.split("=")
    res = nEQT[0]  # GENERALLY IT'S 1 FOR ADVANCED RSA
    eqt = nEQT[1]  # IT'S EQUALITION
    num1 = eqt[1:eqt.index("*x")]
    num2 = eqt[eqt.index("+") + 1:eqt.index("*y")]
    while not cik:
        fNUM += 1
        for n in xrange(-1 * int(num1), int(num1)):
            eqt1 = eqt
            eqt1 = eqt1.replace("x", "{}")
            eqt1 = eqt1.replace("y", "{}")
            eqt1 = eqt1.format(fNUM, n)
            if eval(eqt1) == 1:
                cik = True
                return (fNUM, n)


#########################################



# FUNCTION THAT CREATES NUMBER TO DETERMINE KEYS FOR CIPHER
def crtEUCnums():
    counter = 0
    primes = [5,7,11,13,17,19,23,29]
##    while counter != 2:
##        num1 = random.choice(range(5, 20))
##
##        if isPrime(num1):
##            primes.append(num1)
##            counter += 1
    prime1, prime2 = random.choice(primes), random.choice(primes)
    num1 = prime1*prime2
    num2 = phi(num1, [prime1,prime2])
    cik = False

    n = random.choice(range(num2))
    while not cik:
        if euclid(num2, n) == 1:
            cik = True
            return [prime1,prime2], num2, num1, n
        else:    n = random.choice(range(num2))


###########################################################



# FUNCTION THAT GIVES YOU CIPHER KEYS
def getKEY():
##    cik = False
##    while not cik:
    num = crtEUCnums()
    primes = num[0]
    phi = num[1]
    N = num[2]
    e = num[3]
    eqt = createEQT4eu([phi, e])
    eqtS = solveEQT(eqt)
    d = phi + eqtS[1]
        # N AND e WILL BE GIVEN TO OTHERSIDE AND N AND d WILL BE HIDDEN FOR US
    testMSG = "Lorem ipsum dolor?"
    ciphered = cipher(keyTRANS([N, e]), testMSG)
    res = (e*d) % N
    try:
        testMSG0 = decipher(keyTRANS([N, d]), ciphered)
    except Exception as a:
        testMSG0 = False
##    print testMSG0
    if res== 1 and testMSG == testMSG0:
        return (N, e), (N, d)
    else:
        return getKEY()


#####################################



# TRANSLATE FUNCTION FOR KEYS TO MAKE THEM SENDABLE TO CLIENT
def keyTRANS(keyLIST):
    keyLIST = [str(i) for i in keyLIST]
    return "-".join(keyLIST)


###############################################################


# CIPHER FUNCTION
def cipher(key, message):
    key = key.split("-")
    N = int(key[0])
    e = int(key[1])

    message0 = ""

    counter = 0
    for char in message:
        if char in all_chars:
            code = str((all_chars[char] ** e) % N)
        else: code = str(char)

        if counter == 100:
            counter = 0
            code += "--"
        else:
            code += "-"
            counter += 1

        message0 += code

    if message0.endswith("-"):
        message0 = message0[:-1]
    elif message0.endswith("--"):
        message0 = message0[:-2]

    return message0


################


# DECIPHER FUNCTION
def decipher(key, message):
    key = key.split("-")
    N = int(key[0])
    d = int(key[1])
    decMSG = ""
    if "--" in message:
        message0 = message.split("--")
        for msgLIST in message0:
            pass

    else:
        message0 = message.split("-")

        for n in message0:
            try:
                n = int(n)
                n = n ** d
                n = n % N
                n = int(n)
            except:
                n = n

            decMSG += all_charsRVS[n]
    return decMSG


###################

if __name__ == "__main__":
    print getKEY()


"""
TEST SIDE


for i in range(100):
    
    keys = getKEY()
    open_key = keyTRANS(keys[0])
    hidden_key = keyTRANS(keys[1])
    ciphered = cipher(open_key, "DEneMe")
    deciphered = decipher(hidden_key, ciphered)
    print "=" * 30
    print ciphered
    print deciphered
    print open_key, hidden_key
    print "=" * 30
    print

print "="*10+"TAMAMLANDI"+"="*10

"""
