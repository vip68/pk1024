#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
博客：
    http://v88v.cnblogs.com

简介：
    破解1024程序员大赛试题

    每次提交都会获取10道题，提交5次就可以把所有试题都获取到
    题型有五种，1、2、3单选多选判断，4简答，5图形，但最终只考到单选题

"""

import os
import sys
import time
import json
import pandas as pd
from bs4 import BeautifulSoup

sys.path.append(os.path.normpath(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from pk1024.api import PK1024Api


def get_html(uid, password):
    """
    获取页面
    """
    api = PK1024Api()
    api.login_exam(uid, password)

    api.post_user_mes()

    html = api.get_formal2()

    return html.text


def get_user_id(soup):
    """
    获取用户ID
    """
    soup_data = filter(lambda x: x.attrs['name'] == 'user_id', soup.find(attrs={'class': 'btns_wrap'}).select('input'))
    user_id = list(soup_data)[0].attrs['value']

    return user_id


def get_exam_data(questions):
    """
    获取试题
    """
    data_list = []
    try:
        data_list = list(map(lambda x: {
            'question_id': x.attrs['data-question-id'],
            'question_type': x.attrs['data-question-type'],
            'title': x.find(attrs={'class': 'option_tit'}).text.strip(),
            'answer': list(map(lambda y: {
                'ans_id': y.select_one('input').attrs['value'],
                'text': y.find(attrs={'class': '_quiz_leaf_tit'}).text.strip(),
            }, x.find_all(attrs={'class': 'quiz_dartq_item'}))),
        }, questions))

    except Exception as e:
        print(e)

    finally:
        return data_list


def make_excel_id():
    """
    题目+id
    :return: 
    """
    answer_id_list = list(map(lambda x: x['answer'], exam_list))
    df_id_answer = pd.DataFrame(answer_id_list)

    df_id_ret = pd.merge(df_title, df_id_answer, on=df_title.index)
    df_id_ret.rename(columns=dict(question_id='题目ID', question_type='题型(1、2、3单选多选判断，4简答)', title='题目'), inplace=True)

    df_id_ret.to_excel(writer, sheet_name='题目带ID', index=False)


def make_excel():
    """
    题目
    :return: 
    """
    answer_list = list(map(lambda x: list(map(lambda y: y['text'], x['answer'])), exam_list))
    df_answer = pd.DataFrame(answer_list)

    df_ret = pd.merge(df_title, df_answer, on=df_title.index)
    df_ret.rename(columns=dict(question_id='题目ID', question_type='题型(1、2、3单选多选判断，4简答)', title='题目'), inplace=True)

    df_ret.to_excel(writer, sheet_name='题目', index=False)


if __name__ == '__main__':
    # 1+手机号后四位数
    uid = '13333'
    # 手机号
    pwd = '13333333333'
    html_text = get_html(uid, pwd)

    html_soup = BeautifulSoup(html_text, 'html.parser')

    user_id = get_user_id(html_soup)
    print(f'用户ID：{user_id}')

    soup_data = html_soup.find_all(attrs={'class': 'question _quiz_node _quiz_question question'})
    exam_list = get_exam_data(soup_data)

    if not os.path.exists('data'):
        os.makedirs('data')

    with open(f'data/exam_{user_id}_{int(time.time())}.json', 'w') as f:
        json.dump(exam_list, f, ensure_ascii=False)

    xlsx_path = f'data/exam_{user_id}_{int(time.time())}.xlsx'
    writer = pd.ExcelWriter(xlsx_path)
    df_all = pd.DataFrame(exam_list)
    df_title = df_all[['question_id', 'question_type', 'title']]

    make_excel()
    make_excel_id()

    writer.save()
