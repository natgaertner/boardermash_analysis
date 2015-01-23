import csv,os

def run():
    with open(os.path.join('data','rank.csv')) as rank_file, open(os.path.join('data','split_old_ranks.csv')) as old_rank_file, open(os.path.join('data','hipusers_sorted.csv')) as hipusers_file, open(os.path.join('data','has_av_map.csv')) as has_av_file, open(os.path.join('scores','rank_movement.csv'),'w') as rank_movement_file:
        rank = csv.DictReader(rank_file)
        old_rank = dict((row['name'],row['rank']) for row in csv.DictReader(old_rank_file))
        hipusers = dict((row['username'],row['posts']) for row in csv.DictReader(hipusers_file))
        has_av = set(row['username'] for row in csv.DictReader(has_av_file))
        rank_movement = csv.DictWriter(rank_movement_file,['name','posts','has_av','score','rank','old_rank','movement'])
        rank_movement.writeheader()
        for rank,row in enumerate(rank):
            old = old_rank.get(row['name'],'')
            new = rank+1
            if len(old) > 0:
                movement = str(int(old) - new)
            else:
                movement = 'n/a'
            rank_movement.writerow({'name':row['name'],'posts':hipusers[row['name']],'has_av':(row['name'] in has_av),'score':row['score'],'rank':row['row_number'],'movement':movement,'old_rank':old})

if __name__ == '__main__':
    run()
