# Python - Unittests and Integration Tests

## Description of the files inside this folder:

0. This project module contains the first unit test for utils.access_nested_map. The TestAccessNestedMap class that inherits from unittest.TestCase. 
- Implement the TestAccessNestedMap.test_access_nested_map method to test that the method returns what it is supposed to. Decorate the method with @parameterized.expand.

1.  This project module contains the method TestAccessNestedMap.test_access_nested_map_exception. Use the assertRaises context manager to test that a KeyError is raised for inputs (use @parameterized.expand).

2. This project module contains the TestGetJson(unittest.TestCase) class and implement the TestGetJson.test_get_json method to test that utils.get_json returns the expected result.
- Use unittest.mock.patch to patch requests.get. Make sure it returns a Mock object with a json method that returns test_payload which you parametrize alongside the test_url that you will pass to get_json with inputs.
- Test that the mocked get method was called exactly once (per input) with test_url as argument.
- Test that the output of get_json is equal to test_payload.

3. This project module contains the TestMemoize(unittest.TestCase) class with a test_memoize method. Use unittest.mock.patch to mock a_method. Test that when calling a_property twice, the correct result is returned but a_method is only called once using assert_called_once.

4. This project module contains the TestGithubOrgClient(unittest.TestCase) class and implement the test_org method.

- This method should test that GithubOrgClient.org returns the correct value.
- Use @patch as a decorator to make sure get_json is called once with the expected argument but make sure it is not executed.
- Use @parameterized.expand as a decorator to parametrize the test with a couple of org examples to pass to GithubOrgClient, in this order google and abc.
- No external HTTP calls should be made.

5. This project module contains the test_public_repos_url method to unit-test GithubOrgClient._public_repos_url.
- Use patch as a context manager to patch GithubOrgClient.org and make it return a known payload.
- Test that the result of _public_repos_url is the expected one based on the mocked payload.

6. This project module contains the TestGithubOrgClient.test_public_repos method to unit-test GithubOrgClient.public_repos.
- Use @patch as a decorator to mock get_json and make it return a payload of your choice.
- Use patch as a context manager to mock GithubOrgClient._public_repos_url and return a value of your choice.
- Test that the list of repos is what you expect from the chosen payload.
- Test that the mocked property and the mocked get_json was called once.

7. This project module contains the TestGithubOrgClient.test_has_license method to unit-test GithubOrgClient.has_license.

8. This project module contains the TestIntegrationGithubOrgClient(unittest.TestCase) class and implement the setUpClass and tearDownClass which are part of the unittest.TestCase API.
- Test the GithubOrgClient.public_repos method in an integration test. That means that we will only mock code that sends external requests.
- Use @parameterized_class to decorate the class and parameterize it with fixtures found in fixtures.py. The file contains fixtures.
- The setupClass should mock requests.get to return example payloads found in the fixtures.
- Use patch to start a patcher named get_patcher, and use side_effect to make sure the mock of requests.get(url).json() returns the correct fixtures for the various values of url that you anticipate to receive.
- Implement the tearDownClass class method to stop the patcher.


## Languages and Tools:

- OS: Ubuntu 20.04 LTS
- Language: Python 3.8.10
- Style guidelines: [PEP 8](https://www.python.org/dev/peps/pep-0008/)

<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>


## Author

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>
