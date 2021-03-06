from django.db import models


# Create your models here.
class NaverData(models.Model):
    title = models.TextField()
    contents = models.TextField()
    keyword = models.CharField(max_length=50)
    platform = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    reg_date = models.DateTimeField()
    crawl_url = models.TextField()
    view_cnt = models.IntegerField()
    comment_cnt = models.IntegerField()
    like_cnt = models.IntegerField()

    class Meta:
        managed = True
        db_table = 't_naver_data'


class NaverBlogData(models.Model):
    title = models.TextField()
    contents = models.CharField(max_length=900)
    keyword = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    reg_date = models.DateTimeField()
    crawl_url = models.CharField(max_length=900)
    comment_cnt = models.IntegerField()
    like_cnt = models.IntegerField()

    class Meta:
        managed = True
        db_table = 't_naver_blog'


class NaverCafeData(models.Model):
    title = models.TextField()
    contents = models.CharField(max_length=900)
    keyword = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    reg_date = models.DateTimeField()
    crawl_url = models.CharField(max_length=900)
    comment_cnt = models.IntegerField()
    like_cnt = models.IntegerField()

    class Meta:
        managed = True
        db_table = 't_naver_cafe'
