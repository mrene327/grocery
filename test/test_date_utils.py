from grocery.date_utils import to_timestamp, timedelta_from_now


def test_to_timestamp():
    """Test the to_timestamp function."""
    date = '2016-01-01 10:00:00'
    print(1451613600000 == to_timestamp(date))

    date = '2016/01/01 10:00:00'
    print(1451613600000 == to_timestamp(date, '%Y/%m/%d %H:%M:%S'))


def test_timedelta_from_now():
    """Test the timedelta_from_now function."""
    print(timedelta_from_now(-2, 'days'))
    print(timedelta_from_now(-2, 'hours'))


if __name__ == '__main__':
    test_to_timestamp()
    test_timedelta_from_now()
