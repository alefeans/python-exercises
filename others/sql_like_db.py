"""
Design an SQL-like in-memory database. It should support:
- Database creation
- Table creation
- Inserts, simple select all and by id queries
- Schema validation

For schema validation, it should support validatios for:
- Positive integers
- Strings with less than 100 characters
"""

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional
from uuid import UUID, uuid4


class InvalidColumns(Exception):
    pass


class InvalidValue(Exception):
    pass


@dataclass
class Table:
    name: str
    schema: Dict[str, Callable[[Any], bool]] = field(default_factory=dict)
    entries: List[Dict[str, Any]] = field(default_factory=list, init=False)
    index: Dict[UUID, Dict[str, Any]] = field(default_factory=dict)

    def insert(self, entry: Dict[str, Any]) -> UUID:
        self.validate(entry)
        id = uuid4()
        entry["id"] = id
        self.entries.append(entry)
        self.index[id] = entry
        return id

    def select_all(self) -> List[Dict[str, Any]]:
        return self.entries

    def select_by_id(self, id: UUID) -> Optional[Dict[str, Any]]:
        return self.index.get(id)

    def validate(self, entry: Dict[str, Any]) -> None:
        allowed_columns = self.schema.keys()
        if entry.keys() != allowed_columns:
            raise InvalidColumns(f"Allowed columns are: '{allowed_columns}'")

        for column, value in entry.items():
            validation_fn = self.schema[column]
            if not validation_fn(value):
                raise InvalidValue(f"Invalid value {value} for column '{column}'")

    @staticmethod
    def valid_string(string: str, max_size: int = 100) -> bool:
        return len(string) < max_size

    @staticmethod
    def valid_int(n: int) -> bool:
        return n > -1


class TableAlreadyExists(Exception):
    pass


class TableNotFound(Exception):
    pass


@dataclass
class Database:
    name: str
    tables: Dict[str, Table] = field(default_factory=dict, init=False)

    def create_table(self, table: Table) -> None:
        if table.name in self.tables:
            raise TableAlreadyExists(f"Table {table.name} already exists")
        self.tables[table.name] = table

    def get_table(self, name: str) -> Table:
        table = self.tables.get(name)
        if table:
            return table
        raise TableNotFound(f"Table {name} doesn't exist")


if __name__ == "__main__":
    db = Database("MyDB")

    db.create_table(
        Table(
            "user",
            {"name": Table.valid_string, "age": Table.valid_int},
        )
    )
    user_table = db.get_table("user")
    user_table.insert({"name": "test", "age": 10})
    print(user_table.select_all())

    db.create_table(
        Table(
            "order",
            {"name": Table.valid_string, "price": Table.valid_int},
        )
    )
    order_table = db.get_table("order")
    order_table.insert({"name": "order 1", "price": 100.0})
    orders = order_table.select_all()
    id = orders[0]["id"]
    print(order_table.select_by_id(id))
