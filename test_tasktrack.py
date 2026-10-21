import pytest
from tasktrack import remove_task_by_number, load_tasks, save_tasks



@pytest.fixture
def sample_tasks():
    return ["Study", "Exercise", "Shop"]



@pytest.mark.parametrize(
        "task_number",
        [
            0,
            -1,
            10,
        ],
        ids=[
            "zero",
            "negative_number",
            "number_too_large",
        ],
)



def test_invalid_task_numbers_return_none(task_number):
    #Arrange
    tasks = ["Study", "Exercise", "Shop"]

    #Act
    result = remove_task_by_number(tasks, task_number)

    #Assert
    assert result is None
    assert tasks == ["Study", "Exercise", "Shop"]



def test_remove_first_task(sample_tasks):
    """Removing task 1 should remove the first task."""
    # Arrange
    task_number = 1
    expected_removed = "Study"

    # Act
    result = remove_task_by_number(sample_tasks, task_number)

    # Assert
    assert result == expected_removed
    assert sample_tasks == ["Exercise", "Shop"]



def test_remove_middle_task(sample_tasks):
    # Arrange
    task_number = 2
    expected_removed = "Exercise"

    # Act
    result = remove_task_by_number(sample_tasks, task_number)

    # Assert
    assert result == expected_removed
    assert sample_tasks == ["Study", "Shop"]



def test_remove_last_task(sample_tasks):
    # Arrange
    task_number = 3
    expected_removed = "Shop"

    # Act
    result = remove_task_by_number(sample_tasks, task_number)

    # Assert
    assert result == expected_removed
    assert sample_tasks == ["Study", "Exercise"]



def test_save_tasks_write_all_tasks(tmp_path):
    #Arrange
    test_file = tmp_path / "tasks.txt"
    tasks = ["Study", "Exercise", "Shop"]
    expected_text = "Study\nExercise\nShop\n"

    #Act
    save_tasks(tasks,test_file)

    #Assert
    assert test_file.read_text() == expected_text



def test_load_tasks_reads_all_tasks(tmp_path):
    #Arrange
    test_file = tmp_path / "tasks.txt"
    test_file.write_text("Study\nExercise\nShop\n")
    expected_tasks = ["Study", "Exercise", "Shop"]

    #Act
    result = load_tasks(test_file)

    #Assert
    assert result == expected_tasks



def test_load_tasks_ignores_blank_lines(tmp_path):
    #Arrange
    test_file = tmp_path / "tasks.txt"
    test_file.write_text("Study\n\n\nExercise\n\n\nShop\n")
    expected_tasks = ["Study", "Exercise", "Shop"]

    #Act
    result = load_tasks(test_file)

    #Assert
    assert result == expected_tasks



def test_load_tasks_handles_file_not_found(tmp_path):
    #Arrange
    test_file = tmp_path / "imaginary_file.txt"

    #Act
    result = load_tasks(test_file)

    #Assert
    assert result == []



def test_save_and_load_round_trip(tmp_path):
    #Arrange
    test_file = tmp_path / "tasks.txt"
    tasks = ["Study", "Exercise", "Shop"]

    #Act
    save_tasks(tasks, test_file)
    result = load_tasks(test_file)

    #Assert
    assert result == tasks