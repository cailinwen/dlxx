from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from users.views import login_check
from feat_manager.settings import featDB_config
from dimzou.models import DimZou_article_BaseFields, Users_BaseFields
import pymysql
PAGE_COUNT = 20


@login_check
def translationindex(request):
    return render(request,'translation/list.html')

@login_check
def textlist(request,statusType = 0,taxonomyId = 1):
    connection = pymysql.connect(**featDB_config)
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM cel_profile_art WHERE is_audit = 1 and is_del = 0 and status = 2'
            passCount = cursor.execute(sql)
            sql = 'SELECT * FROM cel_profile_art WHERE is_audit in (0,3) and is_del = 0 and status = 2'
            pendingCount = cursor.execute(sql)
            sql = 'SELECT * FROM cel_profile_art WHERE is_audit = 2 and is_del = 0 and status = 2'
            vetoCount = cursor.execute(sql)
            
            sql = 'SELECT '+DimZou_article_BaseFields+Users_BaseFields+' FROM feat_celestra.cel_profile_art LEFT JOIN feat_celestra.user ON (feat_celestra.cel_profile_art.author = feat_celestra.user.user_id) WHERE is_audit in (0,3) and is_del = 0 and status = 2'
            auditList_count = cursor.execute(sql)
            print auditList_count
            auditList_result = cursor.fetchall()
            
            sql = sql = 'SELECT * FROM ft_dz_category WHERE status != 0'
            cursor.execute(sql)
            sort = cursor.fetchall()
    except:
        #raise "Data Error"
        pass
    finally:
        connection.close()
    
    title = ' | Audit'
    
    if auditList_count > PAGE_COUNT:
        pageEndArticle = auditList_result.pop()
        pageEndArtId = pageEndArticle['art_id']
    else:
        pageEndArtId = 0
    
    '''hasmore init'''
    if auditList_count > PAGE_COUNT:
        hasMore = 'true'
    else:
        hasMore = 'false'
    
    '''offset init'''
    if auditList_count > PAGE_COUNT:
        offset = auditList_count - 1
    else:
        offset = auditList_count 
        
    statusType = 0
    return render(request,'translation/list.html',{'statusType':statusType,
                'auditList':auditList_result,'passCount':passCount,'pendingCount':pendingCount,
                'vetoCount':vetoCount,'offset':offset,'hasmore':hasMore,'pageEndArtId':pageEndArtId,
                'title':title,'sort':sort})