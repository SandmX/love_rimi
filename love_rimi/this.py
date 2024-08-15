
s = """Gb Evzv, ol Fnaqzrlre
Tenprshy orlbaq gur fvzcyvpvgl bs pbqr,
Yviryl whfg yvxr gur rkdhvfvgrarff bs na nytbevguz.
Nf pbzzragf yvtug hc gur zrnavat bs pbqr,
Lbhe fzvyr raqbjf gur pbybe bs yvsr gb zr.
Yvxr n shapgvba jvgu n qrsvavgr tbny,
Lbhe tnmr yrnqf gur qverpgvba bs zl urneg.
Va ybir, V frrx ybtvp,
Naq lbh ner gur zbfg ornhgvshy ehyr.
Zvfgnxrf ner ab ybatre greevslvat va sebag bs lbh,
Orpnhfr lbhe gbyrenapr vf yvxr gur cngvrapr va qrohttvat.
Whfg yvxr n ybbc, ybir arire fgbcf,
Nppbzcnalvat jvgu lbh vf zl rgreany chefhvg.
Evzv, lbh ner gur pbqr bs zl fbhy,
Pbzcvyrq jvgu ybir, arire jvgu reebef.
Znl bhe fgbel or yvxr na bcra-fbhepr cebwrpg,
Funevat ornhgl naq nyjnlf erzrzorerq.
"""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr((i+13) % 26 + c)] = chr(i+c)

print("".join([d.get(c, c) for c in s]))
