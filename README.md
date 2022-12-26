To design a utility in Python or Node.js that can automatically migrate a GitHub repository to Bitbucket, including the branches, tags, and open pull requests, you could follow these steps:

Set up a new Bitbucket repository to receive the migrated code. This will be the destination repository for the migration.

Install the necessary libraries and dependencies. Depending on the language you choose, you may need to install certain libraries and dependencies to interact with the GitHub and Bitbucket APIs. For example, in Python, you might use the github3.py library to interact with the GitHub API and the bitbucket-api library to interact with the Bitbucket API. In Node.js, you could use the github and bitbucket-rest-api packages.

Authenticate with the GitHub and Bitbucket APIs. To access the repositories and other resources you'll need to migrate, you'll need to authenticate with the GitHub and Bitbucket APIs. This typically involves creating API keys or OAuth tokens and using them to authenticate your requests.

Fetch the repository metadata from GitHub. Use the GitHub API to fetch information about the repository you want to migrate, including the branches, tags, and open pull requests. You'll need this information to properly migrate the repository to Bitbucket.

Create the repository on Bitbucket. Use the Bitbucket API to create a new repository on Bitbucket. This will be the destination repository for the migrated code.

Migrate the repository and its contents. Use the Git command-line tools to clone the GitHub repository to your local machine, add the new Bitbucket repository as a remote, and push the code to the new remote. Be sure to include all branches, tags, and open pull requests in the migration.

Test the migrated repository. After the migration is complete, it's important to carefully test the migrated repository to ensure that everything was transferred correctly and that the repository is in good working order. This might involve checking the branches, tags, and pull requests to make sure they were transferred correctly, as well as running any tests or checks that you normally use to ensure the quality of your codebase.

By following these steps, you should be able to create a utility in Python or Node.js that can automatically migrate a GitHub repository to Bitbucket, including all branches, tags, and open pull requests.

This script uses the github3.py and bitbucket-api libraries to interact with the GitHub and Bitbucket APIs, respectively. It fetches the repository metadata from GitHub, creates a new repository on Bitbucket, and uses the Git command-line tools to migrate the code and its branches, tags, and open pull requests. Finally, it uses the Bitbucket API to create and merge new pull requests for any open pull requests on the original repository.
