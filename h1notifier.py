#!/usr/bin/python

import argparse
import requests
import json
from termcolor import colored
from config import * 
import re
from prettytable import PrettyTable
from tqdm import tqdm
import time

version = "1.0"
def banner():
    print('''
                 _     __              _   _  __ _           
                | |   /  |            | | (_)/ _(_)          
                | |__ `| | _ __   ___ | |_ _| |_ _  ___ _ __ 
                | '_ \ | || '_ \ / _ \| __| |  _| |/ _ \ '__|
                | | | || || | | | (_) | |_| | | | |  __/ |   
                |_| |_\___/_| |_|\___/ \__|_|_| |_|\___|_|   
                                                            
                                             
    ''')
    print(colored("               Author: Bour Mohamed Abdelhadi (@BourAbdelhadi)", "red" , attrs=['bold']))
    print(colored("                             Version: {}", "red" , attrs=['bold']).format(version) + "\n")

def getreports():
    type_report_filters = {
        'All': {} ,
        'Bug Bounty': {"total_awarded_amount":{"_gt":"0.00"}}  , 
        'Published': {"report":{"hacker_published":{"_eq":True}}} , 
        'Disclosed': {"report":{"disclosed_at":{"_is_null":False}}}
    }
    h1_json = {"operationName": "HacktivityPageQuery","variables":{"querystring":"","where":type_report_filters['Bug Bounty'],"orderBy":{"field":"popular","direction":"DESC"},"secureOrderBy":None,"count":20,"maxShownVoters":10},"query":"query HacktivityPageQuery($querystring: String, $orderBy: HacktivityItemOrderInput, $secureOrderBy: FiltersHacktivityItemFilterOrder, $where: FiltersHacktivityItemFilterInput, $count: Int, $cursor: String, $maxShownVoters: Int) { me {    id   __typename } hacktivity_items(first: $count, after: $cursor, query: $querystring, order_by: $orderBy, secure_order_by: $secureOrderBy, where: $where) {   total_count   ...HacktivityList   __typename }}fragment HacktivityList on HacktivityItemConnection { total_count pageInfo {   endCursor   hasNextPage   __typename } edges {   node {     ... on HacktivityItemInterface {       id       databaseId: _id       ...HacktivityItem       __typename     }     __typename   }   __typename } __typename}fragment HacktivityItem on HacktivityItemUnion { type: __typename ... on HacktivityItemInterface {   id   votes {     total_count     __typename   }   voters: votes(last: $maxShownVoters) {     edges {       node {         id         user {           id           username           __typename         }         __typename       }       __typename     }     __typename   }   upvoted: upvoted_by_current_user   __typename } ... on Undisclosed {   id   ...HacktivityItemUndisclosed   __typename } ... on Disclosed {   id   ...HacktivityItemDisclosed   __typename } ... on HackerPublished {   id   ...HacktivityItemHackerPublished   __typename }}fragment HacktivityItemUndisclosed on Undisclosed { id reporter {   id   username   ...UserLinkWithMiniProfile   __typename } team {   handle   name   medium_profile_picture: profile_picture(size: medium)   url   id   ...TeamLinkWithMiniProfile   __typename } latest_disclosable_action latest_disclosable_activity_at requires_view_privilege total_awarded_amount currency __typename}fragment TeamLinkWithMiniProfile on Team { id handle name __typename}fragment UserLinkWithMiniProfile on User { id username __typename}fragment HacktivityItemDisclosed on Disclosed { id reporter {   id   username   ...UserLinkWithMiniProfile   __typename } team {   handle   name   medium_profile_picture: profile_picture(size: medium)   url   id   ...TeamLinkWithMiniProfile   __typename } report {   id   title   substate   url   __typename } latest_disclosable_action latest_disclosable_activity_at total_awarded_amount severity_rating currency __typename}fragment HacktivityItemHackerPublished on HackerPublished { id reporter {   id   username   ...UserLinkWithMiniProfile   __typename } team {   id   handle   name   medium_profile_picture: profile_picture(size: medium)   url   ...TeamLinkWithMiniProfile   __typename } report {   id   url   title   substate   __typename } latest_disclosable_activity_at severity_rating __typename}" }
    print(h1_json)
    response = requests.post(h1_url, headers=h1_header, cookies=h1_cookie, json=h1_json)
    data = response.json()
    edges = data['data']['hacktivity_items']['edges']
    t = PrettyTable([colored("Report Title" , "green" , attrs=['bold']), 
                    colored("Reporter" , "green" , attrs=['bold']), 
                    colored("Reported To" , "green" , attrs=['bold']), 
                    colored("Report URL" , "green" , attrs=['bold']), 
                    colored("Report Type" , "green" , attrs=['bold']), 
                    colored("Report Substate" , "green" , attrs=['bold']), 
                    colored("Severity" , "green" , attrs=['bold']), 
                    colored("Reward" , "green" , attrs=['bold'])])
    # hacktivity = {}
    list_hacktivity = []
    for i in tqdm(edges):
        time.sleep(0.10)
        # Reporter infos
        report_type = i['node']['type'] # Disclosed or Undisclosed
        reporter = i['node']['reporter']['username'] # Reporter Username
        reporter_type = i['node']['reporter']['__typename'] # Reporter Type

        # Company infos
        team_name = i['node']['team']['name'] # Company name 
        team_handle = i['node']['team']['handle'] # company handel name
        team_url = i['node']['team']['url'] # Company url on h1
        team_type = i['node']['team']['__typename'] # Team type

        # Report details
        if 'report' in  i['node']:
            if 'title' in i['node']['report']:
                report_title =  i['node']['report']['title'] # Report title
                report_substate =  i['node']['report']['substate'] # Report substate (resolved , unresolved)
                report_url =  i['node']['report']['url'] # Report Url
                report_type = i['node']['report']['__typename'] # Report type
                
        
        # more details about the report
        if 'latest_disclosable_action' in i['node']:
            latest_disclosable_action = i['node']['latest_disclosable_action'].replace("Activities::", "")
            latest_disclosable_action_with_space = re.sub(r"(\w)([A-Z])", r"\1 \2", latest_disclosable_action)
            latest_disclosable_activity_at = i['node']['latest_disclosable_activity_at']
            total_awarded_amount = i['node']['total_awarded_amount']
            if total_awarded_amount is not None:
                total_awarded_amount = colored(total_awarded_amount , "green" , attrs=['bold'])
            currency = i['node']['currency']
            if 'severity_rating' in i['node']:
                severity_rating = i['node']['severity_rating']
                if 'high' == severity_rating:
                    severity_rating = colored(severity_rating , "red")
                if 'low' == severity_rating:
                    severity_rating = colored(severity_rating , "blue" , attrs=['bold'])
                if 'medium' == severity_rating:
                    severity_rating = colored(severity_rating , "yellow" , attrs=['bold'])
                if 'critical' == severity_rating:
                    severity_rating = colored(severity_rating , "red" , attrs=['bold'])
            t.add_row([report_title, reporter , team_name, report_url, report_type, report_substate, severity_rating, total_awarded_amount])
    print(t)

           
if __name__ == "__main__":
    banner()
    getreports()