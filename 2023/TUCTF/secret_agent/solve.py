import heapq

graph = {
    "Attaya": {"Belandris": 10, "Charity": 3, "Delato": 5},
    "Belandris": {"Jolat": 15, "Gevani": 8, "Emell": 1},
    "Jolat": {"Osiros": 7, "Leter": 4, "Kepliker": 5},
    "Osiros": {"Shariot": 8, "Rhenora": 6},
    "Rhenora": {"Notasto": 2, "Shariot": 1},
    "Notasto": {"Shariot": 7},
    "Shariot": {"Attaya": 0},
    "Charity": {"Belandris": 8, "Emell": 2, "Flais": 8, "Haphsa": 3, "Delato": 1},
    "Emell": {"Gevani": 5, "Iyona": 3, "Flais": 5},
    "Gevani": {"Jolat": 8, "Iyona": 1, "Haphsa": 6},
    "Iyona": {"Jolat": 15, "Leter": 4, "Kepliker": 3},
    "Leter": {"Osiros": 3, "Rhenora": 10},
    "Delato": {"Flais": 5, "Iyona": 5, "Belandris": 3},
    "Flais": {"Gevani": 3, "Iyona": 3, "Haphsa": 1},
    "Haphsa": {"Iyona": 8, "Kepliker": 7, "Melyphora": 8, "Queria": 10, "Delato": 1},
    "Melyphora": {"Partamo": 4, "Shariot": 11, "Queria": 1},
    "Partamo": {"Osiros": 1, "Rhenora": 5, "Shariot": 9},
    "Kepliker": {"Leter": 5, "Osiros": 2, "Partamo": 6, "Queria": 7, "Delato": 2, "Melyphora": 5},
    "Queria": {"Partamo": 1, "Rhenora": 6, "Shariot": 10},
}

def dijkstra(graph, start, end):
    priority_queue = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_node = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_node[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous_node[current]

    return path

shortest_path = dijkstra(graph, "Attaya", "Shariot")
print(shortest_path)
#['Attaya', 'Charity', 'Emell', 'Iyona', 'Kepliker', 'Osiros', 'Rhenora', 'Shariot']

from pwn import *

#context.log_level = 'debug'

r = remote("chal.tuctf.com", 30012)
r.sendlineafter(b"KEY: ", b"A"*20)

r.recvuntil(b"Select an Option: ")
r.interactive()

'''
r.sendlineafter(b"Select an Option: ", b"3")
r.sendlineafter(b"Next Best Path to Take: ", shortest_path[1])
r.sendlineafter(b"Next Best Path to Take: ", shortest_path[2])
r.sendlineafter(b"Next Best Path to Take: ", shortest_path[3])
r.sendlineafter(b"Next Best Path to Take: ", shortest_path[4])
r.sendlineafter(b"Next Best Path to Take: ", shortest_path[5])
r.sendlineafter(b"Next Best Path to Take: ", shortest_path[6])
r.sendlineafter(b"Next Best Path to Take: ", shortest_path[7])
r.sendlineafter(b"Next Best Path to Take: ", b"done")
'''
#good_job_agent1089

'''
r.sendlineafter(b"Select an Option: ", b"4")
r.sendlineafter(b"Input the Key: ", b"good_job_agent1089")
'''
#⠥⠞⠀⠞⠉⠀⠎⠊⠋⠀⠍⠁⠀⠵⠁⠀⠝⠊⠀⠺⠊⠛⠀⠇⠇⠊⠀⠕⠉⠀⠍⠀⠑⠀⠃⠀⠅⠉⠁⠀⠛⠁⠀⠝⠊⠁

#https://gchq.github.io/CyberChef/#recipe=From_Braille()Find_/_Replace(%7B'option':'Regex','string':'%20'%7D,'%5C%5Cn',true,false,true,false)Reverse('Character')Reverse('Line')Find_/_Replace(%7B'option':'Regex','string':'%5C%5Cn'%7D,'',true,false,true,false)&input=4qCl4qCe4qCA4qCe4qCJ4qCA4qCO4qCK4qCL4qCA4qCN4qCB4qCA4qC14qCB4qCA4qCd4qCK4qCA4qC64qCK4qCb4qCA4qCH4qCH4qCK4qCA4qCV4qCJ4qCA4qCN4qCA4qCR4qCA4qCD4qCA4qCF4qCJ4qCB4qCA4qCb4qCB4qCA4qCd4qCK4qCB
#TUCTFISAMAZINGIWILLCOMEBACKAGAIN

'''
TYPE IN THE FLAG: $ TUCTFISAMAZINGIWILLCOMEBACKAGAIN

              o*0000000gp
           oo000         '0o 
           000             0
          000               00
         000                 00           o*0000000gp
         000                 00       oo000         '0o
         0000                07       000             0 
          000              007       000               00
           oo00           o07       000                 00       Let's GO!!!
              0*0000000*97          000                 00       You are Amazing!
                 I                  0000                07       Keep up the good work and Continue to help the world.
                  *             o*0000000gp           007        Flag: CONTINUE_THE_GOOD_WORK_2023
                   *         oo000         '0o       o07 
                     *      000             0  00000*97 
                      *    000               00 I
                       *  000                 00
                       *  000                 00
                      *   0000                07
                     *     000              007
                    *       oo00           o07
                    *           0*0000000*97 
                    *                I    *
                     *               *    *
                      *              *    *
                      *              *    *
                    *              *       *
                    *              *      *
                      *              *      *
                    *              *      *
                    *              *      *

Blessings Be Upon You. Good Bye!!
'''
#TUCTF{CONTINUE_THE_GOOD_WORK_2023}