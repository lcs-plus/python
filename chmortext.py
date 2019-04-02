import requests
import json
import pymysql
import time


def execute(sql):
    db = pymysql.connect('106.13.95.79','larav','Tx7aXSRr3cKYypE8','larav')

    cursor = db.cursor()

    try:
        cursor.execute(sql)

        db.commit()
    except:
        db.rollback()
    db.close()


def openUrl(url):

    root = requests.get(url)

    return root.json()

i=1

keys = '`category_name`,`commission_rate`,`commission_type`,`coupon_amount`,`coupon_end_time`,`coupon_id`,`coupon_info`,`coupon_remain_count`,`coupon_share_url`,`coupon_start_fee`,`coupon_start_time`,`coupon_total_count`,`include_dxjh`,`include_mkt`,`item_description`,`item_id`,`item_url`,`level_one_category_id`,`level_one_category_name`,`nick`,`num_iid`,`pict_url`,`provcity`,`reserve_price`,`seller_id`,`shop_dsr`,`shop_title`,`short_title`,`small_images`,`title`,`tk_total_commi`,`tk_total_sales`,`url`,`user_type`,`volume`,`white_image`,`x_id`,`zk_final_price`,`create_time`'

while i < 1000000:
    page = str(i)

    url = 'http://api.tkurl.top/api/alimama/material?appkey=8SUvq9H3&page_size=100&q=女装&page_no='+page+'&has_coupon=true'

    root = openUrl(url)

    root = root['tbk_dg_material_optional_response']['result_list']['map_data']

    for x in root:
        x.pop('category_id')
        x.pop('info_dxjh')

        img = ",".join(x['small_images']['string'])

        x['small_images'] = img

        a = list(x.values())
        values = ''
        for x in a:
            values += "'" + str(x) + "',"

        t = time.time()
        t = int(t)
        values += str(t)

        sql = "INSERT INTO `tb_shop`("+keys+") VALUES("+ values+")"

        execute(sql)


