import codecs
import re

path = r'E:\まいてつ Last Run!!\vn_patch\scnlist_tw_1.tjs'
with codecs.open(path, 'r', 'utf-16le', errors='ignore') as f:
    text = f.read()

# The pattern is: => Nagi...\",
# We want to replace => Nagi with => "Nagi
def replacer(match):
    return '=> "' + match.group(1) + '",'

new_text = re.sub(r'=>\s*([^"\s][^"]*)",', replacer, text)

with codecs.open(path, 'w', 'utf-16le') as f:
    f.write(new_text)

print('Fixed missing quotes in scnlist_tw_1.tjs')
