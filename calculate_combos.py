def word_dist(wordlist_file) -> list[int]:
    with open(wordlist_file, "r") as f: 
        wlist = f.read().splitlines()
        maxlen = max(map(lambda x : len(x), wlist))
        wlengths = maxlen*[0]
        for i in wlist:
            lidx = len(i)
            wlengths[lidx-1]+= 1
        return wlengths 
 


def partition(x, parts) -> list[list[int]]:
    plist = []
    if x < parts:
        return []
    if parts == 1:
        plist.append([x])
        return plist
       
    for i in range(1, x):
        for k in partition(x-i, parts-1):
            plist.append([i, *k])
    return plist 

def partition_to_combos(w_dist:list[int], p_arr:list[int]) -> int:
    if len(p_arr) == 0:
        return 0 
    tot = 1 
    for p in p_arr:
        if p > len(w_dist):
            return 0 
        tot*=w_dist[p-1]
    return tot  

def chars_to_combos(charnum, w_dist:list[int], wordblocks:int):
    

    total_combos = 0
    try:

        hyphens = wordblocks - 1 
        nonhyphens = charnum - hyphens 

        if nonhyphens < wordblocks:
            raise Exception("not enough characters for hyphen seperation")
        for c in partition(nonhyphens, wordblocks):
            total_combos += partition_to_combos(w_dist, c)

        
        
    except Exception as e:
        print(e)

    return total_combos 

