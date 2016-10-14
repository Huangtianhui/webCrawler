
BOT_NAME='novelspider'

SPIDER_MODULES=['novelspider.spiders']
NEWSPIDER_MODULE='novelspider.spiders'

#path setting
ITEM_PIPELINES=['novelspider.pipelines.NovelspiderPipeline']

#USER_AGENT=''
COOKIES_ENABLED=True

MONGODB_HOST='127.0.0.1'
MONGODB_PORT=27017
MONGODB_DBNAME='MongoProject'
MONGODB_DOCNAME='Book'
