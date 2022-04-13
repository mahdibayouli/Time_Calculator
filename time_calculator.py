def add_time(time, dur, daysmsg=''):
    cleantime = time[:time.find(' ')].split(':')
    cleandur = dur.split(':')
    dayslist = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
    inttime = [int(cleantime[0]), int(cleantime[1])]
    intdur = [int(cleandur[0]), int(cleandur[1])]
    if time.find('PM') > -1:
        inttime[0] += 12
    result = [inttime[0] + intdur[0], inttime[1] + intdur[1]]
    result[0] += int(result[1]/60)
    result[1] = result[1] % 60
    days = int(result[0] / 24)
    result[0] = result[0] % 24
    
    am = ' AM'
    if int(result[0]/12) > 0:
        am = ' PM'
        result[0] -= 12
    if(result[0]==0):
        result[0] = 12
    if(len(daysmsg) > 0):
        daysmsg = daysmsg[0].upper() + daysmsg[1:].lower()
        newindex = (dayslist.index(daysmsg) + days) % 7
        daysmsg = ', ' + dayslist[newindex]
    difference = ''
    if (days > 0):
        if (days == 1):
            difference = ' (next day)'
        else:
            difference = ' ('+str(days)+' days later)'
    return (str(result[0]) + ':' + str(result[1]).rjust(2, '0') + am + daysmsg + difference)
