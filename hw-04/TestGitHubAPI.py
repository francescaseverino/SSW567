import unittest

from GitHubAPI import gitUserInfo

class TestGitHubAPI(unittest.TestCase):

    def testRepoCount(self):
        repos = len(gitUserInfo('francescaseverino'))
        self.assertEqual(repos, 3, "user has 3 public repos")

    def testCommitCount(self):
        self.assertEqual(gitUserInfo('francescaseverino'), ['Repo: Focus-Bot Number of commits: 30', 'Repo: francescaseverino.github.io Number of commits: 2', 'Repo: SSW345 Number of commits: 28'])

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()