import csv
import os
from ujson import loads
from json import dumps
from dateutil.parser import parse
    
def read_csv_file(filep):
    ret = csv.reader(open(filep,'rU'), delimiter=',')
    return ret


def parse_lender_csv_data(data):
    ret = {}
    for rec in data:
        ## there are problems with the data. This if statement is a conservative estimate for the lenders 
        if len(rec) == 6:
            ret[rec[0]] = {'id':rec[0],'country':rec[1],'city':rec[2],'prof':rec[3], 'can':rec[4], 'date=':rec[5] }
    return ret

def parse_teams_csv_data(reader):
    ret = {}
    for rec in reader:
        ## there are problems with the data. This if statement is a conservative estimate for the lenders 
        l = len(rec)
        ret[rec[0]] = {'id':rec[0],'name':rec[2] ,'loc':rec[4],'theme':rec[3], 'desc':rec[5:l-3], 'date=':rec[1], 'memb_count':rec[l-3], 'loan_count':rec[l-2], 'loan_amt':rec[l-1], 'misc':rec[l-3:l] }
    return ret

def get_till_month(date):
    print date
    date  = parse(date).replace(day=1,minute=0,second=0,tzinfo=None)
    return date
def get_timeline_csv_data(reader):
    ret ={}
    for rec in reader:
        if rec[2] in ret:
            print rec
            ret[get_till_month(rec[2])] += 1# {'id':rec[0],'name':rec[2] ,'loc':rec[4],'theme':rec[3], 'desc':rec[5:l-3], 'date=':rec[1], 'memb_count':rec[l-3], 'loan_count':rec[l-2], 'loan_amt':rec[l-1], 'misc':rec[l-3:l] }
        else:
            ret[rec[2]]=1
    return ret

def team_joins_reader(reader):
    ret = []
    for rec in reader:
        ret.append((rec[0],rec[1],rec[2])) 
    return ret

def writeJsonToFile(fpath,json):
    if not os.path.isfile(fpath):
        f= open(fpath,'wb')
        f.write(dumps(json))
        f.close()
    else:
        print 'file already exists: '+ fpath
        
def get_lender_joins(team_joins):
    ret = {}
    for item in team_joins:
        if item[0] not in ret:
            ret[item[0]] = []
        ret[item[0]].append({'team_id': item[1], 'date': item[2]})
    return ret

def get_teams_memberships(team_joins):
    ret = {}
    for item in team_joins:
        if item[1] not in ret:
            ret[item[1]] = []
        ret[item[1]].append({'lender_id': item[0], 'date': item[2]})
    return ret

'''
lj is the lender joins dictionary
tm is the team_memberships dictionary 
'''
def create_csv(lj, tm, filep):
    writer = csv.writer(open(filep,'wb'))
    l_count = 0
    matrix = []
    for l in lj:
#        rec= []
#        rec.append(l.replace('l_',''))
        #arr = [0]# array of 0s
#        tm_ids = [join_info['team_id'] for join_info in lj[l]]
        for ji in lj[l]:
            # write rec to the csv file

#            writer.writerow([l.replace('l_',''),ji['team_id'].replace('t_','')])
            writer.writerow([l,ji['team_id']])
        l_count+=1
        if l_count%1000==0:
            print str(l_count) + '/' + str(len(lj))
    return matrix
