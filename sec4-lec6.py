# tests/runner.py
import unittest

# import your test modules
import player
import scenario
import thing

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
# suite.addTests(loader.loadTestsFromModule(player))
# suite.addTests(loader.loadTestsFromModule(scenario))
# suite.addTests(loader.loadTestsFromModule(thing))
# OR
models_to_test = [player,scenario,thing]
for model_to_test in models_to_test:
    suite.addTests(loader.loadTestsFromModule(model_to_test))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)