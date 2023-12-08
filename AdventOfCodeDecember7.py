# AdventOfCode 07.12.2023

# Explanation: In Camel Cards, you get a list of hands, and your goal is to order them based on the 
# strength of each hand. A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. 
# The relative strength of each card follows this order, where A is the highest and 2 is the lowest.
# Every hand is exactly one type. From strongest to weakest, they are:
# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456
# Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.
# If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand. 
# If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the same label, 
# however, then move on to considering the second card in each hand. If they differ, the hand with the higher second card wins; otherwise, 
# continue with the third card in each hand, then the fourth, then the fifth.

example1 = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

example2 = """K99QT 53
TKQ7T 320
22A7J 490
267J9 69
665JJ 431
K856J 605
977K9 552
KKK8K 285
53697 370
3J337 879
84A9K 901
K4289 211
4JA46 100
K452K 315
3K48Q 239
99TT9 985
A7JA9 582
836AT 770
J2KKK 61
KK7KK 37
QTAJK 351
T4578 198
TK55T 513
44K9J 853
KQT58 203
66A6J 881
K77KK 31
6666Q 410
8J8KJ 522
69KQ7 594
T27J3 110
44999 461
98885 231
55655 372
43343 958
82247 300
33336 957
59JT4 303
AQAJA 691
J3626 696
9379A 788
JTTTA 795
442A6 989
73933 857
979QQ 817
65566 150
6T565 182
4T5J5 9
TT3TT 147
J8338 229
6AQ8Q 636
79KK7 933
8T6TT 145
TTT4T 177
KAK52 952
9K83J 469
55855 718
TTT5T 209
9555Q 309
AA3A5 327
647T3 310
22234 717
5TT9J 5
T5A86 831
3J333 544
66767 571
9A777 269
43QTT 822
888J5 422
T4435 259
75394 17
KJA2A 95
A2KK4 762
4T73T 595
7Q97Q 3
9J998 964
KTK2K 267
87Q87 375
4744T 909
3TTA7 637
6J767 409
3KT7K 588
7T6T6 302
39959 887
TKTKT 144
K99K2 777
48237 403
K93A3 886
369AA 350
43QK6 193
657KA 199
7398Q 314
77778 38
ATTAA 903
A9A93 112
T8TT4 128
776K5 509
868T9 641
6T5J5 910
TQ722 976
9A9QQ 224
J93J5 948
JTTT7 576
JKAQK 184
AAAA5 764
J3939 262
7K7K8 204
88928 663
T8T8T 352
5KJQQ 477
22TTT 833
299Q9 437
67J42 393
3A73A 961
982K7 614
J55Q5 549
99699 741
4T4T6 366
55522 256
39898 301
9AA49 137
9A6AA 706
Q6668 740
322J2 716
K5454 439
Q3Q77 954
78J49 946
66828 242
652A9 340
QQJQQ 342
2Q2Q2 92
2K352 871
7Q5A9 361
QAQQQ 925
QQA26 625
97J3Q 932
KQ965 675
8J88T 738
JK84K 19
AA333 130
TTTKT 536
7K8Q3 902
A4A5A 529
393K9 192
85558 216
TQQ77 4
A5AQ9 276
62672 90
246T8 674
Q424T 436
474K4 970
733J7 156
73T23 713
K864J 676
K6K6K 75
5524A 270
AA7AA 89
A6764 105
JK555 103
3Q322 124
89K36 66
7J724 686
KJKJK 939
Q7793 219
J5A5J 296
7AATK 666
4442K 429
4J734 504
28TQ3 668
9T623 862
7Q7A5 810
468A7 517
44Q8Q 569
6TT6T 36
69965 824
2QT39 864
585T5 744
84888 865
QQJ6A 702
66656 365
K9T38 377
56576 604
95665 516
96496 657
5KK6K 274
23857 982
855J9 13
T25QQ 264
Q9K2K 354
37K73 631
88A57 487
689KT 971
898QQ 701
2QA2J 482
99J97 427
77A76 167
7TK93 596
34647 579
46J88 460
QT4AT 380
8T488 553
32A44 726
J3332 635
K2J42 897
93339 55
6J7Q6 311
Q9QQJ 7
47444 539
93399 567
ATJAT 77
TTQQQ 859
9Q999 281
K752A 412
87977 205
92334 995
79QQQ 26
JJTA8 581
A4J24 444
4J444 921
Q9KK9 255
45K2A 728
KA5J6 621
7J277 850
56884 67
44JQQ 240
67Q7Q 426
QT6T5 265
AA9A2 252
A9KA4 649
TTQTT 554
4A444 698
95586 70
7J45Q 996
48848 500
Q3AAA 474
K3A7T 980
5655J 977
75J92 577
TA94A 951
336T3 400
442QA 761
K2J53 537
JQQ22 470
AJA53 88
73797 672
657TT 869
2TTTT 142
JT49K 227
A7A77 338
5J2Q8 221
92269 664
7A965 307
3355J 308
J9T98 518
69TQ5 899
57455 355
AKA5A 489
79K77 39
72767 298
AA858 695
K3JTJ 283
4KKJ4 258
7K248 704
Q9J47 617
3QQT8 820
87J3Q 540
9A6A9 438
3AT7A 344
5656K 478
66663 385
K2KQ2 572
37747 612
58T72 690
Q47A9 368
8K53Q 687
99799 856
TJAQ2 476
KA4A4 1000
Q634A 408
TKK88 785
829JK 633
26446 132
JJJJJ 512
T666T 51
QQQQ3 751
5A35A 534
2222K 432
5K72J 378
866JK 566
5T2AJ 11
KK5JK 898
97T2J 163
7757J 247
33237 640
T554K 975
K666K 940
2T272 91
7A988 960
T9736 671
999K9 68
95595 802
A5JJ3 652
78829 867
4JJJ4 148
AA84J 541
4T4T4 563
A334J 931
9T29T 416
96845 992
A22AK 555
224KK 584
84484 271
22A88 986
37AKJ 49
JQ6QQ 284
33853 280
TTJ77 935
66J66 720
468A3 185
QA958 642
888J8 580
JQQJQ 560
J29J9 57
6888J 14
QJ8TK 440
AQQAA 136
AA9AA 823
6ATTT 175
7T42A 402
A7J9K 907
53A87 805
26262 930
22262 507
27JK4 854
QAQTT 731
8TKTK 418
TTT44 244
J45TJ 98
86898 681
444AK 929
KK88K 521
8356T 644
TKT6T 401
Q99QQ 415
96299 659
8T888 598
5T955 888
85572 658
T59K7 471
7Q77Q 927
AAA7K 949
TA55A 278
KJJK8 692
AA5J4 638
AKK4A 861
77767 774
K4KKK 143
TKKQQ 10
Q598T 794
4A44J 201
288QQ 602
3TT2T 80
Q5855 955
AKKKA 43
66QQQ 942
97977 29
J444J 157
3AAAA 273
3J988 420
JAAAA 715
4KQJ3 250
KJ4K3 480
QQ3Q3 113
3883Q 421
6T4TT 44
77373 472
4K74K 76
AA226 943
4Q4Q4 305
7J729 763
Q4649 456
TKTJA 966
6JJ24 131
5K855 101
AAJ3A 743
82Q5A 558
854Q8 186
TTTT9 74
AKAAA 323
KK5K5 556
3A69Q 164
2AAAA 404
Q4QQ4 162
7T577 313
5QQQQ 618
87535 266
4A4A4 356
875J5 33
9K225 479
JQK95 941
KQT28 826
53356 760
QQ5Q5 16
696J9 498
TJTT6 836
7A7TA 979
999AA 170
55K5K 523
733T3 746
39929 503
686AJ 885
QQKQQ 667
A8KK8 96
Q555A 446
Q2QQJ 797
QQJQ8 445
6T6J6 583
65565 451
535A6 765
45QKT 453
A26K6 816
J4JJ8 60
35535 510
T85KT 613
9Q3Q9 358
53425 680
4JA45 878
76328 481
QJ2AA 813
QK4KQ 324
K9KJJ 919
22822 734
JJJQ9 441
33393 928
29299 495
69666 825
T5Q82 423
43687 834
TTQ6A 682
7KQJ6 736
TK2JA 65
665Q3 232
A7297 593
Q6Q33 837
522J5 272
44424 891
57T63 41
222J9 722
99797 228
33A33 711
5TT7K 458
KTTT4 22
4774J 430
9J889 257
88483 225
KKKKT 678
7QQQQ 322
37337 607
QAQJA 997
46696 316
4A4AA 924
QQ3J3 835
72Q72 236
4AAKA 254
T989T 557
K7Q76 115
77JT6 591
683A7 390
A97Q7 295
AA8AA 895
4KK5K 660
J5665 155
JAJA5 920
3T333 806
5TJ48 287
J4434 332
98TQT 492
J539K 781
9QQ94 452
TA593 745
A4JA4 515
2T332 609
2KKKK 494
4KKKA 30
Q254J 590
4T28A 608
T9Q7K 275
48843 279
9629K 526
778J7 329
J67K5 697
26A22 220
67J97 849
84Q88 863
73777 248
34KA2 286
A9A9A 126
Q2457 984
55672 106
77T89 165
TQQ44 413
KKJKK 497
Q9482 417
88999 550
TTAA5 911
TK2T2 790
44445 578
J55T5 169
T738A 847
55554 789
AJAKQ 829
4Q492 394
QT5Q6 433
Q5Q55 917
KQAA5 801
QQ242 870
92A76 334
7TT96 610
J334K 520
T333J 527
J464K 149
QQJ8T 349
2KAKK 561
K3JK9 40
TTJJ8 213
57557 151
9ATAA 434
JTTT3 990
TTTT7 998
6T3K3 384
45738 293
999TK 288
999JJ 312
333TT 15
8A7TK 650
35JT4 784
29889 796
TT669 114
8585J 502
75555 772
5JT59 173
AJAJA 99
5842T 326
8TA26 214
99T29 776
8TK44 896
74J48 730
78888 123
3T763 139
TT8T9 548
8Q737 405
2AK5J 684
8885Q 804
33Q36 183
2K935 987
3Q55K 346
36933 543
K575K 435
94847 947
7K666 107
9TTTJ 367
KK636 799
J7TTA 766
74K74 484
Q5445 945
2A662 48
886AK 525
A2555 395
26J66 188
22333 771
J2KJ2 533
32329 330
4T4TQ 455
836KJ 318
29999 830
KKAJT 905
QQA9A 673
33QTJ 179
AQ748 719
4Q3T8 46
AJ79J 978
44Q48 524
87277 347
2JQ4T 611
Q6868 773
A7355 950
89Q68 263
4947J 1
QQA7Q 134
TK32T 138
45544 838
J5QQQ 936
7T656 488
KQQ8Q 111
A6T95 122
24T4T 291
64323 646
4JQ4T 268
Q9J82 851
9JQJQ 710
22T2T 606
9J969 564
36633 735
2222J 972
2K77J 292
2T836 406
9J379 721
2T3T3 253
55Q55 875
KKT3T 197
754JJ 643
25577 261
96776 81
33Q33 756
4455J 723
274TJ 506
43432 118
J6JA9 634
68Q2T 923
JTTJT 47
44777 215
K5K5J 937
52252 391
T6365 883
JT4JA 808
25K9A 336
6TTTT 876
67767 703
88485 160
AAJ8A 814
Q4K66 798
853K6 873
K943A 135
74T8A 732
J8T77 780
Q32A6 246
733AT 965
68536 108
K8K88 815
75A42 234
9Q24T 967
J4AAK 514
77KK7 397
89889 93
KJAKK 129
8KA88 973
488A4 62
555J5 226
3AA6J 153
35239 679
22694 574
J3344 450
9J999 545
TKAT6 768
57JQ9 969
22882 189
777A7 24
33323 858
J85A9 260
TT2AT 993
KK29T 200
55595 821
A5555 615
82243 125
82338 586
TK385 457
QQ89Q 243
7T98T 202
34K37 597
8889Q 508
KKTKQ 289
TTTTJ 944
QA8A9 622
33KK3 277
2J233 630
K5666 819
4J824 812
7888K 45
K42K7 846
23A49 485
98888 337
2JJ22 468
966A3 662
J4JT3 86
8KJ33 369
KQ3A8 237
AAQA6 904
JKAKA 538
K9T43 968
44745 34
8A4J8 78
K523K 465
JKAK6 294
37J77 207
33TTT 988
A8TA8 463
Q56Q8 194
QQ443 319
382Q9 532
J66J6 568
A92T4 388
K5J49 172
84288 428
2QK99 752
5QT27 767
37Q54 592
TAAAA 475
AA9Q9 868
97T3Q 58
TAAJJ 120
7TQ85 360
45585 119
JQ252 793
39229 655
66JAA 133
67276 233
66646 493
A8A89 725
K5K4J 620
79KK9 818
AA4AT 218
86888 685
3A252 353
T4TAT 589
TJ269 190
3366T 449
J87Q7 800
77K77 656
Q5856 628
9TT33 874
8J8TA 158
33335 35
4K5J5 587
87877 104
9A66A 168
77277 843
52545 570
2QA3K 841
72K75 727
A8AA3 535
25J5Q 729
T3939 363
4K66J 832
99989 845
36Q53 916
TTKJK 462
764AT 963
88328 934
9229K 708
2J886 328
97A38 448
799J7 755
5AQAT 749
7KK76 146
KAA2T 109
2222T 882
32257 117
3KQ3K 6
AQAAA 54
599QQ 442
44423 809
TT99T 84
523Q2 501
33433 884
2J894 918
44484 411
5J9QT 926
J7872 63
K2KK2 981
655AA 217
9949Q 42
4ATJQ 991
2294J 811
K32JA 79
5T84Q 839
A8K24 530
57T67 333
JQ4TK 791
Q58Q5 235
74756 627
62TT6 742
34443 208
7Q7QJ 102
9Q6TT 792
TA797 72
67K56 645
5K5QQ 629
62666 669
6T5KT 348
66K32 531
J2AAA 331
4KJ7T 223
T88K8 191
55244 714
A4J57 983
Q777K 251
QQKKQ 71
A8858 196
4J8JK 387
88636 386
32J56 230
6Q833 23
TT8T2 877
A8JK4 483
22A24 600
35555 166
4AKQJ 748
94448 52
92229 842
292J3 912
6J4AA 783
A85JJ 890
64556 210
QTT9T 304
7KJKK 180
7777T 915
59TA7 238
TT8TT 206
44434 953
33373 906
2J57A 828
6QJJ7 889
9KA9K 27
T22KK 651
KKJQK 852
Q7373 775
9298J 994
TT739 654
88787 491
J68QJ 661
K8QK4 893
25T25 381
2K895 152
J777A 626
62562 364
Q64JQ 32
98337 28
4A7T4 299
36J33 245
83883 639
59495 962
66T6K 127
JTJ2T 779
KJ4Q6 424
J822J 306
3KQ45 362
25QQ5 807
Q8TJ7 389
QJQ37 94
T2QKK 747
25555 632
Q6Q69 64
J2767 737
333JJ 195
9A9A5 689
823QQ 707
8T5T8 443
23AK6 59
86446 892
93964 8
QKKQ8 97
59T86 866
Q3QQ9 677
55344 414
57KJ5 860
337A7 575
9JJ9K 699
3AA38 343
37273 85
22AAA 154
A9896 601
45J97 18
T7689 599
55537 573
JTQT6 473
262Q2 616
8J5QQ 486
25444 705
2K2K2 922
93QK2 20
JT9AA 396
83JTK 757
J9AA4 827
J3Q44 159
922TT 505
Q22A9 803
3753K 700
T5545 222
777QA 840
2T987 908
JJJ34 547
J9Q85 187
34994 880
K7AKJ 670
9QQ4Q 647
522JT 855
K8K58 750
55JJ5 653
J3977 249
KJKJT 419
8866J 383
56AQ4 87
5444A 392
J77J7 345
495K9 848
4J449 844
96T66 999
66628 758
66684 171
47767 454
TJ54A 21
58888 778
J8J88 467
96JKK 585
8A5J5 624
2A222 603
44494 759
J3A9K 956
8854J 141
5JK22 341
T5Q25 359
K3533 693
44294 914
JJJ7A 382
9K654 241
5A44A 900
777JQ 12
A6AA6 176
T888T 399
AJ77A 739
J636J 499
55KQK 551
79JK9 447
A888A 528
45T49 466
683T4 459
KT7KJ 140
88855 282
85T7T 753
542A8 496
96554 769
45A46 56
642K5 511
87AAJ 297
3T28J 754
A266J 709
9QQK2 83
T32Q2 425
777J7 398
9A5AJ 373
3958K 683
9AAJA 733
92Q9Q 665
777T3 786
529J8 290
592TA 371
9Q99Q 787
8444A 913
AJKAT 872
95K99 174
KK4K3 339
34A73 694
25222 374
Q7Q7Q 325
32T54 321
53K9Q 542
A8TAJ 73
4242J 648
27772 161
2K242 335
3J6AQ 464
3999K 407
52JTT 619
688J5 959
2TT6Q 376
K83AJ 379
372KQ 357
A6T96 25
65AT2 565
AAA6A 181
J8JJJ 623
3Q3Q3 559
K38KK 50
72227 317
537QQ 546
99KK9 212
5J7J5 121
3QT42 782
9QQ32 116
JTKK5 724
J99TT 938
AQQQA 688
7729T 519
8TKQ3 712
53447 562
63679 974
TTTA8 2
9K642 82
44T44 894
T9TQ4 178"""

