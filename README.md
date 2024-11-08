# codetags

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

Manage code comment markup in sections of code that need closer inspection or review

Based on [PEP 350](https://peps.python.org/pep-0350/#what-are-codetags)


## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install holidays.

```bash
git clone https://gitlab.com/majramos/codetags.git

cd codetags

pip install .
```
editable install
```bash
pip install -e . --no-build-isolatio
```

or
```bash
python -m pip install git+https://gitlab.com/majramos/codetags.git
```

## Usage/Examples



## General Syntax
Each codetag should be inside a comment, and can be any number of lines. It should not share a line with code. It should match the indentation of surrounding code. The end of the codetag is marked by a pair of angle brackets <> containing optional fields, which must not be split onto multiple lines. It is mandatory to have a codetag in # comments. There can be multiple fields per codetag, all of which are optional.

In short, a codetag consists of a mnemonic, a colon, commentary text, an opening angle bracket, an optional list of fields, and a closing angle bracket. E.g.,

```python
# MNEMONIC: Some (maybe multi-line) commentary. <field field ...>
```

### Mnemonics
The codetags of interest are listed below, using the following format:

```python
# TODO: ... <>
```
To do: Informal tasks/features that are pending completion.

```python
# FIXME: ... <>
```
Fix me: Areas of problematic or ugly code needing refactoring or cleanup.


```python
# BUG: ... <>
```
Bugs: Reported defects tracked in bug database.

```python
# NOTE: ... <>
```
Notes: Sections where a code reviewer found something that needs discussion or further investigation.


### Fields
All fields are optional

```python
<p:N >
```
Priority (p) level. Range (N) is from 0..3 with 3 being the highest. 0..3 are analogous to low, medium, high, and showstopper/critical.

```python
<d:YYYY[-MM[-DD]] >
```
The origination Date (d) indicating when the comment was added, in ISO 8601 format (digits and hyphens only).

## foundtags file
The codetags are copied verbatim from the original source file to a single file to make easier see what needs to be done and where.
The tags will be ordered either by alphabetical order, date or priority. In the case were date/priority is not given, it will fallback to alphabetical order


## Software dependencies
- python>=3.9


## Latest releases
[Release 0.0.1] - YYYY-MM-DD


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GPLv3](https://choosealicense.com/licenses/gpl-3.0/)


# Notes
