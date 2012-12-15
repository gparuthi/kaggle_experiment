from helpers import *

# load team joins
print  'loading team joins'
reader = read_csv_file('./team_join.csv')
team_joins=  team_joins_reader(reader)


#load  teams
print  'loading teams'
reader = read_csv_file('./teams.csv')
teams=  parse_teams_csv_data(reader)

#load lenders
print 'loading lenders'
reader = read_csv_file('./lenders.csv')
lenders=  parse_lender_csv_data(reader)

lender_joins = get_lender_joins(team_joins)
team_mem = get_teams_memberships(team_joins)
