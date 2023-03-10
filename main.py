import instaloader


class InstaSession:
    """An instagram session for a given user.

        Instance Attributes:
            - username: the username of the desired user to check
            - password: the password of the desired user to check
            - session: an instagram session for a given user
            - profile: a profile object of the given user

        Representation Invariants:
            - isInstance(self.username, str) and isInstance(self.password, str)
            - self.username != '' and self.password != ''
    """

    username: str
    password: str
    session: instaloader.Instaloader
    profile: instaloader.Profile

    def __init__(self, username, password):
        self.session = instaloader.Instaloader()
        self.username = username
        self.password = password
        self.session.login(self.username, self.password)
        self.profile = instaloader.Profile.from_username(self.session.context, self.username)
        self.followers_to_csv()
        self.followees_to_csv()

    def followers_to_csv(self):
        """ This method adds all the followers of the user to a csv file."""

        for follower in self.profile.get_followers():
            with open("followers.txt", "a+") as f:
                f.write(follower.username + '\n')

    def followees_to_csv(self):
        """ This method adds all the followees of the user to a csv file."""

        for followee in self.profile.get_followees():
            with open("followees.txt", "a+") as f:
                f.write(followee.username + '\n')

    def check_unfollowers(self):
        """ This method parses through the followers.txt and followees.txt files to print out a list of unfollowers
        for the user."""

        followers = set(follower.strip('\n\r') for follower in open('followers.txt').readlines())
        followees = set(followee.strip('\n\r') for followee in open('followees.txt').readlines())
        unfollowers = followees.difference(followers)
        print("These people do not follow you back:" + '\n')
        for unfollower in unfollowers:
            print(unfollower)


if __name__ == '__main__':
    newSesh = InstaSession(username='arjunm.17', password='promaster25')
    newSesh.check_unfollowers()