# Task one: 
# Find the rank of every hand in your set. What are the total winnings?

customRanking = {"A" : 0, "K" : 1, "Q" : 2, "J" : 3, "T" : 4,
                 "9" : 5, "8" : 6, "7" : 7, "6" : 8, 
                 "5" : 9, "4" : 10,"3" : 11, "2" : 12}

def findBestHand(string):
    hands = []
    for hand in string.split("\n"):
        handBid = [hand[:hand.find(" ")], hand[hand.find(" ")+1:]]
        hands.append(handBid)
    def handKey(x):
        countRank = {char: x[0].count(char) for char in set(x[0])}
        maxCount = max(countRank.values(), default=0)

        if maxCount == 1:
            number = 0
        if maxCount == 2:
            number = 1
        if maxCount == 2 and len(countRank) == 3:
            number = 2
        if maxCount == 3:
            number = 3
        if maxCount == 3 and len(countRank) == 2:
            number = 4
        if maxCount == 4:
            number = 5
        if maxCount == 5:
            number = 6
        
        return (
            -number,
            customRanking.get(x[0][0], float('inf')),
            customRanking.get(x[0][1], float('inf')),
            customRanking.get(x[0][2], float('inf')),
            customRanking.get(x[0][3], float('inf')),
            customRanking.get(x[0][4], float('inf')),
            x[0]
        )

    hands.sort(key=handKey)
    hands.reverse()
    sum = 0
    counter = 1
    # print(hands)
    for i in range(0,len(hands)):
        sum += int(hands[i][1]) * counter
        # print(str(counter) + "*" + str(hands[i][1]) + "=" + str(int(hands[i][1]) * counter))
        counter += 1
    return sum

