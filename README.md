# ics_creator

## Background

  - _...in progress_

## Installation

  - After `git clone` you need to `pip install -r requirements.txt`
  - If using `direnv` the `.envrc` should create a virtual environment for you, and hence the `pip` command above should work
  - `direnv` will probably also give an error to allow permission to run so a `direnv allow` will be needed
  - Ensure that the two environment variables in `.env` have been set to the appropriate file locations

## Clean-up and Test

  - Do a `rm -rf .direnv/` and `rm *.ics` to clean up generated files and do a complete clean of files in the directory
