from grocery.helper import get_file_list, send_email


if __name__ == '__main__':
    # print(get_file_list('/Users/wchen/workspace/github/grocery', 'cfg'))
    send_email(
        smtp_svr='smtp.163.com',
        smtp_svr_port=465,
        account='testercwl@163.com',
        account_pwd='SSVVKFCUNOHTUGWM',
        to='testercwl@163.com',
        # cc='testercwl@126.com',
        # bcc='testercwl@yeah.net',
        subject='to cc bcc',
        content='to cc bcc',
        from_='testercwl4@126.com'
    )

