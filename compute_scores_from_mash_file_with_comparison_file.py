import csv
import sys,os
from mash_calc import calc_rating

def run(mash_file_name, comparison_scores_file_name, scores_file_name):
    with open(mash_file_name) as mash_file, open(comparison_scores_file_name) as comparison_scores_file, open(os.path.join('scores',scores_file_name),'w') as scores_file:
        mashes = csv.DictReader(mash_file)
        comparison_scores = csv.reader(comparison_scores_file)
        comparison_scores.next()
        scores = csv.DictWriter(scores_file, ['name','score','rank','score_diff'])
        comparison_scores_dict = dict((row[0],float(row[1])) for row in comparison_scores)
        original_scores_dict = dict(comparison_scores_dict.iteritems())
        for x,row in enumerate(mashes):
            winner_name = row['winner_name']
            loser_name = row['loser_name']
            comparison_winner_score = comparison_scores_dict.get(winner_name,100)
            comparison_loser_score = comparison_scores_dict.get(loser_name,100)
            new_winner_score, new_loser_score = calc_rating(comparison_winner_score, comparison_loser_score)
            comparison_scores_dict[winner_name] = new_winner_score
            comparison_scores_dict[loser_name] = new_loser_score
            if x % 1000 == 999:
                print x
        scores.writeheader()
        comparison_scores_dict.pop('pop zeus')
        comparison_scores_dict.pop('stupid ass')
        for rank,(name,score) in enumerate(sorted(comparison_scores_dict.items(),key=lambda (name,score):-score)):
            score_diff = score-original_scores_dict[name]
            scores.writerow({'name':name,'score':score,'rank':rank+1,'score_diff':score_diff})

def median(l):
    if len(l) % 2 == 0:
        return (l[len(l)/2] + l[len(l)/2+1])/2.
    else:
        return l[len(l)/2]

if __name__ == '__main__':
    mash_file_name = sys.argv[1]
    comparison_scores_file_name = sys.argv[2]
    scores_file_name = sys.argv[3]
    run(mash_file_name, comparison_scores_file_name, scores_file_name)
