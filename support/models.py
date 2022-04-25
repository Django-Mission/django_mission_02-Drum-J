from unicodedata import category
from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class FAQ(models.Model) :
    qus = models.TextField(verbose_name='질문')
    일반 = '0'
    계정 = '1'
    기타 ='2'
    Category_choices = [
        (일반,'일반'),
        (계정,'계정'),
        (기타,'기타'),
    ]
    category = models.CharField(
        max_length=2,
        choices=Category_choices,
        default=일반
    )

    ans = models.TextField(verbose_name='답변')
    writer = models.ForeignKey(verbose_name='작성자',to=User, on_delete=models.CASCADE, null=True, blank=True,related_name='writer_FAQ')
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    writer2 = models.ForeignKey(verbose_name='최종 수정자',to=User, on_delete=models.CASCADE, null=True, blank=True,related_name='writer2_FAQ')
    modify_date = models.DateTimeField(verbose_name='최종 수정일시',auto_now=True,null=True, blank=True)