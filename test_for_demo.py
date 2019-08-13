#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeAccessPointsRequest import DescribeAccessPointsRequest

accessKeyId = 'LTAIgpfm3k4idVqU'
accessSecret = 'bb20ubL9Hpzb7fMbsIwe4m5xjLN3o8'
client = AcsClient(accessKeyId, accessSecret, 'cn-hangzhou')

request = DescribeAccessPointsRequest()
request.set_accept_format('json')

response = client.do_action_with_exception(request)
# python2:  print(response) 
print(str(response, encoding='utf-8'))
