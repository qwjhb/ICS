from django.db import models
import datetime

# Create your models here.
class autum(models.Model):
    name=models.CharField('客户姓名',max_length=12,primary_key=True)
    ID_card=models.CharField('身份证号',max_length=18)
    hly = models.BooleanField('活利盈',default=False)
    skb = models.BooleanField('收款宝',default=False)
    sxt = models.BooleanField('随薪通准贷记卡',default=False)
    kkt = models.BooleanField('卡卡通',default=False)
    tlkh = models.BooleanField('通联跨行归集',default=False)
    branchinfo = (
        ('0071','九沙支行'),
        ('0169','月雅路支行'),
        ('0332','朝阳支行'),
        ('0333','营业中心'),
        ('0335','德胜东路支行'),
    )
    branch = models.CharField('网点',max_length=4,choices=branchinfo)
    worker = models.CharField('受理员工',max_length=10)
    market = models.CharField('所属市场',max_length=30)
    note = models.TextField('备注')
    time=models.DateTimeField(default=datetime.datetime.now() )
    def __str__(self):
        return self.name