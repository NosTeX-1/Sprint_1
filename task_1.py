all_time = '1h 45m,360s,25m,30m 120s,2h 60s'

all_time = all_time.replace(' ', ',')
minut_sum = 0
list_time = all_time.split(',')
for i in list_time:
    if 'h' in i:
        i = i.replace('h', '')
        i = int(i) * 60
        minut_sum += i
    elif 'm' in i:
        i = i.replace('m', '')
        i = int(i)
        minut_sum += i
    elif 's' in i:
        i = i.replace('s', '')
        i = int(i) // 60
        minut_sum += i

print(minut_sum)