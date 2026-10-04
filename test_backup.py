import backup, os

def test_should_return_false_when_no_argument():
    # Arrange
    path = ["./backup.py"]
    expected = False

    # Act
    actual = backup.has_argument(path)

    # Assert
    assert actual == expected, "expected False when there are no arguments."

def test_should_return_true_when_argument_was_passed():
    # Arrange
    path = ["./backup.py", os.path.join(".", "folders_to_backup.txt")]
    expected = True

    # Act
    actual = backup.has_argument(path)

    # Assert
    assert actual == expected, "expected True when there are two arguments."

def test_should_return_false_when_many_argument():
    # Arrange
    path = ["./backup.py", os.path.join(".", "folders_to_backup.txt"), os.path.join(".", "another_file.txt")]
    expected = False

    # Act
    actual = backup.has_argument(path)

    # Assert
    assert actual == expected, "expected False when there are no arguments."

def test_should_return_false_when_path_exists():
    # Arrange
    non_existing_folder = os.path.join(".", "non_existing_folder")
    expected = False

    # Act
    actual = backup.path_exists(non_existing_folder)

    # Assert
    assert actual == expected, "expected False when non existing folder path was given."

def test_should_return_true_when_path_exists():
    # Arrange
    non_existing_folder = os.path.join(".", "folders_to_backup.txt")
    expected = True

    # Act
    actual = backup.path_exists(non_existing_folder)

    # Assert
    assert actual == expected, "expected True when existing folder path was given."

def test_should_return_false_when_is_not_a_file():
    # Arrange
    path = os.path.join(".", "imaginary_folder")
    expected = False

    # Act
    actual = backup.is_file(path)

    # Assert
    assert actual == expected, "expected False when path is not a file."