import json
import yaml
import dataclasses
from dacite import from_dict
from io import TextIOWrapper
from .logging import debug


def to_json(foo):
    return dataclasses.asdict(foo)


def from_json(builder, str_json):
    return from_dict(builder, json.loads(str_json))


def strip_string(s: str):
    return s.replace(" ", "_").replace(".", "-")


def into_file(f: TextIOWrapper, foo: dataclasses.dataclass):
    debug("Writing into %s", f.name)
    yaml.safe_dump(to_json(foo), f)


def from_file(f: TextIOWrapper, builder):
    debug("Loading from %s", f.name)
    return from_json(builder, yaml.safe_load(f))
