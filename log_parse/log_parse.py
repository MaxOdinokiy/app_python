# -*- encoding: utf-8 -*-

import re
from collections import Counter, defaultdict
import statistics


def parse(
        ignore_files=False,
        ignore_urls=[],
        start_at=None,
        stop_at=None,
        request_type=None,
        ignore_www=False,
        slow_queries=False
):
    def file_ignor(log):
        if not ignore_files:
            return False
        else:
            for num in range(len(log) - 1, 0, -1):
                if log[num] == '.':
                    return True
                elif log[num] == '/':
                    return False
            return False

    urls = []
    time = []
    url_time = []
    linefile = open('log.log', 'r')
    fl = True

    for line in linefile.readlines():
        if 'http' in line:
            request_date = re.split(r'\s', line)[0].replace('[', '')
            request_types = re.split(r'\s', line)[2].replace('"', '')
            request = re.split(r'\s', line)[3].replace('https://', '').replace('http://', '')
            response_time = int(re.split(r'\s', line)[6].replace('\n', ''))
            if start_at is None:
                start_at = request_date
            if not (request_date != start_at and fl):
                fl = False
                if request_date == stop_at:
                    break
                else:
                    if not (request_type is not None and request_types != request_type):
                        if not request in ignore_urls:
                            if not file_ignor(request):
                                if slow_queries:
                                    time.append(response_time)
                                if ignore_www:
                                    urls.append(request.replace('www.', ''))
                                    url_time.append([request.replace('www.', ''), response_time])
                                else:
                                    urls.append(request)
                                    url_time.append([request, response_time])

    urls2 = []
    times = []
    urls_time = defaultdict(list)
    if slow_queries is True:
        for key, value in url_time:
            urls_time[key].append(value)

        for item in urls_time:
            times.append(int(statistics.mean(urls_time[item])))
        return sorted(times, reverse=True)[0:5]
    else:
        for numb in Counter(urls).most_common(5):
            urls2.append(numb[1])
        return urls2

