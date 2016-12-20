# -*- coding: utf-8 -*-

'封装Http请求'

__author__='litterzhang'

import requests
from requests.auth import AuthBase

from sinaset import *

class SAuth(AuthBase):
	def __init__(self, ua=UserAgent, rf=Referer):
		self.ua = ua
		self.rf = rf
		pass

	def __call__(self, r):
		r.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
		r.headers['Accept-Encoding'] = 'gzip, deflate, sdch'
		r.headers['Accept-Language'] = 'zh-CN,zh;q=0.8'
		r.headers['Cache-Control'] = 'max-age=0'
		r.headers['Connection'] = 'keep-alive'
		r.headers['Referer'] = self.ua
		r.headers['Upgrade-Insecure-Requests'] = '1'
		r.headers['User-Agent'] = self.rf
		return r

class SReq:
	def __init__(self, ua=UserAgent, ss=None):
		self._auth = SAuth(ua=ua)

		if not ss:
			self._session = requests.session()
		else:
			self._session = ss

	def get(self, url, data={}):
		r = self._session.get(url, params=data, auth=self._auth)
		return r

	def post(self, url, data={}):
		r = self._session.post(url, data=data, auth=self._auth)
		return r

if __name__=='__main__':
	req = SReq()
	r = req.get('http://weibo.cn/iamamycheung')
	print(req._session.__dict__)



