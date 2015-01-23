import csv
import sys,os
from mash_calc import calc_rating

def run():
    with open(os.path.join('data','all_mashes.csv')) as mash_file, open(os.path.join('data','ip_counts.csv')) as ip_file:
        ip_comparison_dicts = dict(generate_comparisons(ip_file))
        ip_original_dicts = {}
        for ip_id,comparison_dict in ip_comparison_dicts.iteritems():
            ip_original_dicts[ip_id] = dict(comparison_dict.iteritems())
        mashes = csv.DictReader(mash_file)
        for x,row in enumerate(mashes):
            winner_name = row['winner_name']
            loser_name = row['loser_name']
            ip_id = row['ip_id']
            comparison_winner_score = ip_comparison_dicts[ip_id][winner_name]
            comparison_loser_score = ip_comparison_dicts[ip_id][loser_name]
            new_winner_score, new_loser_score = calc_rating(comparison_winner_score, comparison_loser_score)
            ip_comparison_dicts[ip_id][winner_name] = new_winner_score
            ip_comparison_dicts[ip_id][loser_name] = new_loser_score
            if x % 1000 == 999:
                print x
    with open(os.path.join('scores','ip_diffs.csv'),'w') as ip_diffs_file, open(os.path.join('data','ip_counts.csv')) as ip_counts_file:
        ip_diffs = csv.DictWriter(ip_diffs_file,['ip_id','count','median','average'])
        ip_diffs.writeheader()
        ip_diffs_rows = []
        ip_counts = dict((row['ip_id'],row['count']) for row in csv.DictReader(ip_counts_file))
        for ip_id in ip_comparison_dicts.keys():
            comparison_scores_dict = ip_comparison_dicts[ip_id]
            original_scores_dict = ip_original_dicts[ip_id]
            with open(os.path.join('scores','comparisons','{ip_id}_comparisons.csv'.format(ip_id=ip_id)),'w') as scores_file:
                scores = csv.DictWriter(scores_file, ['name','score','rank','score_diff'])
                scores.writeheader()
                for rank,(name,score) in enumerate(sorted(comparison_scores_dict.items(),key=lambda (name,score):-score)):
                    score_diff = score-original_scores_dict[name]
                    scores.writerow({'name':name,'score':score,'rank':rank+1,'score_diff':score_diff})
                score_diff = [abs(comparison_scores_dict[name]-original_scores_dict[name]) for name in comparison_scores_dict.keys()]
                ip_diffs_rows.append({'ip_id':ip_id,'count':ip_counts[ip_id],'median':median(score_diff),'average':sum(score_diff)/len(score_diff)})
        ip_diffs_rows.sort(key=lambda row:-row['median'])
        ip_diffs_rows.sort(key=lambda row:-row['average'])
        for row in ip_diffs_rows:
            ip_diffs.writerow(row)

def generate_comparisons(ip_file):
    ips = csv.DictReader(ip_file)
    for row in ips:
        ip_id = row['ip_id']
        with open(os.path.join('scores_excluding','{ip_id}.csv'.format(ip_id=ip_id))) as ip_comparison_file:
            ip_comparison = csv.reader(ip_comparison_file)
            yield ip_id,dict((row[0],float(row[1])) for row in ip_comparison)

def median(l):
    if len(l) % 2 == 0:
        return (l[len(l)/2] + l[len(l)/2+1])/2.
    else:
        return l[len(l)/2]

if __name__ == '__main__':
    run()
