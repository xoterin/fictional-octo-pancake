# Start by converting Hexadecimals to Binary Form and Binary to Hexadecimal Form
# Source https://www.rapidtables.com/convert/number/hex-to-binary.html

def hexBin(s):
    convert2Bin = {'0' : "0000", 
          '1' : "0001",
          '2' : "0010", 
          '3' : "0011",
          '4' : "0100",
          '5' : "0101", 
          '6' : "0110",
          '7' : "0111", 
          '8' : "1000",
          '9' : "1001", 
          'A' : "1010",
          'B' : "1011", 
          'C' : "1100",
          'D' : "1101", 
          'E' : "1110",
          'F' : "1111" }
    resultBin = ""
    for i in range(len(s)):
        resultBin = resultBin + convert2Bin[s[i]]
    return resultBin
      
def binHex(s):
    convert2Bin = {"0000" : '0', 
          "0001" : '1',
          "0010" : '2', 
          "0011" : '3',
          "0100" : '4',
          "0101" : '5', 
          "0110" : '6',
          "0111" : '7', 
          "1000" : '8',
          "1001" : '9', 
          "1010" : 'A',
          "1011" : 'B', 
          "1100" : 'C',
          "1101" : 'D', 
          "1110" : 'E',
          "1111" : 'F' }
    resultHex = ""
    for i in range(0,len(s),4):
        bh = ""
        bh = bh + s[i]
        bh = bh + s[i + 1] 
        bh = bh + s[i + 2] 
        bh = bh + s[i + 3] 
        resultHex = resultHex + convert2Bin[bh]
          
    return resultHex
  
# Next convert binary to decimal and vice versa
# Source https://www.geeksforgeeks.org/binary-decimal-vice-versa-python/

def binDec(binary): 
        
    bin1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal
  
# Decimal to binary conversion
def decBin(num): 
    resultBin = bin(num).replace("0b", "")
    if(len(resultBin)%4 != 0):
        div = len(resultBin) / 4
        div = int(div)
        counter =(4 * (div + 1)) - len(resultBin) 
        for i in range(0, counter):
            resultBin = '0' + resultBin
    return resultBin
  
# Start the permutation
def permutation(k, arr, n):
    permutate = ""
    for i in range(0, n):
        permutate = permutate + k[arr[i] - 1]
    return permutate
  
def leftShift(k, n_shifts):
    s = ""
    for i in range(n_shifts):
        for j in range(1,len(k)):
            s = s + k[j]
        s = s + k[0]
        k = s
        s = "" 
    return k    
  
def xor(a, b):
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans
  
# Initial Permutation Table
# Source https://csrc.nist.gov/csrc/media/publications/fips/46/3/archive/1999-10-25/documents/fips46-3.pdf

initial_perm = [58, 50, 42, 34, 26, 18, 10, 2, 
                60, 52, 44, 36, 28, 20, 12, 4, 
                62, 54, 46, 38, 30, 22, 14, 6, 
                64, 56, 48, 40, 32, 24, 16, 8, 
                57, 49, 41, 33, 25, 17, 9, 1, 
                59, 51, 43, 35, 27, 19, 11, 3, 
                61, 53, 45, 37, 29, 21, 13, 5, 
                63, 55, 47, 39, 31, 23, 15, 7] 
  
# E BIT Selection Table
bit_e = [32, 1 , 2 , 3 , 4 , 5 , 4 , 5, 
         6 , 7 , 8 , 9 , 8 , 9 , 10, 11, 
         12, 13, 12, 13, 14, 15, 16, 17, 
         16, 17, 18, 19, 20, 21, 20, 21, 
         22, 23, 24, 25, 24, 25, 26, 27, 
         28, 29, 28, 29, 30, 31, 32, 1 ]
  
# Straight Permutaion Table
straight = [ 16,  7, 20, 21,
        29, 12, 28, 17, 
         1, 15, 23, 26, 
         5, 18, 31, 10, 
         2,  8, 24, 14, 
        32, 27,  3,  9, 
        19, 13, 30,  6, 
        22, 11,  4, 25 ]
  
# S-box Table
sbox =  [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], 
          [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], 
          [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], 
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],
             
         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], 
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5], 
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15], 
           [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]], 
    
         [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], 
           [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1], 
           [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7], 
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]], 
        
          [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], 
           [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9], 
           [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], 
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ], 
         
          [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], 
           [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6], 
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14], 
           [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]], 
        
         [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], 
           [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], 
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6], 
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ], 
          
          [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], 
           [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6], 
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2], 
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ], 
         
         [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], 
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2], 
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8], 
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]
    
