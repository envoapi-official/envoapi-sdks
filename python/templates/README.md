# Python generator adaptation

`model.py.jinja` is based on the template from `openapi-python-client` 0.29.1. Its upstream MIT license is retained in `LICENSE`; that license applies to this vendored template, not to the repository as a whole.

The only functional change adds required string and null checks in model deserialization. Without these checks, the generator's ordered union parser accepts a name-only company reference as the ID-only model, giving callers an incorrectly typed object. Regression tests cover all three company-reference variants. The same checks apply to other models that use these primitive fields.

Do not edit generated Python files. Update this template or generator configuration and run `pnpm generate`.
