# filter-predictor
Auto Image Filter Recommendation System 

### Setup

Here's how to set up `autofilter` for local development and testing.

1. Install [Miniconda](https://conda.io/miniconda.html)

2. Clone the repo locally::

    $ git clone https://github.com/prajnan93/filter-predictor.git

3. Create a Conda virtual environment using the `env.yml` file.  Install your local copy of the package into the environment::

    ```
    $ conda env create -f env.yml
    $ conda activate autofilter
    $ pre-commit install
    ```

    - After `git commit -m 'commit msg'`, pre-commit hooks will auto format codes in `.py` files.

    - This will require to stage `git add .` and commit `git commit -m 'commit msg'` again.

___