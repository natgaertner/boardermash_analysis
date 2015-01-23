import csv,os
from collections import defaultdict
import sys

def run(mash_file_name,scores_file_name):
    with open(mash_file_name) as mash_file, open(os.path.join('scores',scores_file_name),'w') as win_loss_file:
        mashes = csv.DictReader(mash_file)
        win_loss = csv.DictWriter(win_loss_file,['name','wins','losses','percent','rank'])
        win_loss.writeheader()
        player_dict = defaultdict(lambda:{'w':0,'l':0},{})
        for row in mashes:
            player_dict[row['winner_name']]['w']+=1
            player_dict[row['loser_name']]['l']+=1
        win_loss_rows = [{'name':player,'wins':wl['w'],'losses':wl['l'],'percent':float(wl['w'])/float(wl['l']+wl['w'])} for player,wl in player_dict.iteritems() if player not in ['pop zeus','stupid ass']]
        win_loss_rows.sort(key=lambda row:-row['percent'])
        for rank,row in enumerate(win_loss_rows):
            win_loss.writerow(dict([('rank',rank+1)]+row.items()))

if __name__=='__main__':
    run(sys.argv[1],sys.argv[2])
