# OpenAI and FastAPI

This is an example pet name generator app used in the OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [FastAPI](https://fastapi.tiangolo.com/) web framework.

Chat completions doc: https://platform.openai.com/docs/guides/chat/introduction

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

   ```bash
   $ git clone https://www.url.com
   ```

3. Navigate into the project directory

   ```bash
   $ cd service-platform
   ```

4. Create a new virtual environment

   ```bash
   # Linux
   $ python -m venv venv
   $ source venv/bin/activate
   ```

   ```shell
   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file

   ```bash
   # Linux
   $ cp .env.example .env
   ```

   ```shell
   # Windows
   xcopy .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the app

   ```bash
   $ sh run.sh
   ```

You should now be able to access the app at [http://localhost:8000](http://localhost:8000)!

This repogitory is based on the Flask code at [openai-quickstart-python](https://github.com/openai/openai-quickstart-python). For the full context behind Flask app, check out the [Flask tutorial](https://beta.openai.com/docs/quickstart).

## Reference

- [openai/openai-quickstart-python](https://github.com/openai/openai-quickstart-python)

## Deploy - git branch

# DEV

git checkout develop
git commit and push ...

# PROD

git checkout production
git pull
git merge develop
