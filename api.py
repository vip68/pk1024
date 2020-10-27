import requests
import requests.utils


class PK1024Api(object):
    """1024比赛"""

    def __init__(self):
        self.sess = requests.session()

    def login_first(self, uid, password):
        """
        登录首页（用不着）
        """
        headers = {
            'Host': '1024.baby-bus.com',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://1024.baby-bus.com',
            'Referer': 'http://1024.baby-bus.com/index.php/Index/Index/index.html',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,da;q=0.7',
        }

        url = 'http://1024.baby-bus.com/index.php/Index/Index/doLogin.html'
        data = {
            'id': uid,
            'password': password,
        }

        resp = self.sess.post(url=url, headers=headers, data=data).json()

        return resp

    def login_exam(self, uid, email):
        """
        登录考试
        """
        headers = {
            'Host': '1024aq.baby-bus.com',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.111 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://1024aq.baby-bus.com',
            'Referer': f'http://1024aq.baby-bus.com/index.php/Home/Index/index.html?id={uid}&email={email}',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,da;q=0.7',
        }
        url = 'http://1024aq.baby-bus.com/index.php/Home/User/login.html'
        data = {
            'id': uid,
            'email': email,
        }

        resp = self.sess.post(url=url, headers=headers, data=data).json()

        return resp

    def post_user_mes(self):
        """
        提交用户信息
        :return:
        """
        headers = {
            'Host': '1024aq.baby-bus.com',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://1024aq.baby-bus.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.111 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                      'q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://1024aq.baby-bus.com/index.php/Home/Index/user_mes.html',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,da;q=0.7',
        }
        # 要把这个信息改为自己的
        data = {
            "Name": "匿名",
            "Sex": "1",
            "birthday": "2000-01-01",
            "Polity": "团员",
            "AreaCategory_txt": "福建省",
            "AreaCategory": "3400",
            "Tel": "",
            "University": "中央广播电视大学",
            "Professional": "计算机科学与技术",
            "IndustryCategory_txt": "",
            "IndustryCategory": "9",
            "Jobs": "",
            "Department": "",
            # 这个ID应该是固定不变的
            "FK_BeisenUser_ID": "114895095",
        }

        url = 'http://1024aq.baby-bus.com/index.php/Home/Index/user_mes_submit'

        resp = self.sess.post(url=url, headers=headers, data=data)

        return resp

    def pre_read(self):
        """
        这个用不到
        :return:
        """
        headers = {
            'Host': '1024aq.baby-bus.com',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.111 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                      'q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://1024aq.baby-bus.com/index.php/Home/Index/user_mes.html',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,da;q=0.7',
        }
        url = 'http://1024aq.baby-bus.com/index.php/Home/Index/pre_read.html'

        resp = self.sess.get(url=url, headers=headers)

        return resp

    def get_formal2(self):
        """
        获取答题页面
        """
        headers = {
            'Host': '1024aq.baby-bus.com',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.111 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                      'q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,da;q=0.7',
        }

        url = 'http://1024aq.baby-bus.com/index.php/Home/Index/formal2'

        resp = self.sess.get(url=url, headers=headers)

        return resp
