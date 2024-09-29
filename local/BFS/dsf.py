from collections import deque

def solution(tickets):
    for ticket in tickets:
        ticket.append(0) 
    length = len(tickets)+1
    tickets.sort(key = lambda x:x[1])     
    t = ["ICN"]                                          
    def dfs(port):                                       
        for ticket in tickets:               
            if ticket[0] == port and ticket[2] == 0:
                t.append(ticket[1]) 
                ticket[2] = 1
                if length == len(t) or dfs(ticket[1]):   
                    return t
                ticket[2] = 0
                t.pop()                                  
    answer = dfs("ICN")
    return answer