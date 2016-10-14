from scrapy.conf import settings
import pymongo

class NovelspiderPipeline(object):
	def _init_(self):
		host=settings['MONGODB_HOST']
		post=settings['MONGODB_PORT']
		dbName=settings['MONGODB_DBNAME']
		client=pymongo.MONGODBClient(host=host,port=port)
		tdb=client[dbName]
		self.post=tdb[settings['MONGODB_DOCNAME']]


	def process_item(self,item,spider):
		bookInfo=dict(item)
		self.post.insert(bookInfo)
		return item