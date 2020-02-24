def commonChild(s1, s2):
    '''
    Given two strings, s1 and s2, where |s1| = |s2| and 1 <= |s1|, |s2|, <= 5000,
    find the longest common subsequence between s1 and s2.

    A common subsequence is an sequence of character that occurs and both strings
    and that can be separated by other non-common characters.

    output:
    The length of the longest common subsequence

    examples:
    X       Y       LCS
    ABC     ABCD    3 -> ABC
    ABC     ACBC    3 -> ABC
    ABCD    ABDC    3 -> ABC
    CBABC   ABCCB   3 -> ABC

    interesting write up on wikipedia:
    https://en.wikipedia.org/wiki/Longest_common_subsequence_problem

    There are three scenarios to consider:
                    {Null,                                  if i=0 or j=0
    LCS(X_i, Y_j) = {LCS(X_i-1, Y_j-1)^x_i,                 if i, j > 0 and x_i = y_j
                    {max[LCS(X_i-1, Y_j), LCS(X_i, Y_j-1)], if i, j > 0, x_i /= y_j
    Note that when i=0 -> X_0 = (), hence why LCS(X_0, ...) = Null
    '''
    if len(s1) == 0 or len(s2) == 0:
        return 0
    elif s1[-1] == s2[-1]:
        return commonChild(s1[:-1], s2[:-1]) + 1
    else:
        return max(commonChild(s1, s2[:-1]), commonChild(s1[:-1], s2))



if __name__ == '__main__':
    tests = [('HARRY', 'SALLY'), 
             ('AA', 'BB'), 
             ('SHINCHAN', 'NOHARAAA'), 
             ('ABCDEF', 'FBDAMN')
    ]
    answers = [2, 0, 3, 2]

    for (t1, t2), answer in zip(tests, answers):
        max_length = commonChild(t1, t2)
        test_result = ['FAIL', 'PASS'][max_length == answer]
        print(f'({t1}, {t2}): {test_result}')

    t1 = 'LZNGFTIHZHJSQGQQYICYKYAPAFJMYXIRFHFISJZJAVHMQLPBFXSPEEQAUJIIVSVLCRVHSMIGXQIVOOAFHIQOAOJBOTGJUPXEPQZFJSNLVDHCXMDRPPGTUNBIMARYQXUTMQVGOVZDYSCBCHRTTAYEIFFNAGFDFGEFJNAXKWUYNFPETFYTHRLEICJEFDFHJFADZFBRABLMDYNGIBXHGWDOWIFLWUKFVFUIITQGFRCGUYFZINJYIGXCKNPVDPMUKTVOIBSIUUDQDWXTJAIGVSFROIGSEOWNZAWDRIZFLFQAYQKETDOYLUOHSVUYOJLDCJNIWDOFBRLWXQSCCTDEQHGHUXCHTCFSZRTRESSXNVOXFAHSWUAVJXMHCKRCOYVENGGBSXXYPEPUAQFNNCRVFQQDFCBPNTTNISDVORWBJBBCVVNLYUTTSBPRXSKYFEKOMIZCGNSQHZYVCHHILQLGCLIKTNCLQUOUAXFNHJPIZYBYWSVMGUVAGXANTEZHSDUDBVVCAGCPKJAQXIOQOCTNNOOFUYZEGGPAEQGRRDREZUSVTKCQAZQDZAEIIGOCJPMQXRHRFQTCBNEMSAPSSLHXJVDBCSGQVUPGNCZKTFEBRIKWKSYXWRAHGNGYLLXFKJOUNXKDRWMBVOZGEOBAYYNFDNHHWFVPOKWUFLZTZUCMLGFVUWFXSVYYUBGRHAUWHBQSNIHENTXADZCCZZZPOPESVYCROMUBJPDGBGUHBSMUQSYGEHUCRDACDYJIPYBLPXQUOLSELHBBBYQHKIOVFMSXANOMKMOXNPTGZSVHMCAEFSCNMCPHFUHOMNRNEQBOSLMAHJAMSMQMGKTLVKBVTSUDDWKXHHIIAFVNMQIHVVEPACCEVVECWOBVZVTWWMDIKYZAGZJOLQCINZZVZFNJGTCXXVLRAGJQFDMYMNKQDWNCLRTPYCCXEQFGKQWQSSYXNGELLNMAKNPIKFNKUIDCRUTWSTRKIHUAOGMPXOBQTFFAQMKG'
    t2 = 'BLCRCQQMXZCBACBDSFGIQDKFFHGPOGSZLHLXNZSSXRGVKIGNABASNFZDHVJOAINPZEZNDWOWSEJGMOVPPXHBERDJXLJSPAQDKNQEJMTBMVTPRXOCHYPKMDGRIHUPBQWZBNIXJBPTFYRMIUNXLVKPIRLLGJVGBIBIGDRIWGKEIKKYGCCFHCTEVNJPWFCFPDOXQDYGHRRNXTFQRGCTITBUEPHPEIXQMYSKLYQXZWVRWDBYLJRBOWRAHRWUJWZKEGBCEHVTKJERFIJVWWVSRVNIDHYVEYIWAPHYSIKCBDBDWXAWXEHRFMHCQNHTBYOFYJBIKJGUDIMQKNFCKMWNGVROISVLPZZCRUKHBWPSHRBSERBQOJXFTKSDDCRBIACQMHIOQBNESXTNURRXONVMNGZBMBDZDBWGXMFNCJWVUICKVQHUDDMVHNHRAHRDHOITKDDRRMFSQFZSLAASQSKJTVWTOSWQSPEARPEWADMMNSPCZTMKGVQOBGOBMGICUZNBEBZBFDRPFJPLCJOUTZBNJAKTTMQPQVQOGVHIBNWFXOQWSMUSCBBCZURZOYRHSTKIFUXWROLBQBLYEDXQHKXYZNWVDCRAABKUBAPCPLKPZRQWNSWRCLNGDYLICBQAPPFNIDNCRMZEJJNNSUDDMAAOJPDQZPBRYKMVACVMTNNPQZBWHYALBHLDAYTJGJOWXQYVQQVNHLJXVVEXIPHEZZCKLKXNKLAYSHPSWWBPOQXZJYNFWBYVMMTMKFWJVPGHTGXCMBKTBWIXQJAMGVNRALOCACXIICCVEWKKSFDBMPRJUEYCHROEDXTKYJYSGVITYMVSAAEVKDAEDXWDBSHFTXDCDRTLCCFAKWSBNTPUSXIGTSXOVPIMVURDXOGBOOQAHISZBKADCRXVSJSICXWQNMQGCCPTHWHKFKDXUGARNLREDXZIROXZTXPAVOGORNCVXGAMFVJUKLGPHSZKVVMRMFXLYUZNDUYOIIHJCKDWQXNCIYNG'
    
    commonChild(t1, t2)
