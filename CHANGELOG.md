# CHANGELOG


## v0.3.0 (2025-10-01)

### Features

- **logger**: Custom python logger with exports to file, notebook, and open telemetry
  ([#5](https://github.com/FacsimiLab/faxlab-tools/pull/5),
  [`07fe6d5`](https://github.com/FacsimiLab/faxlab-tools/commit/07fe6d527850a41115ad273345c9d238376c5467))


## v0.2.0 (2025-09-30)

### Continuous Integration

- **semantic-release**: Automatic update - v0.2.0
  ([`82e6273`](https://github.com/FacsimiLab/faxlab-tools/commit/82e6273ef3024f4225bab5d9b0dd7c8296d6fc0e))


## v0.1.0 (2025-09-30)

### Bug Fixes

- Allow for fewer than 10 columns
  ([`0b9b051`](https://github.com/FacsimiLab/faxlab-tools/commit/0b9b0517dd35bd321e90f34b2938dfbfa65d50bc))

Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>

- Directory uses underscore rather than hyphen
  ([`4b26688`](https://github.com/FacsimiLab/faxlab-tools/commit/4b266888f834813e3fb5fb7ad19c38e56fea8983))

- Fix_column_dtype() and its unit tests
  ([`3951bcd`](https://github.com/FacsimiLab/faxlab-tools/commit/3951bcd9fb26115f44ead45f979526a59b458216))

- Functions missing from __all__, remove re.escape to allow regex patterns. ensure categorical dtype
  before renaming categories.
  ([`fd52e66`](https://github.com/FacsimiLab/faxlab-tools/commit/fd52e6691a038445af9b200ae96bfc118e704954))

- Remove duplicate 'df_rename_sample_by_col_json'
  ([`4ba14da`](https://github.com/FacsimiLab/faxlab-tools/commit/4ba14da301f0e6531b1c468ed9ce6b0178f28d47))

Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>

- Remove the pre-commit hook that prevents commits to main and release branches. we need it for
  local PSR
  ([`f594444`](https://github.com/FacsimiLab/faxlab-tools/commit/f59444483479d8bde7f209df9cccc5b3b4c8f2b3))

- Return boolean on checking parameters on global
  ([`173c4dc`](https://github.com/FacsimiLab/faxlab-tools/commit/173c4dcc7f2f48e5b8cda273162722d7ba9f49f9))

### Build System

- Add addtitional lint and pre-commit config
  ([`2a7aea7`](https://github.com/FacsimiLab/faxlab-tools/commit/2a7aea731cdeafc8201e5b1b28aecbbc39e7f801))

- Add version file in addition to pyproject
  ([`b028ef7`](https://github.com/FacsimiLab/faxlab-tools/commit/b028ef7db1bd845a1a117b62bd691479d5001432))

### Code Style

- End of file newline
  ([`67bde6f`](https://github.com/FacsimiLab/faxlab-tools/commit/67bde6febdc17989226c7928b388cff7fd352312))

- Format pyproject.toml
  ([`f43d951`](https://github.com/FacsimiLab/faxlab-tools/commit/f43d9517acfef74a04c3deedc50cdac6d91f01bf))

### Continuous Integration

- Add uv to the pipeline to prevent issues. PSR should not build
  ([#2](https://github.com/FacsimiLab/faxlab-tools/pull/2),
  [`cbc0095`](https://github.com/FacsimiLab/faxlab-tools/commit/cbc0095df61c3947d9d477432496bda5f6cbea04))

- Fix duplicate repo hooks
  ([`cc94f81`](https://github.com/FacsimiLab/faxlab-tools/commit/cc94f81f37ddd8f37b36229119d3f6cecc3d8af4))

- Fix error in uv run pytest
  ([`902b2d1`](https://github.com/FacsimiLab/faxlab-tools/commit/902b2d1994d0c58c9b12258712a175bbcf0baeb0))

- Fix missing project number
  ([`f8c07df`](https://github.com/FacsimiLab/faxlab-tools/commit/f8c07dfd4c8875952ce4b27e1ce5c299f2a18822))

- Fix token which was not working
  ([`277d629`](https://github.com/FacsimiLab/faxlab-tools/commit/277d62976190e71fb6eb1f78f7daf54f44d73a1f))

- Fix url typo
  ([`72d6d7a`](https://github.com/FacsimiLab/faxlab-tools/commit/72d6d7ae6a036970de75ec0493a762aaab004c55))

- Install uv and also add PSR for feat and fix branches
  ([`27e3b63`](https://github.com/FacsimiLab/faxlab-tools/commit/27e3b63859079509c2dd83a089994f2be9f2cc79))

- Install uv, run tests, but do not build as part of PSR
  ([`585b60a`](https://github.com/FacsimiLab/faxlab-tools/commit/585b60a3aba4c8046908561f8fe87dc8b4852eb1))

- Semantic versioning in the alpha stages will occur on the main branch, where breaking changes do
  not require a major version bump.
  ([`1694a58`](https://github.com/FacsimiLab/faxlab-tools/commit/1694a58f3e46294e8d1b1a64a565aceab09dd0dd))

- **semantic-release**: Automatic update - v0.1.0
  ([`c7ecbee`](https://github.com/FacsimiLab/faxlab-tools/commit/c7ecbee28d74ed3ba3ab9ed8830acbbe75c58cb8))

- **semantic-release**: Automatic update - v0.1.0
  ([`84f8d3d`](https://github.com/FacsimiLab/faxlab-tools/commit/84f8d3de27e30bce4758cb33b0e38ba7cca8577f))

- **semantic-release**: Automatic update - v0.1.0-beta.1
  ([`8fba61a`](https://github.com/FacsimiLab/faxlab-tools/commit/8fba61abcb11526b46662dbc025c71fe59840dd5))

- **semantic-release**: Automatic update - v0.1.0-beta.2
  ([`d79b628`](https://github.com/FacsimiLab/faxlab-tools/commit/d79b62885b254d9c43efa37b4c8edb1d28a9f98e))

- **semantic-release**: Automatic update - v0.2.0-beta.1
  ([`0678655`](https://github.com/FacsimiLab/faxlab-tools/commit/067865518bb4f035ddc490cf82f97e30d58eb021))

- **semantic-release**: Automatic update - v0.2.0-beta.2
  ([`0d523d3`](https://github.com/FacsimiLab/faxlab-tools/commit/0d523d308fa371974999e6b05df2680c0e72df88))

- **semantic-release**: Automatic update - v0.2.0-beta.3
  ([`4db4318`](https://github.com/FacsimiLab/faxlab-tools/commit/4db43189491afbb3311b381ed6bccfb5fff153cc))

### Documentation

- Add development for the package instructions, separate from using the editable install
  ([`8349d51`](https://github.com/FacsimiLab/faxlab-tools/commit/8349d51db4fb5fb5e0832eb4238898a8d36d5f45))

- Add license
  ([`c558b82`](https://github.com/FacsimiLab/faxlab-tools/commit/c558b82ff46cbc12c872783147d599607770e01c))

- Formatting h1
  ([`559ecf3`](https://github.com/FacsimiLab/faxlab-tools/commit/559ecf3cff5ad33989607ebd1204e6611ae545f5))

### Features

- Add a parameters module to manage loading from a 'parameters' file to global scope, checking if
  globals are loaded, and saving globals to a parameters file
  ([`4bbb11d`](https://github.com/FacsimiLab/faxlab-tools/commit/4bbb11d0cd50d08da1895b1db9aea827967b088d))

- Add a procedure to update a list of local envs which are using an editable install of this package
  ([`6c0b6a3`](https://github.com/FacsimiLab/faxlab-tools/commit/6c0b6a3f34674b79cef52eff4b15225fa3697e84))

- Add a procedure to update a list of local envs which are using an editable install of this package
  ([`e56b042`](https://github.com/FacsimiLab/faxlab-tools/commit/e56b042962123abe506850ca6713bb18b0f6ad11))

- Add functions to rename categorical columns and a function to perform a find-replace using regex
  and an input json dictionary
  ([`77eb6ea`](https://github.com/FacsimiLab/faxlab-tools/commit/77eb6eaebe3a0fce69b26f312c233ed741fdd459))

- Add gitignore, vscode settings, pre-commit hooks
  ([`dad873e`](https://github.com/FacsimiLab/faxlab-tools/commit/dad873e31885757b8d3bb8156eef30ae960ff04b))

- Add module for transcriptomics analysis
  ([`adcb5bb`](https://github.com/FacsimiLab/faxlab-tools/commit/adcb5bb6153a579bf47ec5a78a5e7a9b1f079a94))

- Add parameters functions to the utils
  ([`ae21a4a`](https://github.com/FacsimiLab/faxlab-tools/commit/ae21a4a81a9ad4b6368babd6da5a45f32ebc3ca3))

- Add PSR build command to call uv build and update uv.lock
  ([`7460cd5`](https://github.com/FacsimiLab/faxlab-tools/commit/7460cd536c8e950630715e0f3e506ac8e22486de))

- Add psr settings and init changelog
  ([`cb2fe69`](https://github.com/FacsimiLab/faxlab-tools/commit/cb2fe696729f6a49159c6e3d11910d0d6a197b69))

- Add santization.py which contains the fix_column_dtypes() function
  ([`2458101`](https://github.com/FacsimiLab/faxlab-tools/commit/2458101657bb091964eb322c8dcb2083f916b522))

- Add slicing functions for tables. define __all__ dynamically
  ([`dbb3611`](https://github.com/FacsimiLab/faxlab-tools/commit/dbb361108744792d116e20a757ebb71f7186bf80))

- Add the CI/CD workflows from FacsimiLab
  ([`c0aabbe`](https://github.com/FacsimiLab/faxlab-tools/commit/c0aabbef60bfae889c5e6433b3a9385592f64aca))

- Add the csv_to_dict() to io
  ([`b2a3904`](https://github.com/FacsimiLab/faxlab-tools/commit/b2a3904723912bef6425b318d72d8d859d6e5a1b))

- Add tool to report on the size of a file
  ([`caa40a0`](https://github.com/FacsimiLab/faxlab-tools/commit/caa40a0f5e2c987fc9ac84723b014e68d231ed23))

- Function to filter a dataframe based on a substring
  ([`681ec7f`](https://github.com/FacsimiLab/faxlab-tools/commit/681ec7f2611037b527036358caa8842e0fe86fb2))

- Include a __version__.py which also updates from PSR
  ([`2c6408e`](https://github.com/FacsimiLab/faxlab-tools/commit/2c6408eece258989ac70d49a778b2f82529c1195))

- Init directories
  ([`6e045d2`](https://github.com/FacsimiLab/faxlab-tools/commit/6e045d2178313805d110d1fdbf5610530cd6fb10))

- Initialize git-annex, which can be used for pytest processing larger files
  ([`cddba54`](https://github.com/FacsimiLab/faxlab-tools/commit/cddba5415be1f8f6e9ce596931ca5bfb210ac0ca))

- Initialize repository
  ([`3acb524`](https://github.com/FacsimiLab/faxlab-tools/commit/3acb5247f6e823f631109faad43ed047e86567fd))

- Wip porting the file_nb_logger(), adding a future stream logger
  ([`cb98a3b`](https://github.com/FacsimiLab/faxlab-tools/commit/cb98a3b49935aadac1cb959c1a72c5a22ac1baaa))

- **io**: Add function to convert HDF5 to melted DataFrame
  ([`d7d1035`](https://github.com/FacsimiLab/faxlab-tools/commit/d7d1035488fff4762082f76afabfb9e7bab7537f))
