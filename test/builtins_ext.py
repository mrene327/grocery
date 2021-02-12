from grocery.builtins_ext import list_ext


if __name__ == '__main__':
    test_list = list_ext([{'sender': 'testercwl4', 'subject': 'zlgCmigzrP ts:1602434126.178824', 'size': '1.9K', 'display_date': '00:35', 'date': '2020年10月12日 00:35 (星期一)'}, {'sender': 'name', 'subject': '我是一封邮件1 ts:1602432445.5496838', 'size': '1.4K', 'display_date': '00:07', 'date': '2020年10月12日 00:07 (星期一)'}, {'sender': 'mail_public_30', 'subject': '我是一封邮件1 ts:1602426498.4790692', 'size': '1.7K', 'display_date': '昨日', 'date': '2020年10月11日 22:28 (星期日)'}, {'sender': 'testercwl4', 'subject': '我是一封邮件1 ts:1602423677.533396', 'size': '2.3K', 'display_date': '昨日', 'date': '2020年10月11日 21:41 (星期日)'}, {'sender': 'testpay1', 'subject': '我是一封邮件1 ts:1602420622.2517993', 'size': '4K', 'display_date': '昨日', 'date': '2020年10月11日 20:50 (星期日)'}, {'sender': '123', 'subject': '我是一封邮件1 ts:1602417857.7165806', 'size': '2.1K', 'display_date': '昨日', 'date': '2020年10月11日 20:04 (星期日)'}, {'sender': 'testercwl4@yeah.net', 'subject': '我是一封邮件1 ts:1602410061.3159728', 'size': '2.3K', 'display_date': '昨日', 'date': '2020年10月11日 17:54 (星期日)'}, {'sender': 'testercwl4', 'subject': '我是一封邮件1 ts:1602390125.7198634', 'size': '2K', 'display_date': '昨日', 'date': '2020年10月11日 12:22 (星期日)'}, {'sender': '喜金牌', 'subject': '我是一封邮件1 ts:1602384199.8515599', 'size': '1.7K', 'display_date': '昨日', 'date': '2020年10月11日 10:43 (星期日)'}, {'sender': '我', 'subject': '我是一封邮件1 ts:1602384059.1399727', 'size': '1K', 'display_date': '昨日', 'date': '2020年10月11日 10:40 (星期日)'}, {'sender': 'testercwl4', 'subject': '我是一封邮件1 ts:1602383959.9529996', 'size': '2.3K', 'display_date': '昨日', 'date': '2020年10月11日 10:39 (星期日)'}, {'sender': 'testercwl4@yeah.net', 'subject': '我是一封邮件1 ts:1602376957.2683723', 'size': '2.8K', 'display_date': '昨日', 'date': '2020年10月11日 08:42 (星期日)'}, {'sender': 'testercwl4@yeah.net', 'subject': '我是一封邮件1 ts:1602376761.8498983', 'size': '2.3K', 'display_date': '昨日', 'date': '2020年10月11日 08:39 (星期日)'}, {'sender': 'testercwl4', 'subject': '我是一封邮件1 ts:1602372936.2905068', 'size': '2K', 'display_date': '昨日', 'date': '2020年10月11日 07:35 (星期日)'}, {'sender': 'iolveyou', 'subject': '我是一封邮件1 ts:1602362058.2900214', 'size': '2.1K', 'display_date': '昨日', 'date': '2020年10月11日 04:34 (星期日)'}])
    for i in test_list.filter_dict(subject__le='zlgCmigzrP ts:1602434126.178824'):
        print(i)

