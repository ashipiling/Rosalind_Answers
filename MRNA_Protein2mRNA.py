protein = 'MWCSWKQRCGTVCDWSRQVRICDRGWDMSQHVVKFHCNTNLQYHIYLVWMTQWHTEGELAKNSKTPMIDEKNYGATGQFNKFVVERVTCVEQANSQEMGKMSHYYKRKKPQKKLSLSCQSSYDSMANDECREESHEKDIICRPYINSSGDKVVKIRSQGHRKIPAHSEKWMNDYPPSLRVCQWYCIMSPFMCPAWKVPKPWQPFSFQCKPKQKYHFYCHPVFYKGWFRHKEPDWPMILICWDVTMHHPYKFMLTQNNYFRGQPAEWNRVGATCTSHTLQKPWKYMDNPPKYWMIGGKHAEWGTNGFVLHLWCMSADREKQEVDQFHDGMGCTACEARNCWLACGQARKSRSVKVVVMGARDCPQGQDNRGIWFNLTWDRMNGQCAEPHSFLAPDSDTGGKMSWPSACALKPYWERMCKNGAKANGRIRKSVMWMCSCAPKNLVHDFPEYERFKVSKSCPPRMGQSSLFQYSINFWYSIQDGPFPFMEPLFNPAIIDVKYDSPHMTGFNWYHAHCVLRAWASQHDFGQCQPMYMYTQTCSTTLWQVPMAQCTMDMIDRMKRNRIYCMSTHQCSEPWILVGSCFAKPATIKDHSSQVKYAQPDAGQCWKDIFLFGYLLPLLRVEDIFRKGYRKSTALMENKLEYVKSYPTWSSIPRCGHPYNGLSVLYEHAVQIRYHLQTAWIVFVIYMTMDFSMMDAPHVIQVLDFEDNKVIIVMFTNAFQPWSDTSFWPRWYHYQRAQQTGTWGQHQKWMDYCAWNNAIFKNDPVQHNKSRTRFPNKWEPYMPMYTVPSLQICFSGQETTPKTVGAFEMLLSYTYHMTHPTCLEAQRHCGEKSHPILAWMEMPEVHNWRMRFHKWQEFGIHWMMDITFNHCFPKHVITCFQQVEVMGIGYAKFQVLPPYLDQQIRVYGFSSMWWKDGMWMQPMCRIHKREVALWKQKWHEDVDYIDFQGQFRPGDMVSKELGPCARYWLHSDFIDRHMCRYEICSTPQEKSVLLNEGEST'
#protein = 'MA'
Codon_number_dict = {'A': 4,'C': 2, 'D': 2, 'E': 2, 'F':  2, 'G':4, 'H': 2, 'I':  3, 'K':  2, 'L':  6, 'M':  1, 'N': 2, 'P':  4, 'Q': 2, 'R': 6, 'S': 6, 'T':  4, 'V': 4, 'W':  1, 'Y':  2}

i = 0
num = 3
while i < len(protein):
    num = num * Codon_number_dict[protein[i]]
    if num >1000000:
        num =  num % 1000000
    i += 1

print(num)
