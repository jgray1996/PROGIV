# Feedback on your portfolio

No that many commits (only 25), but the distribution is ok (all done between 9 and 24 August). Good that you have included a `.gitignore`-file, which is specific for this repo (not just copied some file from somewhere). Your commit messages could be a bit more descriptive. The code itself is nicely distributed over several classes / files / modules.

## Assignment 1

Good elaborations. Just a few small issues – please refer to the code itself.

## assignment 2

A very thorough and well thought through elaboration. I really enjoyed the story of the chef as an example of the factory pattern 😎. You also do a good job reflecting on the code and the patterns that we discussed.

## assignment 3

Good elaboration, though of course this is not that difficult an exercise.

## Assignment 4

Nice elaboration. A good thing to have your email and api key in a config file and not in your repo. You could have made this even better if you had provided a comparison between the mp and non-mp realisation of the downloads, but soit.

## Assignment final

You have a good and thorough readme, providing detailled instructions on how to install and run the application. You could have made it even more easy if you had the program create the necessary directories if they weren't found (remember to *automate everything*). However, when I run the program after training and I put new data in the `input`-directory, the system crashes:

```shell
Traceback (most recent call last):
  File "/Users/bart/Hanze/programming2/portfolios/james/assignment final/src/main.py", line 118, in <module>
    m.main()
  File "/Users/bart/Hanze/programming2/portfolios/james/assignment final/src/main.py", line 113, in main
    self.event_loop(training_mode=mode)
  File "/Users/bart/Hanze/programming2/portfolios/james/assignment final/src/main.py", line 76, in event_loop
    predictions = mod.classify(fit, mat_s)
                  ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bart/Hanze/programming2/portfolios/james/assignment final/src/model.py", line 94, in classify
    return model.predict(np_object)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/baba/.venv/bioinf/lib/python3.12/site-packages/sklearn/ensemble/_iforest.py", line 375, in predict
    decision_func = self.decision_function(X)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/baba/.venv/bioinf/lib/python3.12/site-packages/sklearn/ensemble/_iforest.py", line 410, in decision_function
    return self.score_samples(X) - self.offset_
           ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/baba/.venv/bioinf/lib/python3.12/site-packages/sklearn/ensemble/_iforest.py", line 437, in score_samples
    X = self._validate_data(X, accept_sparse="csr", dtype=tree_dtype, reset=False)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/baba/.venv/bioinf/lib/python3.12/site-packages/sklearn/base.py", line 654, in _validate_data
    self._check_n_features(X, reset=reset)
  File "/Users/baba/.venv/bioinf/lib/python3.12/site-packages/sklearn/base.py", line 443, in _check_n_features
    raise ValueError(
ValueError: X has 50 features, but IsolationForest is expecting 51 features as input.
```

You clearly forgot to do the same modifications on newly found data as you did on the trainings-data. Also, the log file remains empty (strangly enough).