# Task two: 
#  cards can pretend to be whatever card is best for the purpose of determining hand type; for example, 
# QJJQ2 is now considered four of a kind. However, for the purpose of breaking ties between two hands of the same type, 
# J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q
# Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?

customRankingWithJoker = {"A" : 0, "K" : 1, "Q" : 2, "T" : 3, "9" : 4,
                 "8" : 5, "7" : 6, "6" : 7, "5" : 8, 
                 "4" : 9, "3" : 10,"2" : 11, "J" : 12}

def findBestHandWithJoker(string):
    hands = []
    for hand in string.split("\n"):
        handBid = [hand[:hand.find(" ")], hand[hand.find(" ")+1:]]
        hands.append(handBid)
    def handKey(x):
        countRank = {char: x[0].count(char) for char in set(x[0])}
        amounts = sorted(countRank.values())
        
        try:
            jokers = int(countRank.get("J"))
        except: 
            jokers = 0
        
        if jokers == amounts[-1]:
            del amounts[-1]

        number = 0
        # Fivepair
        if jokers >= 5 or amounts[-1] + jokers >= 5:
            number = 6
        # Fourpair
        elif jokers >= 4 or amounts[-1] + jokers >= 4:
            number = 5
        # Flush
        elif amounts[-1] + jokers >= 3:
            rem_jokers = amounts[-1] + jokers - 3
            if len(amounts) >= 2 and amounts[-2] + rem_jokers >= 2 or rem_jokers >= 2:
                number = 4
            else: number = 3
        # Twopair
        elif amounts[-1] + jokers >= 2:
            rem_jokers = amounts[-1] + jokers - 2
            if len(amounts) >= 2 and amounts[-2] + rem_jokers >= 2 or rem_jokers >= 2:
                number = 2
            else: number = 1
        # Highcard
        else:
            number = 0

        value.append(number)
        return (
            -number,
            customRankingWithJoker.get(x[0][0], float('inf')),
            customRankingWithJoker.get(x[0][1], float('inf')),
            customRankingWithJoker.get(x[0][2], float('inf')),
            customRankingWithJoker.get(x[0][3], float('inf')),
            customRankingWithJoker.get(x[0][4], float('inf')),
            x[0]
        )
    
    value = []
    hands.sort(key=handKey)
    value.sort()
    value.reverse()

    for i in range(0,len(value)):
        hands[i].append(value[i])

    hands.reverse()

    sum = 0
    counter = 1
    # print(hands)

    for i in range(0,len(hands)):
        sum += int(hands[i][1]) * counter
        counter += 1
    return sum

if __name__ == "__main__":
    print("Result with function findBestHand:")
    print("Example 1:")
    print(findBestHand(example1))
    print("Example 2:")
    print(findBestHand(example2))
    print("Result with function findBestHandWithJoker:")
    print("Example 1:")
    print(findBestHandWithJoker(example1))
    print("Example 2:")
    print(findBestHandWithJoker(example2))
