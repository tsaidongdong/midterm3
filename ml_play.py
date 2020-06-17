import math

class MLPlay:

    
    def __init__(self, player):
        self.player = player
        if self.player == "player1":
            self.player_no = 0
        elif self.player == "player2":
            self.player_no = 1
        elif self.player == "player3":
            self.player_no = 2
        elif self.player == "player4":
            self.player_no = 3
        self.car_vel = 0                            # speed initial
        self.car_pos = (0,0)                        # pos initial
        self.car_lane = self.car_pos[0] // 70       # lanes 0 ~ 8
        self.lanes = [35, 105, 175, 245, 315, 385, 455, 525, 595]  # lanes center
        pass

    def update(self, scene_info):
        """
        9 grid relative position
        |    |    |    |
        |  1 |  2 |  3 |
        |    |  5 |    |
        |  4 |  c |  6 |
        |    |    |    |
        |  7 |  8 |  9 |
        |    |    |    |       
        """
        def check_grid():
            grid = set()
            speed_ahead = 10
            if self.car_pos[0] <= 65: # left bound
                grid.add(1)
                grid.add(4)
                grid.add(7)
            elif self.car_pos[0] >= 565: # right bound
                grid.add(3)
                grid.add(6)
                grid.add(9)
            #判斷整個畫面
            CarPlace=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
            CarSpeed=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
            speed_ahead = 100
            for car in scene_info["cars_info"]:#判斷螢幕上車子的數量+位置                
                car_x=math.ceil(car["pos"][0]/70)-1
                car_y=math.ceil(car["pos"][1] /80)
                if car["id"] != self.player_no:
                    if car_x>=0 and car_x<9 and car_y>=-1 and car_y<=9:
                        CarPlace[car_y+1][car_x]=1
                        CarSpeed[car_y+1][car_x]=car["velocity"]
            #算left 6*1宮格的數量 middle 6*1宮格的數量 right 6*1宮格的數量
            #算left
            self_x=math.ceil(self.car_pos[0]/70)-1
            self_y=math.ceil(self.car_pos[1]/80)
            a=self_y
            b=self_x
            a=a-1
            b=b-1
            left_all_number=0
            exist_number=0
            left_space=0
            count_x=0
            exist_x=0
            count_y=0
            exist_y=0
            while a>=0 and count_y<5 and a<=10:
                count_y=count_y+1
                exist_y=exist_y+1
                while b>=0 and count_x<1 and b<=8:    
                    count_x=count_x+1  
                    exist_x=exist_x+1                 
                    if CarPlace[a][b]==1:
                        left_all_number=left_all_number+1
                    b=b-1
                else:
                    count_x=count_x+1 
                    b=b-1                 
                a=a-1
            else:
                count_y=count_y+1
                a=a-1
            exist_number=exist_x*exist_y
            left_space=((exist_number-left_all_number))
            print("left_space:",left_space)
            #算middle
            a=self_y
            b=self_x
            a=a-1
            b=b
            middle_all_number=0
            exist_number=0
            middle_space=0
            count_x=0
            exist_x=0
            count_y=0
            exist_y=0
            while a>=0 and count_y<5 and a<=10:
                count_y=count_y+1
                exist_y=exist_y+1
                while b>=0 and count_x<1 and b<=8:    
                    count_x=count_x+1
                    exist_x=exist_x+1                    
                    if CarPlace[a][b]==1:
                        middle_all_number=middle_all_number+1
                    b=b-1     
                else:
                    count_x=count_x+1
                    b=b-1              
                a=a-1
            else:
                count_y=count_y+1
                a=a-1
            exist_number=exist_x*exist_y
            middle_space=exist_number-middle_all_number
            print("middle_space:",middle_space)
            #算right
            a=self_y
            b=self_x
            a=a-1
            b=b+2
            right_all_number=0
            exist_number=0
            right_space=0
            count_x=0
            exist_x=0
            count_y=0
            exist_y=0
            while a>=0 and count_y<5 and a<=10:
                count_y=count_y+1
                exist_y=exist_y+1
                while b>=0 and count_x<1 and b<=8:    
                    count_x=count_x+1 
                    exist_x=exist_x+1                   
                    if CarPlace[a][b]==1:
                        right_all_number=right_all_number+1
                    b=b-1 
                else:
                    count_x=count_x+1
                    b=b-1                  
                a=a-1
            else:
                count_y=count_y+1
                a=a-1   
            exist_number=exist_x*exist_y
            right_space=((exist_number-right_all_number))
            print("right_space:",right_space)

            """print("computer car:")
            print(CarPlace[0])
            print(CarPlace[1])
            print(CarPlace[2])
            print(CarPlace[3])
            print(CarPlace[4])
            print(CarPlace[5])
            print(CarPlace[6])
            print(CarPlace[7])
            print(CarPlace[8])
            print(CarPlace[9])
            print(CarPlace[10])
            print("player:",self.car_pos)"""

            for car in scene_info["cars_info"]:
                if car["id"] != self.player_no:
                    x = self.car_pos[0] - car["pos"][0] # x relative position
                    y = self.car_pos[1] - car["pos"][1] # y relative position
                    if x <= 40 and x >= -40 :      
                        if y > 0 and y < 300:
                            grid.add(2)
                            if y < 200:
                                speed_ahead = car["velocity"]
                                grid.add(5) 
                        elif y < 0 and y > -200:
                            grid.add(8)
                    if x > -100 and x < -40 :
                        if y > 80 and y < 250:
                            grid.add(3)
                        elif y < -80 and y > -200:
                            grid.add(9)
                        elif y < 80 and y > -80:
                            grid.add(6)
                    if x < 100 and x > 40:
                        if y > 80 and y < 250:
                            grid.add(1)
                        elif y < -80 and y > -200:
                            grid.add(7)
                        elif y < 80 and y > -80:
                            grid.add(4)
            
            return move(grid= grid, speed_ahead = speed_ahead,left_space=left_space,middle_space=middle_space,right_space=right_space,self_x=self_x,self_y=self_y,CarSpeed=CarSpeed)
            
        def move(grid, speed_ahead,left_space,middle_space,right_space,self_x,self_y,CarSpeed): 
            # if self.player_no == 0:
            #     print(grid)
            if left_space>middle_space and left_space>right_space:#left
                print("LeftSpace MODEL")
                if(5 not in grid):#前方無緊急東西
                    if (1 not in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel:
                        return ["SPEED", "MOVE_LEFT"]
                    elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]>self.car_vel:
                        return ["SPEED","MOVE_LEFT"]
                    elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]<self.car_vel:
                        return ["BRAKE","MOVE_LEFT"]
                    elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]==self.car_vel:
                        return ["MOVE_LEFT"]
                    else :return ["SPEED"]
                else:#若有5 # NEED to BRAKE
                    if (1 not in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel: # turn left 
                        if self.car_vel < speed_ahead:
                            return ["SPEED", "MOVE_LEFT"]
                        else:
                            return ["BRAKE", "MOVE_LEFT"]
                    elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]>self.car_vel:
                        if self.car_vel < speed_ahead:
                            return ["SPEED", "MOVE_LEFT"]
                        else:
                            return ["BRAKE", "MOVE_LEFT"]
                    elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]<self.car_vel:
                        return ["BRAKE","MOVE_LEFT"]
                    elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]==self.car_vel:
                        if self.car_vel < speed_ahead:
                            return ["MOVE_LEFT"]
                        else:
                            return ["BRAKE", "MOVE_LEFT"]
                    else : 
                        if self.car_vel < speed_ahead:  # BRAKE
                            return ["SPEED"]
                        else:
                            return ["BRAKE"]
            elif right_space>middle_space and right_space>left_space:#right
                print("RightSpace MODEL")
                if(5 not in grid):#前方無緊急東西
                    if (3 not in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel:
                        return ["SPEED", "MOVE_RIGHT"]
                    elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]>self.car_vel:
                        return ["SPEED","MOVE_RIGHT"]
                    elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]<self.car_vel:
                        return ["BRAKE","MOVE_RIGHT"]
                    elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]==self.car_vel:
                        return ["MOVE_LEFT"]
                    else :return ["SPEED"]
                else:#若有5 # NEED to BRAKE
                    if (3 not in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel: # turn right
                        if self.car_vel < speed_ahead:
                            return ["SPEED", "MOVE_RIGHT"]
                        else:
                            return ["BRAKE", "MOVE_RIGHT"]
                    elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]>self.car_vel:
                        if self.car_vel < speed_ahead:
                            return ["SPEED", "MOVE_LEFT"]
                        else:
                            return ["BRAKE", "MOVE_LEFT"]
                    elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]<self.car_vel:
                        return ["BRAKE","MOVE_LEFT"]
                    elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]==self.car_vel:
                        if self.car_vel < speed_ahead:
                            return ["MOVE_LEFT"]
                        else:
                            return ["BRAKE", "MOVE_LEFT"]
                    else : 
                        if self.car_vel < speed_ahead:  # BRAKE
                            return ["SPEED"]
                        else:
                            return ["BRAKE"]
            elif middle_space>left_space and middle_space>right_space:#middle
                print("MiddleSpace MODEL")
                if len(grid) == 0:
                    return ["SPEED"]
                else:
                    if (2 not in grid): # Check forward 
                        # Back to lane center
                        return ["SPEED"]
                    else:
                        if (5 in grid): # NEED to BRAKE
                            if (4 not in grid) and (7 not in grid): # turn left 
                                if self.car_vel < speed_ahead:
                                    return ["SPEED", "MOVE_LEFT"]
                                else:
                                    return ["BRAKE", "MOVE_LEFT"]
                            elif (6 not in grid) and (9 not in grid): # turn right
                                if self.car_vel < speed_ahead:
                                    return ["SPEED", "MOVE_RIGHT"]
                                else:
                                    return ["BRAKE", "MOVE_RIGHT"]
                            else : 
                                if self.car_vel < speed_ahead:  # BRAKE
                                    return ["SPEED"]
                                else:
                                    return ["BRAKE"]
                        if (self.car_pos[0] < 60 ):
                            return ["SPEED", "MOVE_RIGHT"]#之後的是有漸層式的選擇模式
                        if (1 not in grid) and (4 not in grid) and (7 not in grid): # turn left 
                            return ["SPEED", "MOVE_LEFT"]
                        if (3 not in grid) and (6 not in grid) and (9 not in grid): # turn right
                            return ["SPEED", "MOVE_RIGHT"]
                        if (1 not in grid) and (4 not in grid): # turn left 
                            return ["SPEED", "MOVE_LEFT"]
                        if (3 not in grid) and (6 not in grid): # turn right
                            return ["SPEED", "MOVE_RIGHT"]
                        if (4 not in grid) and (7 not in grid): # turn left 
                            return ["MOVE_LEFT"]    
                        if (6 not in grid) and (9 not in grid): # turn right
                            return ["MOVE_RIGHT"]
            elif left_space==middle_space and middle_space>right_space:
                if self.car_pos[0]>315:#left
                    print("left_space==middle_space and LEFT")
                    if(5 not in grid):#前方無緊急東西
                        if (1 not in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel:
                            return ["SPEED", "MOVE_LEFT"]
                        elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]>self.car_vel:
                            return ["SPEED","MOVE_LEFT"]
                        elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]<self.car_vel:
                            return ["BRAKE","MOVE_LEFT"]
                        elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]==self.car_vel:
                            return ["MOVE_LEFT"]
                        else :return ["SPEED"]
                    else:#若有5 # NEED to BRAKE
                        if (1 not in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel: # turn left 
                            if self.car_vel < speed_ahead:
                                return ["SPEED", "MOVE_LEFT"]
                            else:
                                return ["BRAKE", "MOVE_LEFT"]
                        elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]>self.car_vel:
                            if self.car_vel < speed_ahead:
                                return ["SPEED", "MOVE_LEFT"]
                            else:
                                return ["BRAKE", "MOVE_LEFT"]
                        elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]<self.car_vel:
                            return ["BRAKE","MOVE_LEFT"]
                        elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]==self.car_vel:
                            if self.car_vel < speed_ahead:
                                return ["MOVE_LEFT"]
                            else:
                                return ["BRAKE", "MOVE_LEFT"]
                        else : 
                            if self.car_vel < speed_ahead:  # BRAKE
                                return ["SPEED"]
                            else:
                                return ["BRAKE"]
                else:#middle
                    print("left_space==middle_space and MIDDLE")
                    if len(grid) == 0:
                        return ["SPEED"]
                    else:
                        if (2 not in grid): # Check forward 
                            # Back to lane center
                            return ["SPEED"]
                        else:
                            if (5 in grid): # NEED to BRAKE
                                if (4 not in grid) and (7 not in grid): # turn left 
                                    if self.car_vel < speed_ahead:
                                        return ["SPEED", "MOVE_LEFT"]
                                    else:
                                        return ["BRAKE", "MOVE_LEFT"]
                                elif (6 not in grid) and (9 not in grid): # turn right
                                    if self.car_vel < speed_ahead:
                                        return ["SPEED", "MOVE_RIGHT"]
                                    else:
                                        return ["BRAKE", "MOVE_RIGHT"]
                                else : 
                                    if self.car_vel < speed_ahead:  # BRAKE
                                        return ["SPEED"]
                                    else:
                                        return ["BRAKE"]
                            if (self.car_pos[0] < 60 ):
                                return ["SPEED", "MOVE_RIGHT"]#之後的是有漸層式的選擇模式
                            if (1 not in grid) and (4 not in grid) and (7 not in grid): # turn left 
                                return ["SPEED", "MOVE_LEFT"]
                            if (3 not in grid) and (6 not in grid) and (9 not in grid): # turn right
                                return ["SPEED", "MOVE_RIGHT"]
                            if (1 not in grid) and (4 not in grid): # turn left 
                                return ["SPEED", "MOVE_LEFT"]
                            if (3 not in grid) and (6 not in grid): # turn right
                                return ["SPEED", "MOVE_RIGHT"]
                            if (4 not in grid) and (7 not in grid): # turn left 
                                return ["MOVE_LEFT"]    
                            if (6 not in grid) and (9 not in grid): # turn right
                                return ["MOVE_RIGHT"]
            elif left_space==right_space and right_space>middle_space:
                if self.car_pos[0]>350:#left
                    print("left_space==right_space and LEFT")
                    if(5 not in grid):#前方無緊急東西
                        if (1 not in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel:
                            return ["SPEED", "MOVE_LEFT"]
                        elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]>self.car_vel:
                            return ["SPEED","MOVE_LEFT"]
                        elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]<self.car_vel:
                            return ["BRAKE","MOVE_LEFT"]
                        elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]==self.car_vel:
                            return ["MOVE_LEFT"]
                        else :return ["SPEED"]
                    else:#若有5 # NEED to BRAKE
                        if (1 not in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel: # turn left 
                            if self.car_vel < speed_ahead:
                                return ["SPEED", "MOVE_LEFT"]
                            else:
                                return ["BRAKE", "MOVE_LEFT"]
                        elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]>self.car_vel:
                            if self.car_vel < speed_ahead:
                                return ["SPEED", "MOVE_LEFT"]
                            else:
                                return ["BRAKE", "MOVE_LEFT"]
                        elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]<self.car_vel:
                            return ["BRAKE","MOVE_LEFT"]
                        elif (1 in grid) and (4 not in grid) and CarSpeed[self_y+1][self_x-1]<self.car_vel and CarSpeed[self_y-1][self_x-1]==self.car_vel:
                            if self.car_vel < speed_ahead:
                                return ["MOVE_LEFT"]
                            else:
                                return ["BRAKE", "MOVE_LEFT"]
                        else : 
                            if self.car_vel < speed_ahead:  # BRAKE
                                return ["SPEED"]
                            else:
                                return ["BRAKE"]
                elif self.car_pos[0]<280:#right
                    print("left_space==right_space and RIGHT")
                    if(5 not in grid):#前方無緊急東西
                        if (3 not in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel:
                            return ["SPEED", "MOVE_RIGHT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]>self.car_vel:
                            return ["SPEED","MOVE_RIGHT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]<self.car_vel:
                            return ["BRAKE","MOVE_RIGHT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]==self.car_vel:
                            return ["MOVE_LEFT"]
                        else :return ["SPEED"]
                    else:#若有5 # NEED to BRAKE
                        if (3 not in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel: # turn right
                            if self.car_vel < speed_ahead:
                                return ["SPEED", "MOVE_RIGHT"]
                            else:
                                return ["BRAKE", "MOVE_RIGHT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]>self.car_vel:
                            if self.car_vel < speed_ahead:
                                return ["SPEED", "MOVE_LEFT"]
                            else:
                                return ["BRAKE", "MOVE_LEFT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]<self.car_vel:
                            return ["BRAKE","MOVE_LEFT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]==self.car_vel:
                            if self.car_vel < speed_ahead:
                                return ["MOVE_LEFT"]
                            else:
                                return ["BRAKE", "MOVE_LEFT"]
                        else : 
                            if self.car_vel < speed_ahead:  # BRAKE
                                return ["SPEED"]
                            else:
                                return ["BRAKE"] 
                else:#在中間車道 靠右
                    if(5 not in grid):#前方無緊急東西
                        if (3 not in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel:
                            return ["SPEED", "MOVE_RIGHT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]>self.car_vel:
                            return ["SPEED","MOVE_RIGHT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]<self.car_vel:
                            return ["BRAKE","MOVE_RIGHT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]==self.car_vel:
                            return ["MOVE_LEFT"]
                        else :return ["SPEED"]
                    else:#若有5 # NEED to BRAKE
                        if (3 not in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel: # turn right
                            if self.car_vel < speed_ahead:
                                return ["SPEED", "MOVE_RIGHT"]
                            else:
                                return ["BRAKE", "MOVE_RIGHT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]>self.car_vel:
                            if self.car_vel < speed_ahead:
                                return ["SPEED", "MOVE_LEFT"]
                            else:
                                return ["BRAKE", "MOVE_LEFT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]<self.car_vel:
                            return ["BRAKE","MOVE_LEFT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]==self.car_vel:
                            if self.car_vel < speed_ahead:
                                return ["MOVE_LEFT"]
                            else:
                                return ["BRAKE", "MOVE_LEFT"]
                        else : 
                            if self.car_vel < speed_ahead:  # BRAKE
                                return ["SPEED"]
                            else:
                                return ["BRAKE"] 
            elif middle_space==right_space and right_space>left_space:
                if self.car_pos[0]<315:#right
                    print("middle_space==right_space and RIGHT")
                    if(5 not in grid):#前方無緊急東西
                        if (3 not in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel:
                            return ["SPEED", "MOVE_RIGHT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]>self.car_vel:
                            return ["SPEED","MOVE_RIGHT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]<self.car_vel:
                            return ["BRAKE","MOVE_RIGHT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]==self.car_vel:
                            return ["MOVE_LEFT"]
                        else :return ["SPEED"]
                    else:#若有5 # NEED to BRAKE
                        if (3 not in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel: # turn right
                            if self.car_vel < speed_ahead:
                                return ["SPEED", "MOVE_RIGHT"]
                            else:
                                return ["BRAKE", "MOVE_RIGHT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]>self.car_vel:
                            if self.car_vel < speed_ahead:
                                return ["SPEED", "MOVE_LEFT"]
                            else:
                                return ["BRAKE", "MOVE_LEFT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]<self.car_vel:
                            return ["BRAKE","MOVE_LEFT"]
                        elif (3 in grid) and (6 not in grid) and CarSpeed[self_y+1][self_x+1]<self.car_vel and CarSpeed[self_y-1][self_x+1]==self.car_vel:
                            if self.car_vel < speed_ahead:
                                return ["MOVE_LEFT"]
                            else:
                                return ["BRAKE", "MOVE_LEFT"]
                        else : 
                            if self.car_vel < speed_ahead:  # BRAKE
                                return ["SPEED"]
                            else:
                                return ["BRAKE"]
                else:#middle
                    print("middle_space==right_space and MIDDLE")
                    if len(grid) == 0:
                        return ["SPEED"]
                    else:
                        if (2 not in grid): # Check forward 
                            # Back to lane center
                            return ["SPEED"]
                        else:
                            if (5 in grid): # NEED to BRAKE
                                if (4 not in grid) and (7 not in grid): # turn left 
                                    if self.car_vel < speed_ahead:
                                        return ["SPEED", "MOVE_LEFT"]
                                    else:
                                        return ["BRAKE", "MOVE_LEFT"]
                                elif (6 not in grid) and (9 not in grid): # turn right
                                    if self.car_vel < speed_ahead:
                                        return ["SPEED", "MOVE_RIGHT"]
                                    else:
                                        return ["BRAKE", "MOVE_RIGHT"]
                                else : 
                                    if self.car_vel < speed_ahead:  # BRAKE
                                        return ["SPEED"]
                                    else:
                                        return ["BRAKE"]
                            if (self.car_pos[0] < 60 ):
                                return ["SPEED", "MOVE_RIGHT"]#之後的是有漸層式的選擇模式
                            if (1 not in grid) and (4 not in grid) and (7 not in grid): # turn left 
                                return ["SPEED", "MOVE_LEFT"]
                            if (3 not in grid) and (6 not in grid) and (9 not in grid): # turn right
                                return ["SPEED", "MOVE_RIGHT"]
                            if (1 not in grid) and (4 not in grid): # turn left 
                                return ["SPEED", "MOVE_LEFT"]
                            if (3 not in grid) and (6 not in grid): # turn right
                                return ["SPEED", "MOVE_RIGHT"]
                            if (4 not in grid) and (7 not in grid): # turn left 
                                return ["MOVE_LEFT"]    
                            if (6 not in grid) and (9 not in grid): # turn right
                                return ["MOVE_RIGHT"]
            else:
                print("Not MODEL")
                if len(grid) == 0:
                    return ["SPEED"]
                else:
                    if (2 not in grid): # Check forward 
                        # Back to lane center
                        if self.car_pos[0] > self.lanes[self.car_lane]:
                            return ["SPEED", "MOVE_LEFT"]
                        elif self.car_pos[0 ] < self.lanes[self.car_lane]:
                            return ["SPEED", "MOVE_RIGHT"]
                        else :return ["SPEED"]
                    else:
                        if (5 in grid): # NEED to BRAKE
                            if (4 not in grid) and (7 not in grid): # turn left 
                                if self.car_vel < speed_ahead:
                                    return ["SPEED", "MOVE_LEFT"]
                                else:
                                    return ["BRAKE", "MOVE_LEFT"]
                            elif (6 not in grid) and (9 not in grid): # turn right
                                if self.car_vel < speed_ahead:
                                    return ["SPEED", "MOVE_RIGHT"]
                                else:
                                    return ["BRAKE", "MOVE_RIGHT"]
                            else : 
                                if self.car_vel < speed_ahead:  # BRAKE
                                    return ["SPEED"]
                                else:
                                    return ["BRAKE"]
                        if (self.car_pos[0] < 60 ):
                            return ["SPEED", "MOVE_RIGHT"]#之後的是有漸層式的選擇模式
                        if (1 not in grid) and (4 not in grid) and (7 not in grid) and self.car_pos[0] > self.lanes[self.car_lane]: # turn left 
                            return ["SPEED", "MOVE_LEFT"]
                        else: # turn right
                            return ["SPEED", "MOVE_RIGHT"]
        """if len(grid) == 0:
                return ["SPEED"]
            else:
                if (2 not in grid): # Check forward 
                    # Back to lane center
                    if self.car_pos[0] > self.lanes[self.car_lane]:
                        return ["SPEED", "MOVE_LEFT"]
                    elif self.car_pos[0 ] < self.lanes[self.car_lane]:
                        return ["SPEED", "MOVE_RIGHT"]
                    else :return ["SPEED"]
                else:
                    if (5 in grid): # NEED to BRAKE
                        if (4 not in grid) and (7 not in grid): # turn left 
                            if self.car_vel < speed_ahead:
                                return ["SPEED", "MOVE_LEFT"]
                            else:
                                return ["BRAKE", "MOVE_LEFT"]
                        elif (6 not in grid) and (9 not in grid): # turn right
                            if self.car_vel < speed_ahead:
                                return ["SPEED", "MOVE_RIGHT"]
                            else:
                                return ["BRAKE", "MOVE_RIGHT"]
                        else : 
                            if self.car_vel < speed_ahead:  # BRAKE
                                return ["SPEED"]
                            else:
                                return ["BRAKE"]
                    if (self.car_pos[0] < 60 ):#往中間跑
                        return ["SPEED", "MOVE_RIGHT"]
                    if (1 not in grid) and (4 not in grid) and (7 not in grid): # turn left 
                        return ["SPEED", "MOVE_LEFT"]
                    if (3 not in grid) and (6 not in grid) and (9 not in grid): # turn right
                        return ["SPEED", "MOVE_RIGHT"]
                    if (1 not in grid) and (4 not in grid): # turn left 
                        return ["SPEED", "MOVE_LEFT"]
                    if (3 not in grid) and (6 not in grid): # turn right
                        return ["SPEED", "MOVE_RIGHT"]
                    if (4 not in grid) and (7 not in grid): # turn left 
                        return ["MOVE_LEFT"]    
                    if (6 not in grid) and (9 not in grid): # turn right
                        return ["MOVE_RIGHT"]
                    """

        if len(scene_info[self.player]) != 0:
            self.car_pos = scene_info[self.player]

        for car in scene_info["cars_info"]:
            if car["id"]==self.player_no:
                self.car_vel = car["velocity"]

        if scene_info["status"] != "ALIVE":
            return "RESET"
        self.car_lane = self.car_pos[0] // 70
        return check_grid()

    def reset(self):
        """
        Reset the status
        """
        pass