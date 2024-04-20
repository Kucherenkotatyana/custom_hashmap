from hashmap import CustomHashMap


def test_set_value_new_value():
    """
    Returns a bucket with created data.
    """
    mock_key = "test_key"
    mock_value = "test_value"
    instance = CustomHashMap(size=1)

    assert instance.set_value(mock_key, mock_value) is None
    assert instance._hash_table[0] == [(mock_key, mock_value)]  # noqa: SLF001


def test_set_value_existed_value():
    """
    Returns a bucket with updated data with the same key.
    """
    mock_key = "test_key"
    mock_value = "test_value"
    mock_new_value = "another_test_value"
    instance = CustomHashMap(size=1)

    assert instance.set_value(mock_key, mock_value) is None
    assert instance.set_value(mock_key, mock_new_value) is None
    assert instance._hash_table[0] == [(mock_key, mock_new_value)]  # noqa: SLF001


def test_get_value_no_value_found():
    """
    Returns a string if there's no value in the hash table.
    """
    mock_key = "test_key"
    instance_hash_table_class = CustomHashMap(size=1)

    result = instance_hash_table_class.get_value(mock_key)  # noqa: SLF001
    assert result == "No record found"


def test_get_value_existed_value_found():
    """
    Returns a value if there's such key in the hash table.
    """
    mock_key = "test_key"
    mock_value = "test_value"
    instance_hash_table_class = CustomHashMap(size=1)
    instance_hash_table_class.set_value(mock_key, mock_value)

    result = instance_hash_table_class.get_value(mock_key)
    assert result == "test_value"


def test_delete_value_no_value_found():
    """
    Returns None if there wasn't such key in the hash table.
    """
    instance_hash_table_class = CustomHashMap(size=1)
    mock_key = "test_key"
    bucket = instance_hash_table_class._find_index(mock_key)  # noqa: SLF001

    result = instance_hash_table_class.delete_value(mock_key)
    assert result == "No record found"
    assert bucket == []
    assert instance_hash_table_class._get_key_and_index(  # noqa: SLF001
        bucket,
        mock_key,
    ) == (False, None)


def test_delete_value_value_deleted():
    """
    Returns a tuple with key and value deleted from the hash table.
    """
    mock_key = "test_key"
    mock_value = "test_value"
    instance_hash_table_class = CustomHashMap(size=1)
    instance_hash_table_class.set_value(mock_key, mock_value)

    result = instance_hash_table_class.delete_value(mock_key)
    assert result == ("test_key", "test_value")
