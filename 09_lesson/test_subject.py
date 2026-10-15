from SubjectTable import SubjectTable

db = SubjectTable('postgresql://postgres:EgelmanKA_3009@localhost:5432/SkyPro')


def test_get_subjects():
    result = db.get_all_subject()

    assert len(result) > 0


def test_add_subject():
    name = "QA"
    db.add_subject(name)
    max_id = db.get_max_id()
    new_subject = db.get_subject_by_id(max_id)

    db.delete(max_id)

    assert new_subject["subject_title"] == name


def test_change_subject():
    max_id = db.create_random_subject()

    new_name = "QA Engineer"
    db.change_subject_title(new_name, max_id)
    updated = db.get_subject_by_id(max_id)

    db.delete(max_id)

    assert updated["subject_title"] == new_name


def test_delete_subject():
    max_id = db.create_random_subject()
    db.delete(max_id)

    result = db.get_subject_by_id(max_id)
    assert result is None
