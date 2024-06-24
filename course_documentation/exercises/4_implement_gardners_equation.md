# Implement Gardner's equation: https://en.wikipedia.org/wiki/Gardner%27s_relation

## Test

```python
def test_gardners_equation():
    velocity = 2000  # m/s
    expected_density = 2.0730949  # g/cm3

    # By default, approx considers numbers within a relative tolerance of 1e-6
    assert gardners_equation(velocity) == pytest.approx(expected_density)
    assert gardners_equation(velocity) == pytest.approx(expected_density, rel=1e-8) # Fails
    assert gardners_equation(velocity) == pytest.approx(expected_density, abs=1e-8) # Fails
```
