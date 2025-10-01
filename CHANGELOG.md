# CHANGELOG

<!-- version list -->


## Unreleased


### Documentation


- Fix changelog issue
  ([`2ff1347`](https://github.com/pranavmishra90/faxlab-tools/commit/2ff134734c6a1fe9740c9ba8080ebef43b1443f2))



## v0.4.0 (2025-10-01)


## v0.3.0 (2025-10-01)

### Features

- **logger**: Custom python logger with exports to file, notebook, and open telemetry
  ([#5](https://github.com/pranavmishra90/faxlab-tools/pull/5),
  [`07fe6d5`](https://github.com/pranavmishra90/faxlab-tools/commit/07fe6d527850a41115ad273345c9d238376c5467))




## v0.2.0 (2025-09-30)

### Bug Fixes

- Add addtitional lint and pre-commit config
  ([`2a7aea7`](https://github.com/FacsimiLab/faxlab-tools/commit/2a7aea731cdeafc8201e5b1b28aecbbc39e7f801))

- Add version file in addition to pyproject
  ([`b028ef7`](https://github.com/FacsimiLab/faxlab-tools/commit/b028ef7db1bd845a1a117b62bd691479d5001432))


- Allow for fewer than 10 columns
  ([`0b9b051`](https://github.com/pranavmishra90/faxlab-tools/commit/0b9b0517dd35bd321e90f34b2938dfbfa65d50bc))


- Functions missing from __all__, remove re.escape to allow regex patterns. ensure categorical dtype
  before renaming categories.
  ([`fd52e66`](https://github.com/pranavmishra90/faxlab-tools/commit/fd52e6691a038445af9b200ae96bfc118e704954))

- Remove duplicate 'df_rename_sample_by_col_json'
  ([`4ba14da`](https://github.com/pranavmishra90/faxlab-tools/commit/4ba14da301f0e6531b1c468ed9ce6b0178f28d47))

### Continuous Integration



### Features

- Add a procedure to update a list of local envs which are using an editable install of this package
  ([`6c0b6a3`](https://github.com/pranavmishra90/faxlab-tools/commit/6c0b6a3f34674b79cef52eff4b15225fa3697e84))

- Add a procedure to update a list of local envs which are using an editable install of this package
  ([`e56b042`](https://github.com/pranavmishra90/faxlab-tools/commit/e56b042962123abe506850ca6713bb18b0f6ad11))

- Add module for transcriptomics analysis
  ([`adcb5bb`](https://github.com/pranavmishra90/faxlab-tools/commit/adcb5bb6153a579bf47ec5a78a5e7a9b1f079a94))


## v0.2.0-beta.3 (2025-09-23)

### Features

- Include a __version__.py which also updates from PSR
  ([`2c6408e`](https://github.com/pranavmishra90/faxlab-tools/commit/2c6408eece258989ac70d49a778b2f82529c1195))


## v0.2.0-beta.2 (2025-09-23)

### Build System

- Add version file in addition to pyproject
  ([`b028ef7`](https://github.com/pranavmishra90/faxlab-tools/commit/b028ef7db1bd845a1a117b62bd691479d5001432))

### Continuous Integration


- Fix error in uv run pytest
  ([`902b2d1`](https://github.com/pranavmishra90/faxlab-tools/commit/902b2d1994d0c58c9b12258712a175bbcf0baeb0))

### Features

- Add functions to rename categorical columns and a function to perform a find-replace using regex
  and an input json dictionary
  ([`77eb6ea`](https://github.com/pranavmishra90/faxlab-tools/commit/77eb6eaebe3a0fce69b26f312c233ed741fdd459))




## v0.2.0-beta.1 (2025-09-23)

### Bug Fixes

- Fix_column_dtype() and its unit tests
  ([`3951bcd`](https://github.com/pranavmishra90/faxlab-tools/commit/3951bcd9fb26115f44ead45f979526a59b458216))

- Return boolean on checking parameters on global
  ([`173c4dc`](https://github.com/pranavmishra90/faxlab-tools/commit/173c4dcc7f2f48e5b8cda273162722d7ba9f49f9))

### Continuous Integration

- Install uv and also add PSR for feat and fix branches
  ([`27e3b63`](https://github.com/pranavmishra90/faxlab-tools/commit/27e3b63859079509c2dd83a089994f2be9f2cc79))

- Install uv, run tests, but do not build as part of PSR
  ([`585b60a`](https://github.com/pranavmishra90/faxlab-tools/commit/585b60a3aba4c8046908561f8fe87dc8b4852eb1))

- Semantic versioning in the alpha stages will occur on the main branch, where breaking changes do
  not require a major version bump.
  ([`1694a58`](https://github.com/pranavmishra90/faxlab-tools/commit/1694a58f3e46294e8d1b1a64a565aceab09dd0dd))

### Documentation

- Add license
  ([`c558b82`](https://github.com/pranavmishra90/faxlab-tools/commit/c558b82ff46cbc12c872783147d599607770e01c))

### Features


- Add the CI/CD workflows from FacsimiLab
  ([`c0aabbe`](https://github.com/FacsimiLab/faxlab-tools/commit/c0aabbef60bfae889c5e6433b3a9385592f64aca))



- Add tool to report on the size of a file
  ([`caa40a0`](https://github.com/FacsimiLab/faxlab-tools/commit/caa40a0f5e2c987fc9ac84723b014e68d231ed23))

- Function to filter a dataframe based on a substring
  ([`681ec7f`](https://github.com/FacsimiLab/faxlab-tools/commit/681ec7f2611037b527036358caa8842e0fe86fb2))



- Initialize git-annex, which can be used for pytest processing larger files
  ([`cddba54`](https://github.com/FacsimiLab/faxlab-tools/commit/cddba5415be1f8f6e9ce596931ca5bfb210ac0ca))


- **io**: Add function to convert HDF5 to melted DataFrame
  ([`d7d1035`](https://github.com/pranavmishra90/faxlab-tools/commit/d7d1035488fff4762082f76afabfb9e7bab7537f))


## v0.1.0-beta.2 (2025-09-20)

### Features

- Add PSR build command to call uv build and update uv.lock
  ([`7460cd5`](https://github.com/pranavmishra90/faxlab-tools/commit/7460cd536c8e950630715e0f3e506ac8e22486de))


## v0.1.0-beta.1 (2025-09-20)

- Initial Release
