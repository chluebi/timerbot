
import time
NUMS = ['0','1','2','3','4','5','6','7','8','9','.']


def string_into_seconds(timestring):
    time_values = {'s':1,
                   'sec':1,
                   'm':60,
                   'min':60,
                   'h':3600,
                   'd':3600*24,
                   'w':3600*24*7,
                   'mon':3600*24*31,
                   'y':3600*24*365}
    end = []
    num = False
    abc = False
    timestring = timestring.replace(' ','')
    for let in timestring:
        if abc and num:
            raise Exception('This shouldn\'t happen')
        elif num:
            if let not in NUMS:
                end[-1][0] += let
            else:
                end[-1][1] += let
        elif abc:
            if let not in NUMS:
                end[-1][0] += let
            else:
                end.append(['', let])
        else:
            if let not in NUMS:
                num = False
                abc = not num
                continue

            end.append(['',let])

        abc = let not in NUMS
        num = not abc

    endsum = 0
    for form, am in end:
        try:
            endsum += time_values[form] * float(am)
        except:
            raise Exception(f'{form} is not a valid timetype')


    return endsum

def seconds_to_string(seconds):

    time_values = {'year': 3600 * 24 * 365,
                   'month': 3600 * 24 * 31,
                   'week': 3600 * 24 * 7,
                   'day': 3600 * 24,
                   'hour': 3600,
                   'minute': 60,
                   'second': 1
                   }

    rest = seconds
    end = []
    for key, value in time_values.items():
        if rest >= value:
            amount = int(rest // value)
            rest = rest % value
            if amount == 1:
                end.append(f'{amount} {key}')
            else:
                end.append(f'{amount} {key}s')

    if len(end) > 1:
        endstring = ', '.join(end[:-1])
        endstring += f' and {end[-1]}'
    else:
        endstring = end[0]

    return endstring

def strptime_list(timestring):
    try:
        return time.strptime(timestring, '%Y')
    except:
        pass
    try:
        return time.strptime(timestring, '%Y.%m.%d')
    except:
        pass
    try:
        return time.strptime(timestring, '%d.%m.%Y')
    except:
        pass
    try:
        return time.strptime(timestring, '%Y.%m.%d %H:%M')
    except:
        pass
    try:
        return time.strptime(timestring, '%d.%m.%Y %H:%M')
    except:
        pass
    try:
        c = time.localtime(time.time())
        end = time.strptime(f'{c.tm_year}.{c.tm_mon}.{c.tm_mday} {timestring}', '%Y.%m.%d %H:%M')
        return end
    except:
        pass
    try:
        c = time.localtime(time.time())
        end = time.strptime(f'{c.tm_year}.{c.tm_mon}.{c.tm_mday} {timestring}', '%Y.%m.%d %H:%M:%S')
        return end
    except:
        pass

    return None

def time_to_seconds(timestring):
    current_time = time.localtime(time.time())
    target_time = strptime_list(timestring)
    if target_time is None:
        raise Exception('Not a valid format')
    return time.mktime(target_time)



if __name__ == '__main__':
    print(time_to_seconds('12:01:00'))

