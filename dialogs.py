#!/usr/bin/python
# -*- coding: utf-8 -*-

a=input("Cien. liet., lūdzu, ievadi skaitli: ")
# 3. python vide visi input rezultāti ir ar str datu tipu
# tāpec ievadītā lieluma datu tips vēlāk ir jāparveido
a = int(a)

# python valoda balstās uz C valodas => print strādā līdzīgi printf
#http://www.cplus.com/reference/cstdio/printf/
print("Liet., Tu esi ievadījis skaitli: %d"%(a))
aa = a * a
print("Tavs skaitlis kvadrātā ir: %d"%(aa))
