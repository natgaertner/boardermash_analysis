import csv
import sys,os
from mash_calc import calc_rating

def run(mash_file_name, scores_file_name):
    with open(mash_file_name) as mash_file, open(os.path.join('scores',scores_file_name),'w') as scores_file:
        mashes = csv.DictReader(mash_file)
        scores = csv.DictWriter(scores_file, ['name','score','rank'])
        scores_dict = {}
        for x,row in enumerate(mashes):
            winner_name = row['winner_name']
            loser_name = row['loser_name']
            old_winner_score = scores_dict.get(winner_name,100)
            old_loser_score = scores_dict.get(loser_name,100)
            new_winner_score, new_loser_score = calc_rating(old_winner_score, old_loser_score)
            scores_dict[winner_name] = new_winner_score
            scores_dict[loser_name] = new_loser_score
            if x % 1000 == 999:
                print x
        
        for rank,(name,score) in enumerate(sorted(scores_dict.items(),key=lambda (name,score):-score)):
            scores.writerow({'name':name,'score':score,'rank':rank})

if __name__ == '__main__':
    mash_file_name = sys.argv[1]
    scores_file_name = sys.argv[2]
    run(mash_file_name, scores_file_name)
