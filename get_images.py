import requests
import string
import random

from datetime import datetime

base_char = string.digits + string.ascii_letters


def get_random_string(length=32):
    return ''.join(random.choices(base_char, k=length))


cookies = {
    '_gscu_378180139': '93555901jjqqd410',
    'JSESSIONID': '66E38E207AEC81C5133095B4A5B4FC65',
    'clientlanguage': 'zh_CN',
    '_gscbrs_378180139': '1',
    '_gscs_378180139': '94423635suejtf10|pv:1',
}

headers = {
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=0C9DEE7EA2DBDF5CD9897B1C33A7C00A; _gscu_378180139=93555901jjqqd410; JSESSIONID=66E38E207AEC81C5133095B4A5B4FC65; JSESSIONID=66E38E207AEC81C5133095B4A5B4FC65; clientlanguage=zh_CN; _gscbrs_378180139=1; _gscs_378180139=94423635suejtf10|pv:1',
    'Referer': 'http://credit.linxia.gov.cn/creditWebSearch/sgs/newestSgs?methodName=sgsview.jspx&accessKey=9e1ea428efb04d4e8c8bdb491067b679&areatype=3&areacode=622900000000',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}


def get_img():
    params = {
        'd': str(int(datetime.now().timestamp() * 1000)),
    }

    response = requests.get(
        'http://credit.linxia.gov.cn/creditWebSearch/servlet/validateCodeServlet',
        params=params,
        # cookies=cookies,
        headers=headers,
        verify=False,
    )

    with open(f'train_images/linxia/_{get_random_string()}.jpg', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    for i in range(100):
        get_img()
