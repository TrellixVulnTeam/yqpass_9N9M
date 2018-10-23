# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-16 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customfield',
            name='field_type_id',
            field=models.IntegerField(help_text='5.字符串、10.整形、15.浮点型、20.布尔、25.日期、30.日期时间、35.单选框、40.多选框、45.下拉列表、50.多选下拉列表、55.文本域、60.用户名、70.多选的用户名', verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='customfield',
            name='order_id',
            field=models.IntegerField(default=0, help_text='工单基础字段在表单中排序为:流水号0、标题20、状态id40、状态名41、创建人80、创建时间100、更新时间120、前端展示工单信息的表单可以根据这个id顺序排列', verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='state',
            name='is_hidden',
            field=models.BooleanField(default=False, help_text='设置为True时,获取工单处理步骤信息中不显示此状态(当前处于此状态时除外)', verbose_name='是否隐藏'),
        ),
        migrations.AlterField(
            model_name='state',
            name='participant',
            field=models.CharField(blank=True, default='', help_text='可以为空(无处理人的情况，如结束状态)、username\\多个username(以,隔开)                                   部门id\\角色id\\变量(creator,creator_tl)\\脚本文件名(不包含上传后的路径)等，包含子工作流的需要设置处理人为robot', max_length=100, verbose_name='参与者'),
        ),
        migrations.AlterField(
            model_name='state',
            name='participant_type_id',
            field=models.IntegerField(blank=True, default=1, help_text='0.无处理人、1.个人、2.多人、3.部门、4.角色、5.变量(工单创建人,创建人的leader)、6.脚本、7.工单的字段内容、8.父工单的字段内容', verbose_name='参与者类型id'),
        ),
        migrations.AlterField(
            model_name='state',
            name='state_field_str',
            field=models.TextField(default='{}', help_text="json格式,包括读写属性1：只读，2：必填，3：可选. 示例：{'created_at':1,'title':2, 'sn':1} 内置特殊字段：participant_info.participant_name:当前处理人信息(部门名称、角色名称)，state.state_name:当前状态的状态名,workflow.workflow_name:工作流名称", verbose_name='表单字段'),
        ),
        migrations.AlterField(
            model_name='workflow',
            name='display_form_str',
            field=models.CharField(blank=True, default='[]', help_text="默认'[]',用户只有工单查看权限时显示的字段，field_key的list如 ['days','sn'],内置特殊字段： participant_info.participant_name:当前处理人信息(部门名称、角色名称), state.state_name：当前状态的状态名workflow.workflow_name:工作流名称", max_length=10000, verbose_name='展现表单字段'),
        ),
    ]