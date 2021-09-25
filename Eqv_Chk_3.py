print("=== EQUIVALENCY TESTING OF 2 PROPOSITIONS ===")
print("=== TEAM 2 ==================================")
print("=== EL5000-03 ADVANCED MATHEMATICS ==========\n")
###Last edit: 22-09-2021/11.13 WIB
play = 1
while (play > 0):
    try:
        print("Rules:\n" +
        "- Use letters for variables, 1 character for each variable.\n"+
        "- Use ~, v, ^, xor, ->, or <->\n"+
        "  for NOT, OR, AND, XOR, IF, or IFF.\n"+
        "- No characters allowed other than letters, operators, and brackets ().\n" +
        "Example: p->(q^~r)xorq\n")
         
        #Fungsi untuk mengambil variabel, dipanggil setelah input.
        def get_vrb(s):
            ops = ["~", "v", "V", "^", "<->", "->", "(", ")", "xor", "-", " "]
            st = s
            for ii in range(0,len(ops)):
                st = str(st).replace(str(ops[ii]),"")
            return "".join(sorted(set(st)))

        #Terima input proposisi dari user
        mx_input = {}
        vrb = {}
        vrb_cln = ""
        for ii in range(1,3):
            inp = input("Enter proposition " + str(ii) + ": ").replace(" ","")
            mx_input[ii] = inp
            vrb[ii] = get_vrb(inp)
        vrb_cln = "".join(sorted(set((vrb[1] + vrb[2]))))

        #Buat matriks kombinasi nilai variabel
        mx_vrb = {}
        nn = len(vrb_cln)
        cc = 2**nn
        for ii in range(0,cc):
            mx_vrb[ii] = bin(ii)[2:].zfill(nn)

        #Buat deklarasi variabel "p = [0, 0, 0, 0, 1, 1, 1, 1]" dst
        bit_vrbar = {}
        for ii in range(0,len(vrb_cln)):
            bit_vrbar[ii] = (str(vrb_cln[ii] + " = [" ))
        for ii in range(0,nn):
            for jj in range(0,cc):
                if jj < cc-1:
                    bit_vrbar[ii] = bit_vrbar[ii] + str(mx_vrb[jj][ii]) + ", "
                else:
                    bit_vrbar[ii] = bit_vrbar[ii] + str(mx_vrb[jj][ii])
            bit_vrbar[ii] = bit_vrbar[ii] + "]"
            exec(str(bit_vrbar[ii]))
            #Sampai di sini variabel p, q, r, dst sudah dideklarasikan, sehingga bisa dipanggil dan digunakan.

        #Simpan proposisi inputan ke dalam bentuk string.
        prop1 =str(mx_input[1])
        prop2 =str(mx_input[2])

        #Replace operator inputan user dengan operator yang bisa dieksekusi Python.
        op_inp = ["~", "v", "V", "^", "<->", "->", "xor", "-"]
        op_cln = ["not ", " or ", " or ", " and ", " == ", " <= ", "^", "not "]
        for ii in range(0,len(op_inp)):
            prop1 = prop1.replace(str(op_inp[ii]),op_cln[ii])
            prop2 = prop2.replace(str(op_inp[ii]),op_cln[ii])
        
        #Berikan kurung untuk variabel yang ada negasinya, agar diproses lebih dulu.
        for ii in range(0,nn):
            prop1 = prop1.replace("not " + str(vrb_cln[ii]),"(not " + str(vrb_cln[ii]) + ")")
            prop2 = prop2.replace("not " + str(vrb_cln[ii]),"(not " + str(vrb_cln[ii]) + ")")

        #Buat string pqr = "p, q, r" dst, dipisahkan koma, untuk digunakan di rumus final nanti.
        pqr = ""
        for ii in range(0,nn):
            if ii < nn-1:
                pqr = pqr + str(vrb_cln[ii]) + ", "
            else:
                pqr = pqr + str(vrb_cln[ii])

        #Pembentukan rumus final, contoh: [ p <= (q or r) for(p, q, r) in zip(p, q, r)]
        if len(vrb_cln) >1:
            #Jika varabelnya >1
            prop1 = "[" + prop1 + " for(" + pqr + ") in zip(" + pqr + ")]"
            prop2 = "[" + prop2 + " for(" + pqr + ") in zip(" + pqr + ")]"
        else:
            #Jika variabelnya hanya 1. Boolean tidak bisa iteratsi, jadi harus dipanggil manual 2x.
            #Contoh: [ p or p for (p, p) in zip(p, p) ]
            prop1 = "[" + prop1 + " for(" + pqr + ", " + pqr + ") in zip(" + pqr + ", " + pqr + ")]"
            prop2 = "[" + prop2 + " for(" + pqr + ", " + pqr + ") in zip(" + pqr + ", " + pqr + ")]"      
        
        #Eksekusi string proposisi dengan eval, menghasilkan array dari bit string.
        res1 = (eval(prop1))
        res2 = (eval(prop2))

        #Cetak truth table
        print("\nTruth table: ")
        for ii in range(1):
            ttl = "| " + ' | '.join(vrb_cln) + " | " + mx_input[1] + " | " + mx_input[2] + " |"
            print(ttl)
            print("-"* (len(ttl)))
            for jj in range(cc):
                print("| " + ' | '.join(mx_vrb[jj]) + " | " + str(res1[jj]).replace("True", "1").replace("False", "0").center(len(mx_input[1]), " ") + " | " + str(res2[jj]).replace("True", "1").replace("False", "0").center(len(mx_input[2]), " ") + " |")

        #Kesimpulan.
        if res1 == res2:
            print("\nConclusion: Both propositions are EQUIVALENT.")
        else:
            print("\nConclusion: Both propositions are NOT EQUIVALENT.")

    except Exception:
        print("\nError: The format of the proposition(s) you entered is incorrect. Please refer to the rules.")

    inp_play = input("Test other propositions? y/n: ")
    print()
    if inp_play == "n" or inp_play == "N":
        print("Thank you for playing. Have a nice day!\n")
        break