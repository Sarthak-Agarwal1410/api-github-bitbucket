#This script uses the github3.py and bitbucket-api libraries to interact with the GitHub and Bitbucket APIs, respectively. 
#It fetches the repository metadata from GitHub, creates a new repository on Bitbucket, and 
#uses the Git command-line tools to migrate the code and its branches, tags, and open pull requests. 
#Finally, it uses the Bitbucket API to create and merge new pull requests for any open pull requests on the original repository.

import github3
import bitbucket_api

github_repo_url = 'https://github.com/Sarthak-Agarwal1410/repo'
bitbucket_repo_url = 'https://bitbucket.org/Sarthak1410/repo'
YOUR_GITHUB_TOKEN = 'a'

gh = github3.login(token = YOUR_GITHUB_TOKEN)
bb = bitbucket_api.Client(auth=('Sarthak1410', 'PASSWORD'))

github_repo = gh.repository(owner='Sarthak-Agarwal1410', repository='repo')
branches = [branch.name for branch in github_repo.branches()]
tags = [tag.name for tag in github_repo.tags()]
prs = [pr for pr in github_repo.pull_requests()]

# Create the repository on Bitbucket
bb.repositories.create(name='repo', is_private=True)

# Migrate the repository and its contents
!git clone $github_repo_url
!git remote add bitbucket $bitbucket_repo_url
!git push bitbucket --all
!git push bitbucket --tags

# Migrate the open pull requests
for pr in prs:
    bb_pr = bb.pullrequests.create(
        repository='repo',
        title=pr.title,
        description=pr.body,
        source={
            'branch': {
                'name': pr.head.ref
            }
        },
        destination={
            'branch': {
                'name': pr.base.ref
            }
        }
    )
    bb_pr.merge()
