class DayGenerator:
    

    def generate(self, starting_date, starting_day):
        days = ['Mon', 'Tue', 'Wed', 'Thu','Fri', 'Sat','Sun']
        index = 0
        for i in range(0,7):
            if ( days[i] == starting_day):
                index = i
            

                
            
        if (starting_date > 15):
            for i in range(0,15):
                print(f'{days[index]} {starting_date}')
                starting_date += 1
                if (index < 6):
                    index +=1
                else:
                    index = 0

        else:
            for i in range(0,15):
                print(f'{days[index]} {starting_date}')
                starting_date += 1
                if (index < 6):
                    index +=1
                else:
                    index = 0

day = DayGenerator()
day.generate(1, 'Sat')
                
    