def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    total_min, total_sec = map(int,video_len.split(':'))
    total = total_min * 60 + total_sec
    
    start_min, start_sec = map(int, video_len.split(':'))
    start = start_min * 60 + start_sec
    
    op_startmin, op_startsec = map(int,op_start.split(':'))
    op_start_time = op_startmin * 60 + op_startsec
    
    op_endmin, op_endsec = map(int, op_end.split(':'))
    op_end_time = op_endmin * 60 + op_endsec
    
    pos_min, pos_sec = map(int, pos.split(':'))
    pos_time = pos_min * 60 + pos_sec
    
    for i in commands:
        if op_start_time <= pos_time <= op_end_time:
            pos_time = op_end_time
        if i == 'next':
            pos_time += 10
            if pos_time > total:
                pos_time = total
        else:
            pos_time -= 10
            if pos_time < 0:
                pos_time = 0
        if op_start_time <= pos_time <= op_end_time:
            pos_time = op_end_time
    answer_min = pos_time // 60
    answer_sec = pos_time % 60
    answer = f'{answer_min}:{answer_sec:02d}'
    if answer_min < 10:
        answer = '0' + answer
    return answer