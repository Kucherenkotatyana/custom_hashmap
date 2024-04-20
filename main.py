import logging

from hashmap import CustomHashMap

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


if __name__ == "__main__":
    hash_map = CustomHashMap(50)

    # add values
    hash_map.set_value("first_task", "implement own hashmap class")
    hash_map.set_value("second_task", "write small service class")
    # updated hash table
    logger.debug(f"{hash_map}")

    # get a value
    logger.debug(f"Your value is: {hash_map.get_value("first_task")}")

    # delete a value
    logger.debug(
        f"Record {hash_map.delete_value(
            "second_task"
        )} was deleted.",
    )

    # updated hash table
    logger.debug(hash_map)

    # try deleting a non-existent record
    logger.debug(
        f"Can't delete the record: {hash_map.get_value("second_task")}",
    )