# PreOutput
final_perm = [ 40, 8, 48, 16, 56, 24, 64, 32, 
               39, 7, 47, 15, 55, 23, 63, 31, 
               38, 6, 46, 14, 54, 22, 62, 30, 
               37, 5, 45, 13, 53, 21, 61, 29, 
               36, 4, 44, 12, 52, 20, 60, 28, 
               35, 3, 43, 11, 51, 19, 59, 27, 
               34, 2, 42, 10, 50, 18, 58, 26, 
               33, 1, 41, 9, 49, 17, 57, 25 ]
  
def encrypt(pt, rkb, rk):
    pt = hexBin(pt)
      
    # Initial Permutation
    pt = permutation(pt, initial_perm, 64)
    print("After inital permutation", binHex(pt))
      
    # Splitting
    left = pt[0:32]
    right = pt[32:64]
    for i in range(0, 16):
        #  Expansion D-box: Expanding the 32 bits data into 48 bits 
        right_expanded = permutation(right, bit_e, 48)
          
        # XOR RoundKey[i] and right_expanded 
        xor_x = xor(right_expanded, rkb[i])
  
        # S-boxex: substituting the value from s-box table by calculating row and column 
        sbox_str = ""
        for j in range(0, 8):
            row = binDec(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
            col = binDec(int(xor_x[j * 6 + 1] + xor_x[j * 6 + 2] + xor_x[j * 6 + 3] + xor_x[j * 6 + 4]))
            val = sbox[j][row][col]
            sbox_str = sbox_str + decBin(val)
              
        # Straight D-box: After substituting rearranging the bits  
        sbox_str = permutation(sbox_str, straight, 32)
          
        # XOR left and sbox_str
        result = xor(left, sbox_str)
        left = result
          
        # Swapper
        if(i != 15):
            left, right = right, left 
        print("Round ", i + 1, " ", binHex(left), " ", binHex(right), " ", rk[i])
      
    # Combination
    combine = left + right
      
    # Final permutaion: final rearranging of bits to get cipher text
    cipher_text = permutation(combine, final_perm, 64)
    return cipher_text
  
pt = input('Enter your plaintext (UPPERCASE): ')
key = input('Enter your key (UPPERCASE): ')
  
# Key generation
# --hex to binary
key = hexBin(key)
  
# --permuted choice
permuted = [57, 49, 41, 33, 25, 17, 9, 
        1, 58, 50, 42, 34, 26, 18, 
        10, 2, 59, 51, 43, 35, 27, 
        19, 11, 3, 60, 52, 44, 36, 
        63, 55, 47, 39, 31, 23, 15, 
        7, 62, 54, 46, 38, 30, 22, 
        14, 6, 61, 53, 45, 37, 29, 
        21, 13, 5, 28, 20, 12, 4 ]
  
# getting 56 bit key from 64 bit using the parity bits 
key = permutation(key, permuted, 56)
  
# Left Shifts 
shift_table = [1, 1, 2, 2, 
                2, 2, 2, 2, 
                1, 2, 2, 2, 
                2, 2, 2, 1 ]
  
# Permuted choice 2
permute2 = [14, 17, 11, 24, 1, 5, 
            3, 28, 15, 6, 21, 10, 
            23, 19, 12, 4, 26, 8, 
            16, 7, 27, 20, 13, 2, 
            41, 52, 31, 37, 47, 55, 
            30, 40, 51, 45, 33, 48, 
            44, 49, 39, 56, 34, 53, 
            46, 42, 50, 36, 29, 32 ]
  
# Splitting 
left = key[0:28]    # rkb for RoundKeys in binary 
right = key[28:56]  # rk for RoundKeys in hexadecimal 
  
rkb = []
rk  = []
for i in range(0, 16):
    # Shifting the bits by nth shifts by checking from shift table
    left = leftShift(left, shift_table[i])
    right = leftShift(right, shift_table[i])
      
    # Combination of left and right string
    combine_str = left + right
      
    # Compression of key from 56 to 48 bits 
    round_key = permutation(combine_str, permute2, 48)
   
    rkb.append(round_key)
    rk.append(binHex(round_key))
  
print("Encryption")
cipher_text = binHex(encrypt(pt, rkb, rk))
print("Cipher Text : ",cipher_text)
  
print("Decryption")
rkb_rev = rkb[::-1]
rk_rev = rk[::-1]
text = binHex(encrypt(cipher_text, rkb_rev, rk_rev))
print("Plain Text : ",text)
