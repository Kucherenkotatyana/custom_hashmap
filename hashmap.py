from collections.abc import Hashable
from typing import Any


class CustomHashMap:

    def __init__(self, size: int) -> None:
        self._size = size
        # here we create empty hash table with given size
        self._hash_table = self._create_buckets()

    # create buckets in our hash table
    def _create_buckets(self) -> list[list]:  # type: ignore
        return [[] for _ in range(self._size)]

    def _find_index(self, key: Hashable) -> list[tuple[Hashable, Any]]:
        # use hash function to find index for a new key
        # (or find out where records with a given key are stored)
        # This helps to choose the index there the
        # key will be stored in the table.

        hashed_key = hash(key) % self._size
        # return the bucket associated with the index
        return self._hash_table[hashed_key]

    def _get_key_and_index(
            self,
            bucket: list[tuple[Hashable, Any]],
            key: Hashable,
    ) -> tuple[bool, int]:
        found_key = False
        index = None

        for index, record in enumerate(bucket):
            # get access to the data in current bucket
            record_key, record_value = record

            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                return found_key, index

        return found_key, index

    # add values to our hash map
    def set_value(self, key: Hashable, value: Any) -> None:
        bucket = self._find_index(key)

        found_key, found_index = self._get_key_and_index(bucket, key)

        # if there's the same key as the key to be inserted,
        # update the record with new value. Otherwise, add
        # the new record to the bucket
        if found_key:
            bucket[found_index] = (key, value)
        else:
            bucket.append((key, value))

    def get_value(self, key: Hashable) -> Any:

        bucket = self._find_index(key)

        found_key = False
        for index, record in enumerate(bucket):  # noqa
            record_key, record_value = record

            # check if the bucket has the key which
            # is being searched
            if record_key == key:
                found_key = True
                break

        # return value if there's such key
        # Otherwise, returns an information string.
        if found_key:
            return record_value
        return "No record found"

    # Remove a value with specific key
    def delete_value(self, key: Hashable) -> tuple[Hashable, Any] | str:

        bucket = self._find_index(key)

        found_key, found_index = self._get_key_and_index(bucket, key)

        # deletes data from the bucket if there's such key
        # and returns deleted data
        # Otherwise, returns an information string.
        if found_key:
            return bucket.pop(found_index)
        return "No record found"

    # Print the items of our hash map
    def __str__(self) -> str:
        return "".join(str(item) for item in self._hash_table)
