#singular to plural
def get_words():
    """ comment 
    
    gizagiza
    """
    rows = int(input())
    words_list = []
    for i in range(rows):
        words_list.append(input())
    return(words_list)

get_words = get_words()

target = [x[-2:] for x in get_words]
rest = [x[:-2] for x in get_words]

def appender(target):
    appender = []
    for i in target:
        #zone "es"
        if (i in ("sh", "ch")) or (i[-1] in ("s", "o", "x")):
            appender.append(i + "es")
        #zone "ves"
        elif (i == "fe"):
            appender.append("ves")
        elif (i[-1] == "f"):
            appender.append(i[0] + "ves")
        #zone "ies"
        elif (i[-1] == "y") and (i[0] not in ("a", "i", "u", "e", "o")):
            appender.append(i[0] + "ies")
        #zone "s"
        else:
            appender.append(i + "s")
    return(appender)
    
appender = appender(target)
results = [x+y for x,y in zip(rest,appender)]   
for i in results:
    print(i)
"""
・末尾が s, sh, ch, o, x のいずれかである英単語の末尾に es を付ける
・末尾が f, fe のいずれかである英単語の末尾の f, fe を除き、末尾に ves を付ける
・末尾の1文字が y で、末尾から2文字目が a, i, u, e, o のいずれでもない英単語の末尾の y を除き、末尾に ies を付ける
・上のいずれの条件にも当てはまらない英単語の末尾には s を付ける
"""
