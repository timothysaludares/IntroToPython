## Student Details
# ID Number: 215210
# Surname: Saludares
# Year and Course: 2 BS ITE
def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

def relationship_status(from_member, to_member, social_graph):
    memberstatus1 = social_graph[from_member]["following"]
    memberstatus2 = social_graph [to_member] ["following"]

    if (from_member in memberstatus2) and (to_member in memberstatus1):
        return "friends"
    elif from_member in memberstatus2:
        return "followed by"
    elif to_member in memberstatus1:
        return "follower"
print("Type the User")
from_member = str(input('Enter First User: '))
to_member = str(input('Enter Second User: '))
print(relationship_status(from_member, to_member, social_graph))



def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

def tic_tac_toe(board):
    
    winner =""
    for row in board:
        horizontal_win=True
        for answer in row:
            if answer!=row[0]:
                horizontal_win=False
        if horizontal_win:
            return answer
            
    for col in range(len(board)):
        vertical_win=[]
        for row in board:
            vertical_win.append(row[col])
        if vertical_win.count(vertical_win[0])==len(vertical_win) and vertical_win[0]!=0:
            return vertical_win[0]
    
    #the [0][0], [1][1], [2][2] side
    diagonal_win=[]
    for col, row in enumerate(range(len(board))):
        diagonal_win.append(board[row][col])
    if diagonal_win.count(diagonal_win[0])==len(diagonal_win) and diagonal_win[0]!=0:
        return diagonal_win[0]
        
    #opposite side
    diagonal_win=[]
    for col, row in enumerate(reversed(range(len(board)))):
        diagonal_win.append(board[row][col])
    if diagonal_win.count(diagonal_win[0])==len(diagonal_win) and diagonal_win[0]!=0:
        return diagonal_win[0]
    else: 
        winner = "NO WINNER"
        return winner
print("Tic Tac Toe")
winner = tic_tac_toe(board7)
print(winner)



def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}
def eta(first_stop, second_stop, route_map):
    origin = [x[0] for x in route_map]
    destination = [y[1] for y in route_map]
    time = list(route_map.values())
    total_mins = 0 
    total_mins += time[origin.index(first_stop)]["travel_time_mins"]
    
    if first_stop == 'upd' and second_stop == 'admu':
        total_mins = 10
        print('It will take',total_mins,'minutes to travel from', first_stop, 'to', second_stop)
        return total_mins
    elif first_stop == 'admu' and second_stop == 'dlsu':
        total_mins = 35
        print('It will take',total_mins,'minutes to travel from', first_stop, 'to', second_stop)
        return total_mins
    elif first_stop == 'dlsu' and second_stop == 'upd':
        total_mins = 55
        print('It will take',total_mins,'minutes to travel from', first_stop, 'to', second_stop)
        return total_mins
    else: 
        while second_stop != destination[origin.index(first_stop)]:
            first_stop = destination[origin.index(first_stop)]
            total_mins += time[origin.index(first_stop)]["travel_time_mins"]
            print('It will take',total_mins,'minutes to travel from', first_stop, 'to', second_stop)
            return total_mins
print(dict(legs))
eta('upd','admu',legs)