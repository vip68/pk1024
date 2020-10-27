#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
博客：
    http://v88v.cnblogs.com

简介：
    POST方式提交答卷

"""

import json
import requests.utils

sess = requests.session()
headers = {
    "Host": "1024.baby-bus.com",
    "Cache-Control": "max-age=0",
    "Origin": "http://1024.baby-bus.com",
    "Upgrade-Insecure-Requests": "1",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/77.0.3865.120 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;"
              "q=0.8,application/signed-exchange;v=b3",
    "Referer": "http://1024.baby-bus.com/index.php/Home/Index/formal2",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,da;q=0.7",
    # "Cookie": "PHPSESSID=fq5doloepdlejvkq3icdq9c9p0",
    "Connection": "keep-alive",
}

cookies_dict = {
    "PHPSESSID": "pqal1470anocrueteik93mtia5"
}

requests.utils.add_dict_to_cookiejar(sess.cookies, cookies_dict)

url = 'http://1024.baby-bus.com/index.php/Home/Index/submit.html'

data = [
    {"id": "1701", "answer_id": "5102"}, {"id": "1702", "answer_id": "5105"}, {"id": "1703", "answer_id": "5108"},
    {"id": "1704", "answer_id": "5111"}, {"id": "1705", "answer_id": "5114"}, {"id": "1706", "answer_id": "5117"},
    {"id": "1707", "answer_id": "5120"}, {"id": "1708", "answer_id": "5123"}, {"id": "1709", "answer_id": "5126"},
    {"id": "1710", "answer_id": "5129"}, {"id": "1711", "answer_id": "5132"}, {"id": "1712", "answer_id": "5135"},
    {"id": "1713", "answer_id": "5138"}, {"id": "1714", "answer_id": "5141"}, {"id": "1715", "answer_id": "5144"},
    {"id": "1716", "answer_id": "5147"}, {"id": "1717", "answer_id": "5150"}, {"id": "1718", "answer_id": "5153"},
    {"id": "1719", "answer_id": "5156"}, {"id": "1720", "answer_id": "5159"}, {"id": "1721", "answer_id": "5162"},
    {"id": "1722", "answer_id": "5165"}, {"id": "1723", "answer_id": "5168"}, {"id": "1724", "answer_id": "5171"},
    {"id": "1725", "answer_id": "5174"}, {"id": "1726", "answer_id": "5177"}, {"id": "1727", "answer_id": "5180"},
    {"id": "1728", "answer_id": "5183"}, {"id": "1729", "answer_id": "5186"}, {"id": "1730", "answer_id": "5189"},
    {"id": "1731", "answer_id": "5192"}, {"id": "1732", "answer_id": "5195"}, {"id": "1733", "answer_id": "5198"},
    {"id": "1734", "answer_id": "5201"}, {"id": "1735", "answer_id": "5204"}, {"id": "1736", "answer_id": "5207"},
    {"id": "1737", "answer_id": "5210"}, {"id": "1738", "answer_id": "5213"}, {"id": "1739", "answer_id": "5216"},
    {"id": "1740", "answer_id": "5219"}, {"id": "1741", "answer_id": "5222"}, {"id": "1742", "answer_id": "5225"},
    {"id": "1743", "answer_id": "5228"}, {"id": "1744", "answer_id": "5231"}, {"id": "1745", "answer_id": "5234"},
    {"id": "1746", "answer_id": "5237"}, {"id": "1747", "answer_id": "5240"}, {"id": "1748", "answer_id": "5243"},
    {"id": "1749", "answer_id": "5246"}, {"id": "1750", "answer_id": "5249"}, {"id": "1751", "answer_id": "5252"},
    {"id": "1752", "answer_id": "5255"}, {"id": "1753", "answer_id": "5258"}, {"id": "1754", "answer_id": "5261"},
    {"id": "1755", "answer_id": "5264"}, {"id": "1756", "answer_id": "5267"}, {"id": "1757", "answer_id": "5270"},
    {"id": "1758", "answer_id": "5273"}, {"id": "1759", "answer_id": "5276"}, {"id": "1760", "answer_id": "5279"},
    {"id": "1761", "answer_id": "5282"}, {"id": "1762", "answer_id": "5285"}, {"id": "1763", "answer_id": "5288"},
    {"id": "1764", "answer_id": "5291"}, {"id": "1765", "answer_id": "5294"}, {"id": "1766", "answer_id": "5297"},
    {"id": "1767", "answer_id": "5300"}, {"id": "1768", "answer_id": "5303"}, {"id": "1769", "answer_id": "5306"},
    {"id": "1770", "answer_id": "5309"}, {"id": "1771", "answer_id": "5312"}, {"id": "1772", "answer_id": "5315"},
    {"id": "1773", "answer_id": "5318"}, {"id": "1774", "answer_id": "5321"}, {"id": "1775", "answer_id": "5324"},
    {"id": "1776", "answer_id": "5327"}, {"id": "1777", "answer_id": "5330"}, {"id": "1778", "answer_id": "5333"},
    {"id": "1779", "answer_id": "5336"}, {"id": "1780", "answer_id": "5339"}, {"id": "1781", "answer_id": "5342"},
    {"id": "1782", "answer_id": "5345"}, {"id": "1783", "answer_id": "5348"}, {"id": "1784", "answer_id": "5351"},
    {"id": "1785", "answer_id": "5354"}, {"id": "1786", "answer_id": "5357"}, {"id": "1787", "answer_id": "5360"},
    {"id": "1788", "answer_id": "5363"}, {"id": "1789", "answer_id": "5366"}, {"id": "1790", "answer_id": "5369"},
    {"id": "1791", "answer_id": "5372"}, {"id": "1792", "answer_id": "5375"}, {"id": "1793", "answer_id": "5378"},
    {"id": "1794", "answer_id": "5381"}, {"id": "1795", "answer_id": "5384"}, {"id": "1796", "answer_id": "5387"},
    {"id": "1797", "answer_id": "5390"}, {"id": "1798", "answer_id": "5393"}, {"id": "1799", "answer_id": "5396"},
    {"id": "1800", "answer_id": "5399"}
]

post_data = {
    'answer_list': json.dumps(data),
    'user_id': "120",
    'remaining_time': '00:40:10',
    'breakoff_num': "1"
}

resp = sess.post(url, headers=headers, data=post_data, verify=False)
print(resp)
