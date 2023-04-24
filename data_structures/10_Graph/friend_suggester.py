class User:
    def __init__(self,user_id,username,email,mobile):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.mobile = mobile
        
    def get_user_data(self):
        return {'id':self.user_id,'name':self.username,'email':self.email,'mobile':self.mobile}
    
    def show_user_data(self):
        for key in self.get_user_data():
            print(f"{key} :- {self.get_user_data()[key]}")

class Facebook:
    def __init__(self):
        self.users = {}
        
    def connect_user(self,user1,user2):
        """It connects the 2 user objects"""
        if user1 not in self.users:
            self.users[user1] = []
            
        if user2 not in self.users:
            self.users[user2] = []
            
        self.users[user1].append(user2)
        self.users[user2].append(user1)
        
    def get_friends(self,user1):
        """It returns all the user's friend object as a list"""
        return self.users[user1]
    
    def show_details(self):
        """It shows the details of each user and their friends"""
        for each_person in self.users:
            print(f"{each_person.user_id}.{each_person.username}")
            for ef in self.users[each_person]:
                print(f"  -{ef.username}")
            print("\n")
                
            

    
    def suggest_friends(self,user1,current_user,friends=[]):
        friends += [current_user]
        
        if friends.count(current_user) >= 2:
            return friends
        
        visited_friend = []
        suggested_friends = []
        for each_friend in self.users[current_user]:
            if each_friend not in visited_friend:
                new_friends = self.suggest_friends(user1,each_friend,friends)
                                                   
            if new_friends is not None:
                for esf in new_friends:
                    if esf not in self.users[user1] and  esf not in suggested_friends and esf != user1:
                        suggested_friends.append(esf)
                        
                    if esf not in visited_friend:
                        visited_friend.append(esf)
                    
        return suggested_friends
    
    def suggest_for(self,user):
        """It calls the suggest_friends method for suggesting the friends"""
        print(f"Suggested frieds for={user.username}")
        return self.suggest_friends(user,user,[])
                                                   
                                        
                                                   
        
#these are dummy details
u1 = User(1,"Suraj Rajesh Gupta","SurajGuptaRavi@gmail.com",8795148960)
u2 = User(2,"Sumit Mohan Naik","SumitNaik@gmail.com",8390888127)
u3 = User(3,"Shreya Mishra","ShreyaMishra@gmail.com",9284161739)
u4 = User(4,"Nakshatra Navrat","NakshatraNavrat@gmail.com",8390887531)
u5 = User(5,"Dhiraj Mishra","DhirajMishra@gmail.com",9852862960)
u6 = User(6,"Dale Lobo","DaleLobo@gmail.com",9784888127)
u7 = User(7,"Surya Nemiwal","SuryaNemiwal@gmail.com",8979162960)
u8 = User(8,"Raj Kushwaha","RajKushwaha@gmail.com",9267888127)
u9 = User(9,"Adarsh Srivastav","AdarshSrivastav@gmail.com",8390888127)
u10 = User(10,"Divyesh Pawar","DivyeshPawar@gmail.com",8390888127)
u11 = User(11,"Vidisha Barot","VidishaBarot@gmail.com",8390999127)
u12 = User(12,"Abhay Dwiwedi","AbhayDwiwedi@gmail.com",9267888127)
u13 = User(13,"Shivam Mishra","ShivamMishra@gmail.com",8390888127)
u14 = User(14,"Aditya Singh","AdityaSingh@gmail.com",8390888127)
u15 = User(15,"Ambuj Mishra","AmbujMishra@gmail.com",8390999127)
u16 = User(16,"Gautam","Gautam@gmail.com",9267888127)
u17 = User(17,"Shruti Gupta","ShrutiGupta@gmail.com",8390888127)
u18 = User(18,"Nisar Shah","NisarShah@gmail.com",8390888127)
u19 = User(19,"Ruchi","Ruchi@gmail.com",8390999127)

fb = Facebook()
fb.connect_user(u1,u2)
fb.connect_user(u1,u3)
fb.connect_user(u1,u4)
fb.connect_user(u1,u5)
fb.connect_user(u1,u17)
fb.connect_user(u1,u16)
fb.connect_user(u1,u8)
fb.connect_user(u1,u6)
fb.connect_user(u1,u18)

fb.connect_user(u2,u4)
fb.connect_user(u2,u5)
fb.connect_user(u2,u18)
fb.connect_user(u2,u3)
fb.connect_user(u2,u16)
fb.connect_user(u2,u6)

fb.connect_user(u3,u4)
fb.connect_user(u3,u8)

fb.connect_user(u4,u10)
fb.connect_user(u4,u11)
fb.connect_user(u4,u16)

fb.connect_user(u17,u19)
fb.connect_user(u17,u16)
fb.connect_user(u17,u11)

fb.connect_user(u16,u19)
fb.connect_user(u16,u11)

fb.connect_user(u18,u10)
fb.connect_user(u18,u9)
fb.connect_user(u18,u5)
fb.connect_user(u18,u6)

fb.connect_user(u9,u10)

fb.connect_user(u5,u6)
fb.connect_user(u5,u14)

fb.connect_user(u14,u12)
fb.connect_user(u14,u13)

fb.connect_user(u13,u12)

fb.connect_user(u8,u7)
fb.connect_user(u8,u15)

fb.connect_user(u15,u7)



#if you want to see the suggested friend list for u6 then pass u6 object in the below method
x = fb.suggest_for(u6)
print(f"Total Friends={len(x)}")
for e in x:
    print('-',e.username)
