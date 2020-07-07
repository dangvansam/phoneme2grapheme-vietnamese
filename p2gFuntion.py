import os, json
from collections import defaultdict
def load_p2g():
    p2g = defaultdict(list)
    with open('simple_p2g.json','r') as f:
        p2g = json.load(f)
    #print(p2g)
    return p2g

def p2g_simple(text):
	
    p2g = load_p2g()
    text = text.replace(' ','_<sp>_').split('_')
    gtext = []
    #vowel = ['i','is','i']
    for i,p in enumerate(text):
        if p == '<sp>':
            gtext.append('<sp>')
        elif p == '':
            continue
        else:
            gs = p2g[p]
            g = ''
            #print(gs)
            if len(gs) == 1:
                g = gs[0]
            else:
                #print('len > 1')
                if p in ['g','ng','c']:
                    #print(p)
                    #print('in [c g ng]')
                    if text[i-1] == '<sp>' or i == 0:
                        #print('after sp')
                        #print(text[i+1])
                        if text[i+1][0] in ['i','e']:
                            #print('in i e ee')
                            if p == 'g':
                                g = 'gh'
                            elif  p == 'ng':
                                g = 'ngh'
                            elif  p == 'c':
                                g = 'k'
                        else:
                            #print('not i e ee')
                            if p == 'g':
                                g = 'g'
                            elif  p == 'ng':
                                g = 'ng'
                            elif  p == 'c':
                                #print('ccc')
                                g = 'c'
                    else:
                        #print('not begin word')
                        if p == 'g':
                            g = 'g'
                        elif  p == 'ng':
                            g = 'ng'
                        elif  p == 'c':
                            g = 'c'
                else:
                    g = gs[0]
            gtext.append(g)
    gtext = ''.join(gtext).replace('<sp>',' ')
    return gtext

phoneme = 'dd_oof_ng ng_ieej_p t_aay b_aor nh_aj_c c_uar t_ooi ch_ir th_oas_ng ng_e'
grapheme = p2g_simple(phoneme)
print("phoneme:",phoneme)
print("grapheme:",grapheme)