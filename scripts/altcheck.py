import re, sys, glob, os
# The two sets, read straight out of the stylesheet so the audit can't
# drift from the rule it is auditing.
css = open('assets/css/custom.css').read()
def names(block):
    m = re.search(block, css, re.S)
    return set(re.findall(r'\.section_[a-z_]+|\.section-alt', m.group(1)))
alt  = names(r'(body\.oss \.section_hero,.*?)\{ background: var\(--paper-2\)')
dark = names(r'(body\.oss \.section_hero_dark,.*?)\{ background: var\(--plum\)')
bad = 0
for f in sorted(glob.glob('docs/**/index.html', recursive=True)):
    page = '/' + os.path.dirname(f).replace('docs','',1).strip('/') + '/'
    seq = []
    for cls in re.findall(r'<section[^>]*class="([^"]*section[^"]*)"', open(f).read()):
        c = set('.'+x for x in cls.split())
        if c & dark:  seq.append(('D', cls))
        elif c & alt: seq.append(('2', cls))
        elif '.section' in c: seq.append(('P', cls))
    letters = ''.join(s for s, _ in seq)
    runs = [(i, seq[i][1]) for i in range(1, len(seq))
            if seq[i][0] == seq[i-1][0] and seq[i][0] != 'D']
    flag = ''
    if runs:
        bad += 1
        flag = '   <-- repeats: ' + ', '.join(c.replace('section ','') for _, c in runs)
    print('%-22s %s%s' % (page, letters, flag))
print('\n%d page(s) with a repeated band' % bad)
