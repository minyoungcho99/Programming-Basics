class Video:
    def __init__(self, sound, minutes = 1.0): 
        self.sound = sound
        self.likes = 0
        self.comments = 0
        self.minutes = minutes
    def __str__(self):
        return "Video has {} likes and is {} minutes long.".format(self.likes, self.minutes)
    def __eq__(self, other):
            return self.sound == other.sound and self.comments == other.comments    
    def __repr__(self): #provided
        return f"Video({self.sound}, {self.likes}, {len(self.comments)}, {self.minutes})"
    
class Account:
    def __init__(self, username, password, isPrivate = True):
        self.username = username
        self.password = password
        self.followers = []
        self.following = []
        self.videos = []
        self.isPrivate = isPrivate
    def changePassword(self, oldPassword, newPassword):
        if oldPassword != self.password:
            return "Invalid password."
        else:
            self.password = newPassword        
    def isInfluencer(self):
        videoList = []
        for video in self.videos:
            if video.likes >= 50000 and video.comments >= 1000:
                videoList.append(video)
        if len(videoList) >= 5 and self.isPrivate == False:
            return True
        else:
            return False
    def follow(self, followedAccount):  
        if followedAccount not in self.following:
            self.following.append(followedAccount)
            followedAccount.followers.append(self)        
    def unfollow(self, unfollowedAccount):
         if unfollowedAccount in self.following:
            self.following.remove(unfollowedAccount)
            unfollowedAccount.followers.remove(self)         
    def __lt__(self, other):
        selfSum = 0 
        for video in self.videos:
            selfSum += video.likes
        otherSum = 0 
        for video in other.videos:
            otherSum += video.likes
        return selfSum < otherSum
    def __eq__(self, other):
        return self.username == other.username and self.password == other.password
    def __repr__(self):
        return f"Account({self.username}, {self.password}, {len(self.followers)}, {len(self.following)}, {len(self.videos)}, {self.isPrivate})"


class TikTok:
    def __init__(self):
        self.accounts = []
        self.followers = []
        self.following = []
        self.videos = []
        self.soundBase = []
    def makeAccount(self, username, password):
        usernameList = []
        for account in self.accounts:
            usernameList.append(account.username)    
        if username in usernameList:
            return "Username is already taken."
        else:
            newAccount = Account(username, password)
            self.accounts.append(newAccount)
            self.followers.append((newAccount.username, newAccount.followers))
            self.following.append((newAccount.username, newAccount.following))
    def changePrivacy(self, user):
        if user.isPrivate == True:
            user.isPrivate = False
        else:
            user.isPrivate = True         
    def deleteAccount(self, user):
        if user in self.accounts:
            self.accounts.remove(user)
            self.followers.remove((user.username, user.followers))
            self.following.remove((user.username, user.following))     
    def post(self, user, sound, minutes):
        if user.username not in self.accounts:
            return "You must have a registered account to post."
            if minutes < 0.25:
                return "Video must be at least 15 seconds."
            else:
                newVideo = Video(sound, minutes = 1.0)
                user.videos.append(newVideo)
                self.videos.append(newVideo)
    def getInfluencers(self):
        influencerList = []
        for account in self.accounts:
            if account.isInfluencer() == True:
                influencerList.append(account)
        return influencerList 
    def __repr__(self): 
        return f"TikTok Object with {len(self.accounts)} accounts and {len(self.videos)} videos"