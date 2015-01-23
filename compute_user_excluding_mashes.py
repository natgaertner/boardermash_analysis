import csv,os,time
from itertools import izip, repeat
from skills import elo
import skills
import sys

def calc_rating(winner_rating, loser_rating):
    ec = elo.EloCalculator(k_factor=1)
    return ec.new_rating(winner_rating, loser_rating, skills.WIN).mean, ec.new_rating(loser_rating, winner_rating, skills.LOSE).mean

def run(ip_counts_file_name):
    with open(os.path.join('data','all_mashes.csv')) as all_mashes_file, open(os.path.join('data',ip_counts_file_name)) as ip_counts_file:
        all_mashes = csv.DictReader(all_mashes_file)
        ip_counts = csv.DictReader(ip_counts_file)
        ip_dict = dict((row['ip_id'],{}) for row in ip_counts)
        t = time.time()
        for x,row in enumerate(all_mashes):
            for ip_id, scores_dict in ip_dict.iteritems():
                if row['ip_id'] == ip_id:
                    continue
                winner_score = scores_dict.get(row['winner_name'],100)
                loser_score = scores_dict.get(row['loser_name'],100)
                new_winner_score, new_loser_score = calc_rating(winner_score, loser_score)
                scores_dict[row['winner_name']] = new_winner_score
                scores_dict[row['loser_name']] = new_loser_score
            if x % 1000 == 999:
                print ip_counts_file_name, x, time.time() - t
                t = time.time()
        for ip_id,scores_dict in ip_dict.iteritems():
            with open(os.path.join('scores_excluding',ip_id+'.csv'),'w') as scores_excluding_file:
                scores_excluding = csv.DictWriter(scores_excluding_file, ['name','score','rank'])
                sorted_scores = [{'rank':rank+1,'name':name,'score':score} for (rank,(name,score)) in enumerate(sorted(scores_dict.items(),key=lambda (name,score):-score))]
                for row in sorted_scores:
                    scores_excluding.writerow(row)

if __name__ == '__main__':
    ip_counts_file = sys.argv[1]
    run(ip_counts_file)
