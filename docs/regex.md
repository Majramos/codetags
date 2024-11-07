


# current regex
```
(?:(?:# )(BUG|FIXME|NOTE|TODO)(?::))(.*?)(?:(?:<(.*?)>)|(?:\n))
```
- finds ending on <> or \n but no multiline suport

```
# NOTE: Lorem ipsum dolor sit amet
Lorem ipsum dolor sit amet, consectetur adipiscing elit

# NOTE: Lorem ipsum dolor sit amet <>
Lorem ipsum dolor sit amet, consectetur adipiscing elit # NOTE: Lorem ipsum dolor sit amet
# Lorem ipsum dolor sit amet <consectetur>

Lorem ipsum dolor sit amet, consectetur adipiscing elit

# NOTE: Lorem ipsum dolor sit amet <p:1>
Lorem ipsum dolor sit amet, consectetur adipiscing elit
# BUG: Lorem ipsum dolor sit amet <d:2022-01-01>

# TODO: Lorem ipsum dolor sit amet <d:2022-01-01 p:2>
Lorem ipsum dolor sit amet, consectetur adipiscing elit

# FIXME: Lorem ipsum dolor sit amet <p:2 d:2022-01-01>
```


# parse the extra fields

priority
```
p:([1-9]{1})
```

date
```
d:((?:(?:19|20)[0-9][0-9])-(?:0?[1-9]|1[012])-(?:0[1-9]|[12][0-9]|3[01]))
```


# old regex for fields
```
'(?:(?:(?:p:([1-3]))(?:.*?)(?:d:((?:(?:19|20)[0-9][0-9])-(?:0?[1-9]|1[012])-(?:0?[1-9]|[12][0-9]|3[01])))))|(?:(?:d:((?:(?:19|20)[0-9][0-9])-(?:0?[1-9]|1[012])-(?:0[1-9]|[12][0-9]|3[01])))(?:.*?)(?:p:([1-3])))|(?:p:([1-3]))|(?:d:((?:(?:19|20)[0-9][0-9])-(?:0?[1-9]|1[012])-(?:0?[1-9]|[12][0-9]|3[01])))'
```
