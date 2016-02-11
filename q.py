__author__ = 'ffpku_000'

from GameOn.main import *
import pandas as pd
os.chdir('C:/Users/ffpku_000/Documents/Research_Genome/Data/gameon/')

x = pd.read_table('task.txt', ' ', header=None)

def find_n(chr=None, start=None, end=None):
    d = simple_load(chr=chr, start=start, end=end)
    time.sleep(1)
    html = etree.HTML(d.page_source)
    ij = html.xpath('//*[@id="l_edu_dfci_cccb_gameon_domain_Snp_info"]')[0].text
    d.close()
    return int(re.sub(',', '', re.split(' ', ij)[5]))

print find_n()

n = [find_n(i) for i in range(1, 23)]
print 'data by chr: \n', n, '\n', sum(n)

m = [find_n(x.loc[i][2], x.loc[i][3], x.loc[i][4]) for i in range(0, 64)]
print 'data by task: \n', m, '\n', sum(m)

print sum(x.loc[:, 5])

for i in range(0, 64):
    print m[i], x.loc[i, 5]

print all(m == x.loc[:, 5]) # True

for i in range(0, 22):
    print n[i], sum(m[x.loc[:, 2] == i+1]), sum(x.loc[x.loc[:, 2] == i+1, 5])



df = pd.read_table('GameOnData.txt', ' ', header=None)
print df.shape # total 2543887 lines, 2521687 are not None

print sum(df[0].duplicated()) # 0
print df.loc[df[0].duplicated(), 0] # None

