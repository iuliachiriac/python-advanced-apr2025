# Python Training

This project contains materials for the Python Advanced Training. 
You can either access them in the browser, or clone and install the project locally, as described below.

## Project installation with PyCharm

1. Clone the repository inside `PycharmProjects` directory:

    ```shell
    cd ~/PycharmProjects/
    git clone https://github.com/iuliachiriac/python-advanced-apr2025
    ```
   
1. Open PyCharm, go to `File` -> `Open` and select the `python-advanced-apr2025` directory.
1. Select `Trust Project` in the dialog.
1. Next, PyCharm will advise you to create a Virtual Environment for your project. Leave the default options selected and click OK.
1. Run the Jupyter Notebook server:

    ```shell
    jupyter notebook
    ```

## Project installation without PyCharm

1. Clone the repository:

    ```shell
    git clone https://github.com/iuliachiriac/python-advanced-apr2025
    ```

1. Move to project directory:
    ```shell
    cd python-advanced-apr2025
    ```

1. Create a virtual environment:

    ```shell
    virtualenv venv
    ```

1. Activate virtual environment:

    Linux/MacOS:
    ```shell
    source venv/bin/activate
    ```

    Windows:
    ```shell
    venv\Scripts\activate
    ```

1. Install the requirements:

    ```shell
    pip install -r requirements.txt
    ```

1. Run the Jupyter Notebook server:

    ```shell
    jupyter notebook
    ```

## Getting solutions
After each day solutions will be submitted to this repo.
Since you've been working on your exercises and maybe altered files in the repo directory, use the following in a terminal, in the repo directory:

```shell
# forget unwanted changes in docs
git checkout -- docs/
# save your changes
git stash
# get the updates
git pull
# restore your changes
git stash pop
```

## Contact
Iulia Chiriac <iulia.chiriac.a@gmail.com>
